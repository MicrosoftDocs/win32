---
title: Opening Multiple AVI Files
description: Opening Multiple AVI Files
ms.assetid: 982bcea1-77b0-4a38-893d-1f506ffb18f5
keywords:
- initAVI function
- termAVI function
ms.topic: article
ms.date: 05/31/2018
---

# Opening Multiple AVI Files

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



 

 