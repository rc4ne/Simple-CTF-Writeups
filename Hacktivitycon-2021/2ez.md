# 2ez
# DESCRIPTION
These warmups are just too easy! This one definitely starts that way, at least!

# SOLUTION
Using the "file" command reveals its an JPEG image, but opening it displays nothing (corrupted). Simple enough, header for JPEG must be wrong. 

1. Use command - hexedit 2ez_imhg
2. Notice the header seems wrong. It has "2EZ" embedded for no reason. You can check hex headers for different kind of files here - https://www.garykessler.net/library/file_sigs.html 

![image](https://user-images.githubusercontent.com/83397936/133918902-13fb3c5e-11e7-41de-a550-f7b84bc4a580.png)

3. Correct the header and save it.

![image](https://user-images.githubusercontent.com/83397936/133918916-281b1055-6eec-4cc8-a0c4-b7359b837fa2.png)

4. Open it to reveal the flag. 

![image](https://user-images.githubusercontent.com/83397936/133918927-ab4cb793-c76c-4de5-8173-f39e57c7d521.png)
