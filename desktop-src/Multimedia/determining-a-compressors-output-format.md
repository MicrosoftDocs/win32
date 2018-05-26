---
title: Determining a Compressors Output Format
description: Determining a Compressors Output Format
ms.assetid: 910bd77f-4c65-4ea2-bab2-96f42a2b6cf1
keywords:
- video compression manager (VCM),output format
- VCM (video compression manager),output format
- ICCompressGetFormat macro
- ICCompressQuery macro
- ICCompressGetSize macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining a Compressor's Output Format

The following example uses the [**ICCompressGetFormat**](/windows/win32/Vfw/nf-vfw-iccompressgetformat?branch=master) size macro to determine the buffer size needed for the data specifying the compression format, allocates a buffer of the appropriate size using the [GlobalAlloc](http://go.microsoft.com/fwlink/p/?linkid=16999) function, and retrieves the compression format information using the **ICCompressGetFormat** macro.


```C++
LPBITMAPINFOHEADER   lpbiIn, lpbiOut; 
 
// *lpbiIn must be initialized to the input format. 
 
dwFormatSize = ICCompressGetFormatSize(hIC, lpbiIn); 
h = GlobalAlloc(GHND, dwFormatSize); 
lpbiOut = (LPBITMAPINFOHEADER)GlobalLock(h); 
ICCompressGetFormat(hIC, lpbiIn, lpbiOut); 
 
```



The following example uses the [**ICCompressQuery**](/windows/win32/Vfw/nf-vfw-iccompressquery?branch=master) macro to determine whether a compressor can handle the input and output formats.


```C++
LPBITMAPINFOHEADER   lpbiIn, lpbiOut; 
 
// Both *lpbiIn and *lpbiOut must be initialized to the respective
// formats.
 

if (ICCompressQuery(hIC, lpbiIn, lpbiOut) == ICERR_OK)
{ 
 
    // Format is supported; use the compressor. 
 
}
 
 
```



The following example uses the [**ICCompressGetSize**](/windows/win32/Vfw/nf-vfw-iccompressgetsize?branch=master) macro to determine the buffer size, and it allocates a buffer of that size using [GlobalAlloc](http://go.microsoft.com/fwlink/p/?linkid=16999).


```C++
// Find the worst-case buffer size. 
dwCompressBufferSize = ICCompressGetSize(hIC, lpbiIn, lpbiOut); 
 
// Allocate a buffer and get lpOutput to point to it. 
h = GlobalAlloc(GHND, dwCompressBufferSize); 
lpOutput = (LPVOID)GlobalLock(h);
 
 
```



 

 




