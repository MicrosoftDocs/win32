---
title: Output Problems
description: Output Problems
ms.assetid: 45423b7e-f648-408c-9cff-f7cf1affc42a
ms.topic: article
ms.date: 05/31/2018
---

# Output Problems

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

### The character leaves images or trails behind when it moves.

When an Agent character animates, it requires the application windows behind the character to update themselves on a timely basis. When the character moves across the screen, it is normal to sometimes see some residual images that disappear quickly (depending the speed of your PC and the applications you are running). If they don't, the following may be the cause:

-   Your system does not meet the minimum system requirements for Agent.
-   The application window behind the character does not process updates in a timely fashion. Try dragging the character over the desktop or a folder window, or shut down some of your applications. If you see a noticeable improvement, the problem may be unavoidable.
-   You may not have the official release of the Microsoft Internet Explorer 4.0 (or later) installed. Early pre-release versions of Internet Explorer 4.0 did not handle updating the screen correctly. This would result in residual images of the character remaining on the screen. To fix the problem, install the latest official release of the Internet Explorer ([https://www.microsoft.com/windows/ie/](https://www.microsoft.com/windows/internet-explorer/default.aspx)).
-   There may be a problem with your system's screen drivers or hardware. Make certain you have the latest drivers for your graphic hardware. If the problem still persists, you may want to contact your PC vendor.

### The character doesn't produce any audio output when it speaks.

This symptom could have several causes. Try the following to isolate the problem:

-   Verify that your speakers are plugged in and your sound card is compatible with Windows. It is a good idea to test them with another sound application to confirm that audio output is working properly.
-   Verify that the Agent-enabled application or webpage supports speech input. Not all sample pages support speech input. Press and hold the Listening key (typically this will be the Scroll Lock key unless you changed it).A pop-up window should appear under the character. The text in the tip will tell you the listening state of the character. If no tip appears, either the application or webpage does not support speech input or you don't have a compatible speech engine installed. If the tip does appear and indicates the character is listening, Speak one of the character's voice commands. If you do not know what voice commands are available: release the Listening key and right-click the character, then choose Open Voice Commands Window from the pop-up menu. If the command does not appear, speech support is not available for the application or webpage you are using. If it does appear, press and hold the Listening key again. If the Listening tip appears under the character and indicates that the character is listening, speak one of the commands listed in the window. If the character does not respond, go to the next step.
-   Verify that no other application is currently using the audio output device.
-   Verify that the character you are using has been configured for spoken output. (You may need to check with the website or application supplier.)
-   Verify that your Microsoft Agent settings are enabled for spoken output
-   If the character uses a text-to-speech (TTS) engine to produce spoken output, verify that you have installed a compatible TTS engine. For example, when installed as an Internet Explorer 4.0 add-on component, only the core components of Microsoft Agent are installed. The core components do not include a text-to-speech engine. Without this TTS engine (a Microsoft Speech API-compatible engine), Microsoft Agent sample characters will not produce spoken output.
-   Verify that Microsoft Agent's use of MIDI is not blocking the audio channel (see the next topic, Applications that play MIDI have no audio output when Microsoft Agent is running).

### Applications that play MIDI have no audio output when Microsoft Agent is running.

Microsoft Agent uses MIDI to play a tone when you press the Listening key. If you find that this interferes with other applications that play MIDI or interferes with speech input, you can turn off the Play Tone When You Can Speak option in the Microsoft Agent properties.

### I get the following message: An outgoing call cannot be made since the application is dispatching an input-synchronous call.

This message may occur under the following circumstances:

When a webpage including Microsoft Agent is closed (by right-clicking the page's taskbar entry and choosing Close from the pop-up menu), this may occur. This is due to a timing problem between Agent and the browser when they are shutting down at the same time. The error is harmless. Click OK to dismiss the message.

What occurred was the Agent-enabled webpage (or application) attempted to request a specific text-to-speech (TTS) engine. Speechapi.dll was not installed.

### The speech engines don't seem to work with Microsoft Agent in Windows XP?

Microsoft Agent uses SAPI 4.0 to provide speech services. Windows XP however now ships with SAPI 5.0 which does not provide backward compatibility support for its predecessor. Fortunately, SAPI 4.0 and SAPI 5.0 can co-exist together on the same Windows XP computer.

To make the speech engines work with Microsoft Agent in Windows XP, first install the SAPI 4.0 runtime binaries (spchapi.exe), then install the particular speech engines.

### The speech engines used to work with Microsoft Agent until I upgraded to Windows XP. What happened?

See the previous question and answer. The upgrade process of Windows XP may have removed the SAPI 4.0 support already existing on the computer. Just re-install the SAPI 4.0 runtime and SAPI 4.0 speech engines again after the upgrade to Windows XP.

### I installed the TTS3000 text-to-speech engines onto my computer that runs Windows XP (or Windows 2000) and correctly edited my programming accordingly for their use. The Microsoft Agent characters speak audibly using these TTS3000 text-to-speech engines when I or other local Administrators are logged in but not when other users *without Administrator privileges* are logged into this computer. On Windows 98 and Windows Me, these TTS3000 text-to-speech engines work correctly for both sets of users. How can I fix this?

You will need to configure the security permissions for some of the registry keys of the TTS3000 text-to-speech engines to enable their use by user accounts without Administrator privileges. This can be accomplished with the operating system's Registry Editor.

### I followed the procedure described as a solution to the problem stated in the previous question. This worked fine so that the Microsoft Agent characters could speak audibly using these TTS3000 text-to-speech engines when users *without Administrator privileges* were logged into the Windows XP (or Windows 2000) computer. Now, months later, these same TTS3000 text-to-speech engines have stopped working again. What happened?

When you followed the described procedure provided for the previous question, this provided the non-Administrator user accounts with Full Control permissions to the required registry keys. It is possible that one of these users, may have knowingly or unknowingly edited the values, changed the permissions again, or even deleted the registry key entirely.

Check if these registry keys and their permissions have been edited, deleted or otherwise changed since. If necessary, change these registry keys and their permissions back again, or re-install the TTS3000 text-to-speech.

 

 




