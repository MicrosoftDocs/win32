---
title: Command Messages
description: Command Messages
ms.assetid: 29b40f35-d390-49c3-99bd-c648c7c50504
keywords:
- MCI command messages,about
- MCI command messages,syntax
- mciSendCommand function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Command Messages

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The command-message interface is designed to be used by applications requiring a C-language interface to control multimedia devices. It uses a message-passing paradigm to communicate with MCI devices. You can send a command by using the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function.

The **mciSendCommand** function returns zero if successful. If the function fails, the low-order word of the return value contains an error code. You can pass this error code to the [**mciGetErrorString**](/previous-versions//dd757158(v=vs.85)) function to get a text description of the error.

## Syntax of Command Messages

MCI command messages consist of the following elements:

-   A constant message value
-   A structure containing parameters for the command
-   A set of flags specifying options for the command and validating fields in the parameter block

The following example uses the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to send the [**MCI\_ PLAY**](mci-play.md) command to the device identified by a device identifier.


```C++
mciSendCommand(wDeviceID,            // device identifier 
    MCI_PLAY,                        // command message 
    0,                               // flags 
    (DWORD)(LPVOID) &mciPlayParms);  // parameter block 
```



The device identifier given in the first parameter is retrieved when the device is opened using the [**MCI\_ OPEN**](mci-open.md) command. The last parameter is the address of an [**MCI\_ PLAY\_ PARMS**](mci-play-parms.md) structure, which might contain information about where to begin and end playback. Many MCI command messages use a structure to contain parameters of this kind. The first member of each of these structures identifies the window that receives an [**MM\_ MCINOTIFY**](mm-mcinotify.md) message when the operation finishes.

 

 