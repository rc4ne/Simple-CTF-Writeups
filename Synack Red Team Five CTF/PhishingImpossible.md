# CTF NAME - SYNACK RED TEAM FIVE CTF

# CATEGORY: FORENSICS

# DIFFICULTY: It had 2 stars with 164 solves.

# SOLUTION:

1. Downloading the attachment reveals a PDF. Description also hints about exploiting with PDF we can expect some shellcode inside file.
2. Use pdf-parser -c "file" to reveal object info. Looking at Object 8, we can see potential shell code there.
![op1](https://user-images.githubusercontent.com/83397936/140708069-7afe1afb-3157-439a-8d8e-309832aaf337.JPG)
![op2](https://user-images.githubusercontent.com/83397936/140708081-b2bf8a49-3c6c-4d76-b09d-823a5322a5d8.JPG)
3. Use "--raw" to reveal the code and the flag.
![op3](https://user-images.githubusercontent.com/83397936/140708254-bd4c6073-f142-4d00-a343-d75f2714b756.JPG)

