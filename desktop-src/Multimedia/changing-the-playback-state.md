---
title: Changing the Playback State
description: Changing the Playback State
ms.assetid: 69ede616-aea4-4b7c-a12b-014ac0485b1c
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Changing the Playback State

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following examples show how to use the [**pause**](pause.md), [**resume**](resume.md), [**stop**](stop.md), and [**seek**](seek.md) commands in the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function.


```C++
// Assume the file was opened with the alias 'movie'. 
 
// Pause play. 
mciSendString("pause movie", NULL, 0, NULL); 
 
// Resume play. 
mciSendString("resume movie", NULL, 0, NULL); 
 
// Stop play. 
mciSendString("stop movie", NULL, 0, NULL); 
 
// Seek to the beginning. 
mciSendString("seek movie to start", NULL, 0, NULL); 
 
```



The following example shows how to change the seek mode:


```C++
// Set seek mode with the string interface. 
// Assume the file was opened with the alias 'movie'. 
 
void SetSeekMode(BOOL fExact) 
{ 
    if (fExact) 
        mciSendString("set movie seek exactly on", NULL, 0, NULL); 
    else 
        mciSendString("set movie seek exactly off", NULL, 0, NULL); 
} 
```



 

 