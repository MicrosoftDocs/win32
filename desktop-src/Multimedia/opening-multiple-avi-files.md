---
title: Opening Multiple AVI Files
description: Opening Multiple AVI Files
ms.assetid: 982bcea1-77b0-4a38-893d-1f506ffb18f5
keywords:
- initAVI function
- termAVI function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Opening Multiple AVI Files

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If your application opens multiple files, it should include routines such as the following simple functions. The application would use the "initAVI" function during its initialization and the "termAVI" function during its termination. These functions simply wrap the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function.


```C++
// Initialize the MCIAVI driver. This returns TRUE if OK, 
// FALSE on error. 
 
BOOL initAVI(VOID) 
{ 
    // Perform additional initialization before loading first file. 
    return mciSendString("open digitalvideo", NULL, 0, NULL) == 0; 
} 
 
// Close the MCIAVI driver. 
void termAVI(VOID) 
{ 
    mciSendString("close digitalvideo", NULL, 0, NULL); 
} 
```



 

 