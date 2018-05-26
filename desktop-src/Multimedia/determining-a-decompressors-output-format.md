---
title: Determining a Decompressors Output Format
description: Determining a Decompressors Output Format
ms.assetid: afedef5e-a506-40bd-aaad-fd85b0468ed7
keywords:
- video compression manager (VCM),output format
- VCM (video compression manager),output format
- ICDecompressGetFormatSize macro
- ICDecompressQuery macro
- ICDecompressGetPalette macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining a Decompressor's Output Format

The following example determines the buffer size needed for the data specifying the decompression format using the [**ICDecompressGetFormatSize**](/windows/win32/Vfw/nf-vfw-icdecompressgetformatsize?branch=master) macro, allocates a buffer of the appropriate size using the [GlobalAlloc](http://go.microsoft.com/fwlink/p/?linkid=16999) function, and retrieves the decompression format information using the [**ICDecompressGetFormat**](/windows/win32/Vfw/nf-vfw-icdecompressgetformat?branch=master) macro.


```C++
LPBITMAPINFOHEADER lpbiIn, lpbiOut; 
 
// Assume *lpbiIn points to the input (compressed) format. 
dwFormatSize = ICDecompressGetFormatSize(hIC, lpbiIn); 
h = GlobalAlloc(GHND, dwFormatSize); 
lpbiOut = (LPBITMAPINFOHEADER)GlobalLock(h); 
ICDecompressGetFormat(hIC, lpbiIn, lpbiOut); 
 
```



The following example shows how an application can use the [**ICDecompressQuery**](/windows/win32/Vfw/nf-vfw-icdecompressquery?branch=master) macro to determine if a decompressor can handle the input and output formats.


```C++
LPBITMAPINFOHEADER lpbiIn, lpbiOut; 
// Assume *lpbiIn & *lpbiOut are initialized to the respective 
// formats.
 
if (ICDecompressQuery(hIC, lpbiIn, lpbiOut) == ICERR_OK)
{ 
    
    // Format is supported - use the decompressor. 
    
} 
 
```



The following code fragment shows how to get the palette information using the [**ICDecompressGetPalette**](/windows/win32/Vfw/nf-vfw-icdecompressgetpalette?branch=master) macro.


```C++
ICDecompressGetPalette(hIC, lpbiIn, lpbiOut); 
 
// Move up to the palette. 
lpPalette = (LPBYTE)lpbiOut + lpbi->biSize;
 
 
```



 

 




