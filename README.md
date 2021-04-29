# ArkoseBuster
<h3>Arkose Labs captcha solver written in Python using Selenium and using IBM Watson STT AI</h3><br>
Useful for any kinds of browser automation/botting that needs to get past a sneaky captcha. Ironic how a bot is able to crack Arkose Labs captchas, but for a human it's impossible. A real staple in shitty design.<br>
Use with caution, there's some tinkering for you ahead. A lot of sites use agressive captcha mode and if you don't use selenium-stealth and emulate user behavior, you're gonna get the audio captcha disabled and it's game over. This tool isn't made with this really in mind cause that's too much work. Good luck<br>
<i>This is not a standalone tool. You can run it to demonstrate how it works, but the purpose of this tool is for it to be integrated in other peoples' projects</i>

# What you need
```
IBM Watson API key - IBM offers a Lite plan for free offering 500 minutes of speech recognition per month, which is probably more than you could ever use
Selenium
ibm_watson pip package
requests pip package
```
# How to use
Integrate it with your tool, it's not really useful on its own

<h3>This tool is really extremely simple compared to other ones I've seen on GitHub. If you want to use it in your project, you're free to do so, and instructions are in the comments in main.py</h3>
