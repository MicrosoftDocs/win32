---
title: Naming the Capture File
description: Naming the Capture File
ms.assetid: 'fae2fd6a-4c2f-432f-a714-9faae6daeafe'
keywords: ["capFileSetCaptureFile macro", "capFileAlloc macro"]
---

# Naming the Capture File

The following example uses the [**capFileSetCaptureFile**](capfilesetcapturefile.md) macro to specify an alternate filename (MYCAP.AVI) for the capture file and the [**capFileAlloc**](capfilealloc.md) macro to preallocate a file of 5 MB.


```C++
char szCaptureFile[] = "MYCAP.AVI";

capFileSetCaptureFile( hWndC, szCaptureFile); 
capFileAlloc( hWndC, (1024L * 1024L * 5)); 
 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




