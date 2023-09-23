# Description
This challenge was in the Android Category. An APK was provided, we needed to call something that shouldn't be possible. Clearly, this hinted at calling some non-exported components in one or other way. You can find the original file as well as the exploit APK attached to this folder. 

### Note: This can very well be done with a single Frida script. I wrote this article to show a manual approach, step-by-step. 

# Steps

1. Open the APK inside jadx-gui and open the AndroidManifest.xml file. We observe that there are 3 activities of concern - An exported MainActivity, An exported HandleActivity, and one non-exported DeepLinkActivity.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/cf4bd7c0-d133-4a55-907c-1715e1a88285)

2. Let's take a look at HandleActivity. It is observed that a parcelable intent will be accepted here named "activity".

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/402b8688-3944-4f03-b565-deebfccb7224)

3. Now let us take a look at DeepLinkActivity. On creation, this will accept an intent and then perform scheme and host validation on the received URL. If it is a success, i.e., the passed intent is "https://winja.nullcon.net" then a javascript interface will be added called "app" and the URL will be loaded within webview. This javascript interface enables calling of makeToast() method which will make a toast message of the flag and log it.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/af04e238-d908-4c0d-9fc3-072097a7e0dc)

4. The exploit plan - Create an APK that will call "HandleActivity" with a parcelable intent calling DeepLinkActivity. Open Android Studio, create a new project and inside the main activity add any button (or choose a template having a button). In the attached screenshot - (1) Explains how HandleActivity would be called. (2) We are setting data URI to pass to DeepLinkActivity. (3) We set this data to be sent as Extra. (4) We will send the intent for HandleActivity, encapsulating the activity call with data URI to DeepLinkActivity.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/276dea56-df2f-4ade-a518-bc890ee01be0)

5. Launch the created exploit app. Click the button where the above logic is embedded.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/043abc48-87f0-4047-ab78-fa118a06a141)

6. The webview will launch for URL "https://winja.nullcon.net".

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/73e5f098-b06b-4fcf-90ad-404c37534f08)

7. Now to access JS Interface, open Chrome and navigate to "chrome://inspect". It will show webview opened in connected devices and allow inspecting.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/e2ec3849-2bee-48f3-9a73-2ce59ad0c76b)

8. In the console, try to call the "app" interface. We see makeToast() method is callable. Call it.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/1529b1bb-4592-4fd1-8f9a-59da9d93ceac)

9. The flag will be displayed inside a Toast message.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/53781b8f-1a04-4252-b581-af42f575ec1d)

10. It can also be obtained from Logcat. Thats it.

![image](https://github.com/rc4ne/Simple-CTF-Writeups/assets/83397936/61162bc3-02a1-41f6-869b-66124cd71a0d)



