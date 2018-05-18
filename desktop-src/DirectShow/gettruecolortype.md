---
Description: 'The GetTrueColorType function retrieves the human-readable name of a video subtype.'
ms.assetid: '479a020c-b55c-44ec-9096-5528113a4b74'
title: GetTrueColorType function
---

# GetTrueColorType function

The **GetTrueColorType** function retrieves the human-readable name of a video subtype.

## Syntax


```C++
const GUID GetTrueColorType(
   const BITMAPINFOHEADER *pHeader
);
```



## Parameters

<dl> <dt>

*pHeader* 
</dt> <dd>

Pointer to a [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure that defines the bitmap.

</dd> </dl>

## Return value

Returns MEDIASUBTYPE\_RGB555 or MEDIASUBTYPE\_RGB565.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




