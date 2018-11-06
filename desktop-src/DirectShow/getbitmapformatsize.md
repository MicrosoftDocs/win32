---
Description: The GetBitmapFormatSize function calculates the size needed for a VIDEOINFO structure that can hold a specified BITMAPINFOHEADER structure.
ms.assetid: a559415a-070f-4674-be12-a65a46025809
title: GetBitmapFormatSize function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetBitmapFormatSize
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# GetBitmapFormatSize function

The `GetBitmapFormatSize` function calculates the size needed for a [**VIDEOINFO**](/windows/desktop/api/amvideo/ns-amvideo-tagvideoinfo) structure that can hold a specified [**BITMAPINFOHEADER**](/windows/desktop/api/WinGDI/ns-wingdi-tagbitmapinfoheader) structure.

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

Pointer to a [**BITMAPINFOHEADER**](/windows/desktop/api/WinGDI/ns-wingdi-tagbitmapinfoheader) structure.

</dd> </dl>

## Return value

Returns the size, in bytes.

## Remarks

A [**BITMAPINFOHEADER**](/windows/desktop/api/WinGDI/ns-wingdi-tagbitmapinfoheader) structure might be followed by color masks or palette entries, so it can be difficult to determine the number of bytes required to construct a [**VIDEOINFO**](/windows/desktop/api/amvideo/ns-amvideo-tagvideoinfo) structure from an existing **BITMAPINFOHEADER** structure.

To copy a [**BITMAPINFOHEADER**](/windows/desktop/api/WinGDI/ns-wingdi-tagbitmapinfoheader) structure into a [**VIDEOINFO**](/windows/desktop/api/amvideo/ns-amvideo-tagvideoinfo) structure, use the [**HEADER**](/windows/desktop/api/Amvideo/nf-amvideo-header) macro, which calculates the correct offset.

## Examples


```
LONG size = GetBitmapFormatSize(&bmi);

VIDEOINFO *pVi = static_cast<VIDEOINFO*>(CoTaskMemAlloc(size));

if (pVi != NULL)
{
    CopyMemory(HEADER(pVi), &bmi, sizeof(BITMAPINFOHEADER));
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

 

 




