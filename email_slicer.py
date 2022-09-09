email = input("Enter your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = f"Your USERNAME is '{username}' and your Domain name is '{domain_name}'"
print(format_)

