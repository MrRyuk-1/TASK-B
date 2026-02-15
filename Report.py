#Task -B
class SalesReport:
    def __init__(self):
        self.weekly_sales = 0
        self.monthly_sales = 0
        self.single_sales = 0

    def add_sale(self, pass_type, amount):
        if pass_type == "Weekly":
            self.weekly_sales += max(0, amount)
        elif pass_type == "Monthly":
            self.monthly_sales += max(0, amount)
        elif pass_type == "Single":
            self.single_sales += max(0, amount)

    def show_report(self):
        print("\nSales Report by Pass Type:")
        print(f"Weekly Pass: ${self.weekly_sales:.2f}")
        print(f"Monthly Pass: ${self.monthly_sales:.2f}")
        print(f"Single Entry Pass: ${self.single_sales:.2f}")


r = SalesReport()

r.add_sale("Weekly", float(input("Weekly Sale Amount: $")))
r.add_sale("Monthly", float(input("Monthly Sale Amount: $")))
r.add_sale("Single", float(input("Single Entry Sale Amount: $")))

r.show_report()
