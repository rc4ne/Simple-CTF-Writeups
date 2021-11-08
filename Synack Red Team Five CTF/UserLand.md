# CTF NAME - SYNACK RED TEAM FIVE CTF

# CATEGORY: WEB

# DIFFICULTY: It had 3 stars with 59 solves.

# SOLUTION:

1. Reading the description reveals some information about situation. It seems like investigating some illegal activity thingy.
2. We got login credentials from description. After logging in, we get several items to be purchased varying from some spying malware to backdoors etc.
3. There is also option of uploading files. Basic step is definitely to make a sample php file and try to upload it. So I made a simple phpinfo page and uploaded.
4. The app crashes revealing stack trace and lots of useful information. We can see it Laravel Framework. Going through app information revealed Laravel version to be 8.10.0

![debug](https://user-images.githubusercontent.com/83397936/140702691-250a0faa-1b94-4f15-8bfa-c7473c0b176b.JPG)

5. Googling for "Laravel version exploit" revealed some complicated results. Using phpggc it was possible to execute commands. Fortunately I found exploit script on github https://github.com/ambionics/laravel-exploits from the blog I came across.
6. I decided to make a reverse shell. For this purpose I used ngrok for port forwarding. I would recommend ngrok or such services for port forwarding if doing it from router is not possible for any reason. I have never tried maybe EC2 instances can also help here after editing inbound outbound rules.
7. Reverse shell was success, we found flag at /.
 
# STEPS AND SCREENSHOTS:

1. Open a tcp connection from ngrok. (We want reverse_tcp shell)
![userland_ngro](https://user-images.githubusercontent.com/83397936/140702269-90eb2182-d6de-41b5-9675-ffe0cbfe0741.JPG)

2. Open a nc connection for connect on tcp port specified above.
![nc](https://user-images.githubusercontent.com/83397936/140702341-f0659c24-42e0-4d34-adc2-78c2e2589dce.JPG)

3. Generate a payload executing command for reverse shell.
![laravel_1](https://user-images.githubusercontent.com/83397936/140702440-97fbf333-3eab-4f51-9b48-d05067d84d8f.JPG)

4. Run the exploit
![exploit1](https://user-images.githubusercontent.com/83397936/140702482-0631d9c8-e218-459d-a308-4040ceb2b2a2.JPG)
![working1](https://user-images.githubusercontent.com/83397936/140702561-c63cc2fd-d701-4b63-aa23-6690d73e3dc5.JPG)


5. Grab the Flag!
![flag](https://user-images.githubusercontent.com/83397936/140702608-c676ff50-782b-4911-b685-259874d846f8.JPG)
![flag display](https://user-images.githubusercontent.com/83397936/140702630-5181ee13-ed59-4dc3-ae97-c591178bfc91.JPG)

