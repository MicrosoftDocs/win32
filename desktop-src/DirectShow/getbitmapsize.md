---
Description: 'The GetBitmapSize function calculates the number of bytes required by a device-independent bitmap (DIB). This function simply calls the DIBSIZE macro.'
ms.assetid: 'ce23cdf2-9804-4d2e-b9ef-16e54b2d571e'
title: GetBitmapSize function
---

# GetBitmapSize function

The `GetBitmapSize` function calculates the number of bytes required by a device-independent bitmap (DIB). This function simply calls the [**DIBSIZE**](dibsize.md) macro.

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

Pointer to a [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure.

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

 

 




