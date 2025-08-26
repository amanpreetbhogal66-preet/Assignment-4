user_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
     file.write(user_input + "\n")
print("Data sucessfully written to output.txt.")
additional_input = input("Enter additional text to append:")
with open("output.txt", "a") as file:
     file.write(additional_input + "\n")
print("Data sucessfully append")
print("\n final content of output.txt: ")
with open("output.txt", "r") as file:
     for line in file:
      print(line.strip())