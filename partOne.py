def main():
    info = input("Tell me a bit about your interests and why you love them \n")
    SlowDown(info)

def SlowDown(info):
  slowedinfo = info.replace(" ","...")
  print (slowedinfo)

main()
