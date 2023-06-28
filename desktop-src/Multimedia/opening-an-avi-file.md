---
title: Opening an AVI File
description: Opening an AVI File
ms.assetid: 322eb45f-7dd3-40f4-b6bf-381021c50397
keywords:
- AVIFileInit function
- AVIFileOpen function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Opening an AVI File

\[The feature associated with this page, [AVIFile Functions and Macros](/windows/win32/multimedia/avifile-functions-and-macros), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **AVIFile Functions and Macros**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example initializes the AVIFile library using the [**AVIFileInit**](/windows/desktop/api/Vfw/nf-vfw-avifileinit) function and opens an AVI file using the [**AVIFileOpen**](/windows/desktop/api/Vfw/nf-vfw-avifileopen) function. The function uses a default file handler.


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
 
    hr = AVIFileOpen(&pfile, szFile, OF_SHARE_DENY_WRITE, 0L); 
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



 

 




