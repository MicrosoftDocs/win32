---
title: Opening an AVI File
description: Opening an AVI File
ms.assetid: 322eb45f-7dd3-40f4-b6bf-381021c50397
keywords:
- AVIFileInit function
- AVIFileOpen function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Opening an AVI File

The following example initializes the AVIFile library using the [**AVIFileInit**](/windows/win32/Vfw/nf-vfw-avifileinit?branch=master) function and opens an AVI file using the [**AVIFileOpen**](/windows/win32/Vfw/nf-vfw-avifileopen?branch=master) function. The function uses a default file handler.


```C++
// LoadAVIFile - loads AVIFile and opens an AVI file. 
// 
// szfile - filename 
// hwnd - window handle 
// 
VOID LoadAVIFile(LPCSTR szFile, HWND hwnd) 
{ 
    LONG hr; 
    PAVIFILE pfile; 
 
    AVIFileInit();          // opens AVIFile library 
 
    hr = AVIFileOpen(&amp;pfile, szFile, OF_SHARE_DENY_WRITE, 0L); 
    if (hr != 0){ 
        // Handle failure.
        return; 
    } 
 
// 
// Place functions here that interact with the open file. 
// 
 
    AVIFileRelease(pfile);  // closes the file 
    AVIFileExit();          // releases AVIFile library 
} 
 
```



 

 




