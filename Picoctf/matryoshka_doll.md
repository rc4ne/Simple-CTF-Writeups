# CTF NAME - PICOCTF

# CHALLENGE DESCRIPTION:
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5ef2e9103d55972d975437f68175b9ab/dolls.jpg)

# SOLUTION:
Using binwalk we can find out that file can be unzipped. Once you unzip, you need to unzip the extracted file. This is a simple Python script that does this until .txt file is obtained.
This can probably be done in better way such as by 1-2 line bash script, but I just went this way. Script can be found with name [extract.py](https://github.com/rc4ne/Simple-CTF-Writeups/blob/main/Picoctf/extract.py)
 
# FLAG: 
picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}

![pico](https://user-images.githubusercontent.com/83397936/118254823-1fceba00-b4c9-11eb-84c3-3aff1c7582ba.JPG)

