class Checkbook:
    """
    A simple Checkbook class to manage a user's balance with functionalities
    to deposit, withdraw, and check the current balance.
    """
    def __init__(self):
        """
        Initialize the Checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
        amount (float): The amount to deposit. Must be positive.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Parameters:
        amount (float): The amount to withdraw. Must be positive and less than or equal to the current balance.

        Prints:
        - A success message with the updated balance if the withdrawal is successful.
        - An error message if there are insufficient funds.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook class.

    Allows the user to:
    - Deposit money into the checkbook.
    - Withdraw money from the checkbook.
    - Check the current balance.
    - Exit the program.

    Input validation is included to ensure the program does not crash due to invalid input.
    """
    cb = Checkbook()  # Initialize a new Checkbook object

    while True:
        # Prompt user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break  # Exit the loop and terminate the program
        elif action == 'deposit':
            try:
                # Prompt user for deposit amount
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be positive. Please try again.")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                # Prompt user for withdrawal amount
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be positive. Please try again.")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            # Display the current balance
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

