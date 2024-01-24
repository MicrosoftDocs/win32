---
title: Using the MCI_NOTIFY Flag
description: Using the MCI\_NOTIFY Flag
ms.assetid: 1d1803c8-f315-463e-ae0d-a258aa3af3c9
keywords:
- MCI_NOTIFY flag
- MCI_PLAY command
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the MCI\_NOTIFY Flag

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example shows how the MCI\_NOTIFY flag is used with the [**MCI\_PLAY**](mci-play.md) command. The handle to the window procedure that will process the [**MM\_MCINOTIFY**](mm-mcinotify.md) message is specified in *hwnd*.


```C++
MCI_DGV_PLAY_PARMS mciPlay; 
DWORD dwFlags; 
 
mciPlay.dwCallback = MAKELONG(hwnd, 0); 
dwFlags = MCI_NOTIFY; 
 
mciSendCommand(wMCIDeviceID, MCI_PLAY, dwFlags, (DWORD)(LPSTR)&mciPlay); 
```



 

 




