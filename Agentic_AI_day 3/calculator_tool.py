def calculate_fee(total_fee, scholarship_percent):
    """
    Calculate the final course fee after applying a scholarship.
    """

    discount = total_fee * scholarship_percent / 100
    final_fee = total_fee - discount

    return (
        f"Original fee: ₹{total_fee:.2f}\n"
        f"Scholarship: {scholarship_percent}%\n"
        f"Scholarship amount: ₹{discount:.2f}\n"
        f"Final fee: ₹{final_fee:.2f}"
    )


if __name__ == "__main__":
    print(calculate_fee(15000, 25))