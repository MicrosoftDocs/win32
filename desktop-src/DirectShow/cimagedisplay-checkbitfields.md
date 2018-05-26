---
Description: The CheckBitFields method validates the color masks in a VIDEOINFO structure.
ms.assetid: b03455aa-8d90-4fab-999d-7408d8417021
title: CImageDisplay.CheckBitFields method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CImageDisplay.CheckBitFields method

The `CheckBitFields` method validates the color masks in a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure.

## Syntax


```C++
BOOL CheckBitFields(
   const VIDEOINFO *pInput
);
```



## Parameters

<dl> <dt>

*pInput* 
</dt> <dd>

Pointer to a **VIDEOINFO** structure.

</dd> </dl>

## Return value

Returns **TRUE** if the color masks are valid, or **FALSE** otherwise.

## Remarks

This method verifies that the color mask for each color component is between one and eight bits long, and that each color mask is a contiguous sequence of bits. Call this method only when the **biCompression** member is set to BI\_BITFIELDS.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




