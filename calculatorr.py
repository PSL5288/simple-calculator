print("=" * 40)
print("        SIMPLE CALCULATOR")
print("=" * 40)

# Taking numbers
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

print("\nChoose an operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter choice (1/2/3/4): ")

# Starting result
result = numbers[0]

# Performing operations
for num in numbers[1:]:

    if choice == "1":
        result += num

    elif choice == "2":
        result -= num

    elif choice == "3":
        result *= num

    elif choice == "4":
        if num != 0:
            result /= num
        else:
            print("\n❌ Cannot divide by zero")
            break

    else:
        print("\n❌ Invalid choice")
        break

else:
    print("\n" + "=" * 40)
    print("✅ Final Result =", result)
    print("=" * 40)