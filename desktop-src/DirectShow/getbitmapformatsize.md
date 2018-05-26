---
Description: The GetBitmapFormatSize function calculates the size needed for a VIDEOINFO structure that can hold a specified BITMAPINFOHEADER structure.
ms.assetid: a559415a-070f-4674-be12-a65a46025809
title: GetBitmapFormatSize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetBitmapFormatSize function

The `GetBitmapFormatSize` function calculates the size needed for a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure that can hold a specified [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) structure.

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

Pointer to a [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) structure.

</dd> </dl>

## Return value

Returns the size, in bytes.

## Remarks

A [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) structure might be followed by color masks or palette entries, so it can be difficult to determine the number of bytes required to construct a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure from an existing **BITMAPINFOHEADER** structure.

To copy a [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) structure into a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure, use the [**HEADER**](/windows/win32/Amvideo/nf-amvideo-header?branch=master) macro, which calculates the correct offset.

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

 

 




