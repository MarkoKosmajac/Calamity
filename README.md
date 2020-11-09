<p align="center"><img src="https://github.com/MarkoKosmajac/Calamity/blob/main/images/calamity.gif" alt="Calamity" width="350" height="80" style="border-radius: 2px;"></p>

<p align="center">
<a href="#"><img src="https://img.shields.io/badge/Python-blue?label=Made%20With&style=flat-square%22%20alt=%22C#%20Language"></a> ||
<a href="#"><img src="https://img.shields.io/badge/License-MIT-brightgreen?&style=flat-square" alt="License"></a>
</p>
<br>

<table border="0" cellpadding="2" cellspacing="2" width="100%">
  <tr>
    <td align="center"><img title="Legal desclaimer" src="https://imgur.com/7OzJEBI.png"></td>
     <td align="center"> <b><a href="https://github.com/MarkoKosmajac/">Marko Kosmajac</a> is not responsible for any misuse, damage caused by this script or attacking targets without prior mutual consent! It is your responsibility to obey laws!</b>
    </td>
  </tr>
</table>

# DISCLAIMER
**Calamity is for education/research purposes only. The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided.
 The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of ANY files provided with Calamity.
 By using Calamity or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again Calamity and ALL files included are for EDUCATION and/or RESEARCH purposes ONLY.
 Calamity is ONLY intended to be used on your own pentesting labs, or with explicit consent from the owner of the property being tested.** 


# About Calamity
Calamity is a Remote Administration Tool (RAT) written in Python using HTTP as a C&amp;C

# Instructions
Run the flask server on your machine.
<br>
Calamity is a facebook clone, working with some fake approutes.
 - <img src="https://img.shields.io/badge/POST-/facebook-lightblue?&style=flat-square" alt="Method Post"> Saves all output from the client to a file on your server
 - <img src="https://img.shields.io/badge/GET-/facebookfriends-red?&style=flat-square" alt="Method Get"> Displays the current statuscode/command variable
 - <img src="https://img.shields.io/badge/GET-/changeFacebookFriends-red?&style=flat-square" alt="Method Get"> Renders form to change statuscode/command variable
 - <img src="https://img.shields.io/badge/POST-/FacebookAddStatusFriend-lightblue?&style=flat-square" alt="Method Post"> Post to change to statuscode/command variable
 - <img src="https://img.shields.io/badge/POST-/FacebookAddStatus-lightblue?&style=flat-square" alt="Method Post"> Post to change to statuscode/command variable
<br>
Instructions to run on the client should be placed in update.py at the bottom:
 - Some basic instructions were added as a default e.g: dir, whoami, ipconfig, ...
 - Statuscode 98 means 'Do Nothing & Wait for a change'
 - Statuscode 99 means 'Post Data to server'
 - !!! Do not change these 2 statuscodes unless you know what you are doing !!!

# Features
You are free to add any feature you want to this remote administration tool.
<br>
I have added 3 default ones:
 - Collect Google Chrome Passwords
 - Collect all WiFi Passwords
 - Collect public IP

## License

See [LICENSE](/LICENSE)
