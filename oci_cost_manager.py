import oci
import datetime
import csv
from tabulate import tabulate

def get_last_month_dates():
    """
    Calculates the start and end dates for the previous full calendar month.
    """
    today = datetime.date.today()
    first_day_current_month = today.replace(day=1)
    last_day_prev_month = first_day_current_month - datetime.timedelta(days=1)
    first_day_prev_month = last_day_prev_month.replace(day=1)
    return first_day_prev_month, first_day_current_month

def export_to_csv(data, headers, filename="monthly_cost_breakdown.csv"):
    """
    Exports the cost data to a CSV file.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"\n[Success] Data exported to {filename}")
    except Exception as e:
        print(f"[Error] Could not write to CSV: {e}")

def analyze_monthly_costs(config_profile="DEFAULT"):
    try:
        # Load config
        config = oci.config.from_file(profile_name=config_profile)
        usage_client = oci.usage_api.UsageapiClient(config)
        
        # Date range
        start_date, end_date = get_last_month_dates()
        print(f"Analyzing costs from {start_date} to {end_date}...\n")

        # Request Details
        request_details = oci.usage_api.models.RequestSummarizedUsagesDetails(
            tenant_id=config['tenancy'],
            time_usage_started=start_date.strftime('%Y-%m-%dT00:00:00Z'),
            time_usage_ended=end_date.strftime('%Y-%m-%dT00:00:00Z'),
            granularity='MONTHLY',
            query_type='COST',
            group_by=['service'] 
        )

        # API Call
        response = usage_client.request_summarized_usages(request_details)
        
        # Process Data
        cost_data = []
        total_cost = 0.0
        currency = "USD"

        for item in response.data.items:
            service_name = item.service if item.service else "Other/Adjustment"
            cost = item.computed_amount if item.computed_amount else 0.0
            
            if item.currency:
                currency = item.currency

            if cost > 0:
                cost_data.append([service_name, cost])
                total_cost += cost

        # Sort and Add Total
        cost_data.sort(key=lambda x: x[1], reverse=True)
        
        # Prepare data for CSV (raw numbers) vs Table (formatted strings)
        csv_data = cost_data.copy()
        csv_data.append(["TOTAL", total_cost])

        # Display Table
        table_headers = ["Service", f"Cost ({currency})"]
        formatted_table_data = [[row[0], f"{row[1]:,.2f}"] for row in csv_data]
        print(tabulate(formatted_table_data, headers=table_headers, tablefmt="grid"))

        # Export CSV
        export_to_csv(csv_data, ["Service", "Cost"])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_monthly_costs()
