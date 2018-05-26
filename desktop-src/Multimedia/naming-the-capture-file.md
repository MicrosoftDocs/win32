---
title: Naming the Capture File
description: Naming the Capture File
ms.assetid: fae2fd6a-4c2f-432f-a714-9faae6daeafe
keywords:
- capFileSetCaptureFile macro
- capFileAlloc macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Naming the Capture File

The following example uses the [**capFileSetCaptureFile**](/windows/win32/Vfw/nf-vfw-capfilesetcapturefile?branch=master) macro to specify an alternate filename (MYCAP.AVI) for the capture file and the [**capFileAlloc**](/windows/win32/Vfw/nf-vfw-capfilealloc?branch=master) macro to preallocate a file of 5 MB.


```C++
char szCaptureFile[] = "MYCAP.AVI";

capFileSetCaptureFile( hWndC, szCaptureFile); 
capFileAlloc( hWndC, (1024L * 1024L * 5)); 
 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




