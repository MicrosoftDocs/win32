---
Description: The GetBitmapSize function calculates the number of bytes required by a device-independent bitmap (DIB). This function simply calls the DIBSIZE macro.
ms.assetid: ce23cdf2-9804-4d2e-b9ef-16e54b2d571e
title: GetBitmapSize function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetBitmapSize function

The `GetBitmapSize` function calculates the number of bytes required by a device-independent bitmap (DIB). This function simply calls the [**DIBSIZE**](/windows/desktop/api/Amvideo/nf-amvideo-dibsize) macro.

## Syntax


```C++
DWORD GetBitmapSize(
   const BITMAPINFOHEADER *pHeader
);
```



## Parameters

<dl> <dt>

*pHeader* 
</dt> <dd>

Pointer to a [**BITMAPINFOHEADER**](/windows/desktop/api/WinGDI/ns-wingdi-tagbitmapinfoheader) structure.

</dd> </dl>

## Return value

Returns the size in bytes.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




