Token = input("Please Enter Your Token: \t")
File = open("bot.py", 'r')
Contents = File.read()
File.close()
Contents = Contents.replace("**TOKEN**", Token)
File = open("bot.py", 'w')
File.write(Contents)
File.close
