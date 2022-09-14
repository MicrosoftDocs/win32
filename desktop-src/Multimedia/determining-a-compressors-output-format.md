---
title: Determining a Compressor's Output Format
description: Determining a Compressor's Output Format
ms.assetid: 910bd77f-4c65-4ea2-bab2-96f42a2b6cf1
keywords:
- video compression manager (VCM),output format
- VCM (video compression manager),output format
- ICCompressGetFormat macro
- ICCompressQuery macro
- ICCompressGetSize macro
ms.topic: article
ms.date: 05/31/2018
---

# Determining a Compressor's Output Format

The following example uses the [**ICCompressGetFormat**](/windows/desktop/api/Vfw/nf-vfw-iccompressgetformat) size macro to determine the buffer size needed for the data specifying the compression format, allocates a buffer of the appropriate size using the [GlobalAlloc](/windows/win32/api/winbase/nf-winbase-globalalloc) function, and retrieves the compression format information using the **ICCompressGetFormat** macro.


```C++
LPBITMAPINFOHEADER   lpbiIn, lpbiOut; 
 
// *lpbiIn must be initialized to the input format. 
 
dwFormatSize = ICCompressGetFormatSize(hIC, lpbiIn); 
h = GlobalAlloc(GHND, dwFormatSize); 
lpbiOut = (LPBITMAPINFOHEADER)GlobalLock(h); 
ICCompressGetFormat(hIC, lpbiIn, lpbiOut); 
 
```



The following example uses the [**ICCompressQuery**](/windows/desktop/api/Vfw/nf-vfw-iccompressquery) macro to determine whether a compressor can handle the input and output formats.


```C++
LPBITMAPINFOHEADER   lpbiIn, lpbiOut; 
 
// Both *lpbiIn and *lpbiOut must be initialized to the respective
// formats.
 

if (ICCompressQuery(hIC, lpbiIn, lpbiOut) == ICERR_OK)
{ 
 
    // Format is supported; use the compressor. 
 
}
 
 
```



The following example uses the [**ICCompressGetSize**](/windows/desktop/api/Vfw/nf-vfw-iccompressgetsize) macro to determine the buffer size, and it allocates a buffer of that size using [GlobalAlloc](/windows/win32/api/winbase/nf-winbase-globalalloc).


```C++
// Find the worst-case buffer size. 
dwCompressBufferSize = ICCompressGetSize(hIC, lpbiIn, lpbiOut); 
 
// Allocate a buffer and get lpOutput to point to it. 
h = GlobalAlloc(GHND, dwCompressBufferSize); 
lpOutput = (LPVOID)GlobalLock(h);
 
 
```



 

 