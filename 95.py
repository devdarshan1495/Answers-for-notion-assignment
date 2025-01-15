class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def show_message():
        print("This is a static method.")

Counter.increment()
Counter.increment()
print(f"Count after incrementing: {Counter.count}")

Counter.show_message()
