---
title: Speech Input Problems
description: Speech Input Problems
ms.assetid: b42664a2-9615-4e15-97a6-115e9556096b
ms.topic: article
ms.date: 05/31/2018
---

# Speech Input Problems

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

### The character does not respond to my spoken input.

This symptom may be caused by a number of problems. Try the following to isolate the problem:

-   Verify that your microphone is correctly plugged in. It is a good idea to test it with another sound input application to ensure that it works properly.
-   Verify that a compatible speech engine is installed. Under Windows 95, Windows 98, and Windows NT 4.0, open the Control Panel. If you find the Speech object there, open it, and it will list the speech engines available and installed on your system.
-   Verify that your sound card is compatible with Microsoft Windows 95, Windows 98, or Windows NT.

    The best way to do this is to run the Sound Recorder application that comes with Windows. It can usually be found on the Start menu. Click the Start button, click Programs, click Accessories, click Multimedia, and then click Sound Recorder. When the Sound Recorder window displays, click the **Record** button and talk into your microphone. The line in the window should animate in response to your voice input.

    If the Sound Recorder application doesn't work on your system, contact the sound card manufacturer's technical support department for assistance. Your sound card may not be compatible with Windows or there may be a problem with the software drivers for your sound card.

-   Verify that your sound input for speech input is set properly.
    1.  Open the Speech input object in the Control Panel. If the Speech object is not present, install one.
    2.  Select the speech input engine you have installed.
    3.  Choose the Microphone Settings Wizard button. If this button appears disabled, a compatible speech engine is not installed or the speech engine you installed may not support automatic adjustment.
-   Verify that the Agent-enabled application or webpage supports speech input. Not all pages (or applications) support speech input. Press and hold the Listening key. Typically this will be the Scroll Lock key unless you changed it. A pop-up window should appear under the character. The text in the tip will tell you the listening state of the character. If no tip appears, either the application or webpage does not support speech input, or you don't have a compatible speech engine installed. If the tip does appear and indicates the character is listening, speak one of the character's voice commands. If you do not know what voice commands are available, release the Listening key and right-click the character. Then, choose Open Voice Commands Window from the pop-up menu. If the command does not appear, speech support is not available for the application or webpage you are using. If it does appear, press and hold the Listening key again. If the Listening tip appears under the character and indicates that the character is listening, speak one of the commands listed in the window. If the character does not respond, go to the next step.
-   Verify that no other application is currently using the audio output device.
-   Verify that Microsoft Agent's use of MIDI is not blocking the audio channel (see [Applications that play MIDI have no audio output when Microsoft Agent is running](output-problems.md)" in the Output Problems section).
-   If you followed the steps above but still have problems with speech input, verify that your sound card and driver software is compatible with the speech engine you are using. Check with the technical support for your sound card and your speech engine manufacturer.

### The MIDI tone seems to disrupts speech input.

Reduce the MIDI volume using the following steps.

1.  Open the Volume Control window by right-clicking the speaker icon in the taskbar or by opening the Multimedia object in the Control Panel. Click the Volume button in the Playback section of the Audio page.
2.  Decrease the MIDI volume by moving slider down.

### The character does not respond to voice input, but I can hear my voice through my speakers when I talk into my microphone.

Your sound card is not set up properly for use with Microsoft Agent. Choose the Microphone Settings Wizard on the property sheet of the Speech object in the Control Panel. See the steps for "[The character does not respond to my spoken input](#the-character-does-not-respond-to-my-spoken-input)" for information on how to access this button.

 

 




