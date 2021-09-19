# TITANIC
# DESCRIPTION 
Tee-Tech is a rising cyber security organization which creates tools and provide cyber security solution to it's clients, but are they themself secure enough?

# SOLUTION
Well, well, well. This was interesting, though it was in "Easy" category for beginners like me I think this was just GREAT. Glad I figured it out in one go. It was a simple SSRF for localhost.

We are provided a website for the organization. On going through it, admin page is found as well as a functionality called "URL Capture" can be found. I first tried some basic authentication bypass through SQLi on admin page but all in vain. Then I switched to URL Capture, we can enter any url and it would show a screenshot of that webpage. Interesting right? 

I had looked at the  response headers and webserver was Apache. By now, I had clue about what can be possibly done. We need too access some file that is sensitive for servers in general. I knew few names that I tried to "hit-n-try" but didn't yield any result. It was quite late, but soon I tried entering the "localhost" and now it got simple.

1. Request a webpage "http://localhost/server-status"

![Tee](https://user-images.githubusercontent.com/83397936/133918493-5ce62af1-18d9-4817-9eb6-9ede7a82853b.JPG)

2. We can find juicy logs here. Notice the admin login credentials with GET request. (NOTICE THAT, the credentials are sent with GET Request! That's a security risk in itself.)

![status](https://user-images.githubusercontent.com/83397936/133918545-d2fd7698-9bb6-405c-ba0c-494c2603c0be.JPG)

3. You can try typing the credentials but I was lazy and I had tessaract installed so I used that :P (tessaract can be used for OCR, learn about it. It was also helpful in solving OTP Smasher, another challenge from same event.)

![tessaract](https://user-images.githubusercontent.com/83397936/133918580-4f627b70-cdc0-448a-856d-93eda03951c0.JPG)

![url](https://user-images.githubusercontent.com/83397936/133918582-3a700a7e-b673-4a7c-8766-07e0620ba91b.JPG)

4. Here, we have the flag. 

![flag](https://user-images.githubusercontent.com/83397936/133918589-68bd835e-cac3-4656-9059-c495ab50ac8a.JPG)
