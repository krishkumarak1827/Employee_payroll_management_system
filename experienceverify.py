def validate_experience(experience):
      while experience<0 or experience > 35 :
              print("experience can not be negative or not more then 35 years ")
              experience = int(input("Enter Years of Experience:"))
      return experience