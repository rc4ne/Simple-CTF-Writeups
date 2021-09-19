## BAD WORDS 
# DESCRIPTION 
You look questionable... if you don't have anything good to say, don't say anything at all! 

# SOLUTION
This was rather simple one. We were provided with instance access to a bash terminal. All the basic commands were blocked, ex- ls,whoami,cd etc. The idea was simple, to utilize where the commands are being "stored" for user access. I was able to ultimately traverse directory and obtain the flag through head.

1. Locate the command needed.
To run ls, try /usr/bin/ls, doesn't work. Try /bin/ls

2. Traverse the directory by listing them out.

![1](https://user-images.githubusercontent.com/83397936/133918183-eb17c9a0-f16c-424d-904d-c0ef6e7faa5f.JPG)

3. Print the flag using some command like head.

![flag](https://user-images.githubusercontent.com/83397936/133918194-85688e60-2bd7-46a7-94a7-3574bb38c0fa.JPG)
