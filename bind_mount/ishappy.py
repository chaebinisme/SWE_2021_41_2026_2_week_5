def isHappy(n):
  visited=set()
  while n!=1 and n not in visited:
    visited.add(n)
    n=sum(int(char)**2 for char in str(n))

  return n==1
if __name__ == "__main__":
 sample0_output = isHappy(19)
 sample1_output = isHappy(2)
 with open("/app/bind_mount/output.txt", "w") as f:
      f.write(f"19: {sample0_output}\n")
      f.write(f"2: {sample1_output}\n")
 print("Results saved to /app/bind_mount/output.txt")