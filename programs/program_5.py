
def generate_monthly_report(year, month, department):
    db_host = "localhost"
    db_user = "admin"
    db_pass = "password123"
    db_name = "company_data"
    
    print("Connecting to database...")
    
    
    if department == "sales":
        query = "SELECT * FROM sales WHERE YEAR(date) = " + str(year) + " AND MONTH(date) = " + str(month)
    elif department == "marketing":
        query = "SELECT * FROM marketing_campaigns WHERE YEAR(date) = " + str(year) + " AND MONTH(date) = " + str(month)
    elif department == "hr":
        query = "SELECT * FROM employee_records WHERE YEAR(hire_date) = " + str(year) + " AND MONTH(hire_date) = " + str(month)
    else:
        print("Error: Unknown department")
        return None
    

    print("Executing query: " + query)

    

    if department == "sales":
        results = [
            {"id": 1, "date": "2023-01-15", "amount": 1500, "customer": "ABC Corp"},
            {"id": 2, "date": "2023-01-22", "amount": 2200, "customer": "XYZ Inc"}
        ]
    elif department == "marketing":
        results = [
            {"id": 1, "date": "2023-01-10", "campaign": "Social Media", "cost": 5000, "leads": 120},
            {"id": 2, "date": "2023-01-20", "campaign": "Email", "cost": 1000, "leads": 45}
        ]
    else:
        results = [
            {"id": 1, "hire_date": "2023-01-05", "employee": "John Doe", "position": "Developer"},
            {"id": 2, "hire_date": "2023-01-12", "employee": "Jane Smith", "position": "Designer"}
        ]
    

    print("Generating report...")
    

    report = "========= Monthly Report =========\n"
    report += "Department: " + department + "\n"
    report += "Period: " + str(month) + "/" + str(year) + "\n"
    report += "================================\n\n"
    

    if department == "sales":
        total_sales = 0
        for sale in results:
            total_sales += sale["amount"]
            report += "Sale ID: " + str(sale["id"]) + "\n"
            report += "Date: " + sale["date"] + "\n"
            report += "Customer: " + sale["customer"] + "\n"
            report += "Amount: $" + str(sale["amount"]) + "\n"
            report += "-----------------\n"
        
        report += "\nTotal Sales: $" + str(total_sales) + "\n"
        

        if total_sales < 5000:
            commission_rate = 0.05
        elif total_sales < 10000:
            commission_rate = 0.07
        else:
            commission_rate = 0.1
        
        commission = total_sales * commission_rate
        report += "Commission (Rate: " + str(commission_rate * 100) + "%): $" + str(commission) + "\n"
    
    elif department == "marketing":
        total_cost = 0
        total_leads = 0
        for campaign in results:
            total_cost += campaign["cost"]
            total_leads += campaign["leads"]
            report += "Campaign: " + campaign["campaign"] + "\n"
            report += "Date: " + campaign["date"] + "\n"
            report += "Cost: $" + str(campaign["cost"]) + "\n"
            report += "Leads Generated: " + str(campaign["leads"]) + "\n"
            report += "-----------------\n"
        
        report += "\nTotal Cost: $" + str(total_cost) + "\n"
        report += "Total Leads: " + str(total_leads) + "\n"
        
        if total_leads > 0:
            cost_per_lead = total_cost / total_leads
            report += "Cost per Lead: $" + str(cost_per_lead) + "\n"
    
    else:
        for record in results:
            report += "Employee: " + record["employee"] + "\n"
            report += "Hire Date: " + record["hire_date"] + "\n"
            report += "Position: " + record["position"] + "\n"
            report += "-----------------\n"
        
        report += "\nTotal New Hires: " + str(len(results)) + "\n"
    

    filename = department + "_report_" + str(year) + "_" + str(month) + ".txt"
    print("Saving report to file: " + filename)

    print("\nReport Preview:")
    print(report)
    
    return report