---
title: Reading Streams from an AVI File
description: Reading Streams from an AVI File
ms.assetid: fa17cac4-bc6f-48ef-8960-286386b43c82
keywords:
- AVIStreamInfo function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reading Streams from an AVI File

The following subroutine obtains stream information from an AVI file and determines the stream type from the [**AVISTREAMINFO**](/windows/win32/Vfw/ns-vfw-_avistreaminfoa?branch=master) structure returned by the [**AVIStreamInfo**](/windows/win32/Vfw/nf-vfw-avistreaminfoa?branch=master) function.


```C++
// StreamTypes - opens the streams in an AVI file and determines 
// stream types. 
// 
// Global variables 
// gcpavi - count of streams in an AVI file 
// gapavi[] = array of stream-interface pointers 
 
void StreamTypes(HWND hwnd) 
{ 
    AVISTREAMINFO     avis; 
    LONG    r, lHeight = 0; 
    WORD    w; 
    int     i; 
    RECT    rc; 
 
// Walk through all streams. 
    for (i = 0; i < gcpavi; i++) { 
        AVIStreamInfo(gapavi[i], &amp;avis, sizeof(avis)); 
 
        if (avis.fccType == streamtypeVIDEO) { 
 
        // Place video-processing functions here. 
 
        } 
        else if (avis.fccType == streamtypeAUDIO) { 
 
        // Place audio-processing functions here. 
 
        } 
        else if (avis.fccType == streamtypeTEXT) { 
 
        // Place text-processing functions here. 
 
        } 
    } 
} 
 
```



 

 




