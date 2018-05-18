---
Description: 'The GetBitmapFormatSize function calculates the size needed for a VIDEOINFO structure that can hold a specified BITMAPINFOHEADER structure.'
ms.assetid: 'a559415a-070f-4674-be12-a65a46025809'
title: GetBitmapFormatSize function
---

# GetBitmapFormatSize function

The `GetBitmapFormatSize` function calculates the size needed for a [**VIDEOINFO**](videoinfo.md) structure that can hold a specified [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure.

## Syntax


```C++
LONG GetBitmapFormatSize(
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

Returns the size, in bytes.

## Remarks

A [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure might be followed by color masks or palette entries, so it can be difficult to determine the number of bytes required to construct a [**VIDEOINFO**](videoinfo.md) structure from an existing **BITMAPINFOHEADER** structure.

To copy a [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure into a [**VIDEOINFO**](videoinfo.md) structure, use the [**HEADER**](header.md) macro, which calculates the correct offset.

## Examples


```
LONG size = GetBitmapFormatSize(&amp;bmi);

VIDEOINFO *pVi = static_cast<VIDEOINFO*>(CoTaskMemAlloc(size));

if (pVi != NULL)
{
    CopyMemory(HEADER(pVi), &amp;bmi, sizeof(BITMAPINFOHEADER));
}
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




