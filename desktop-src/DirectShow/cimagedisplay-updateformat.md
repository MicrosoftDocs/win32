---
Description: The UpdateFormat method fills in some optional members of the VIDEOINFO structure.
ms.assetid: 5ca34fa0-eef4-44f5-bbcc-e686e5181d86
title: CImageDisplay.UpdateFormat method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CImageDisplay.UpdateFormat method

The `UpdateFormat` method fills in some optional members of the [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure.

## Syntax


```C++
HRESULT UpdateFormat(
   VIDEOINFO *pVideoInfo
);
```



## Parameters

<dl> <dt>

*pVideoInfo* 
</dt> <dd>

Pointer to a **VIDEOINFO** structure.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method sets the **biClrUsed**, **biClrImportant**, and **biSizeImage** members to the correct values, and clears the source and target rectangles.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




