import datetime as dt

def calculate_age(birth_date):
    today = dt.datetime.today()
    age=today.year - birth_date.year

    if (today.month,today.year) < (birth_date.month,birth_date.year):
        age -= 1

    return age


def main():
    birth_date_input = input(" Enter Your Date of Birth (YYYY-MM-DD):")
    birth_date = dt.datetime.strptime(birth_date_input, "%Y-%m-%d")

    age = calculate_age(birth_date)

    print(f"Your Age is :{age}")

if __name__ == "__main__":
    main()
