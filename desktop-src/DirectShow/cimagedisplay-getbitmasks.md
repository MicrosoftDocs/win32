---
description: The GetBitMasks method retrieves the color masks for a specified VIDEOINFO format.
ms.assetid: 72a9ba44-96de-4fff-a3fb-675d3dd080d8
title: CImageDisplay.GetBitMasks method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay.GetBitMasks
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageDisplay.GetBitMasks method

The `GetBitMasks` method retrieves the color masks for a specified [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) format.

## Syntax


```C++
const DWORD* GetBitMasks(
   const VIDEOINFO *pVideoInfo
);
```



## Parameters

<dl> <dt>

*pVideoInfo* 
</dt> <dd>

Pointer to the **VIDEOINFO** structure.

</dd> </dl>

## Return value

Returns an array of three **DWORD** values.

## Remarks

If the **biCompression** member is BI\_BITFIELDS, the method returns a pointer to the color masks that are supplied in the **dwBitMasks** member. If the **biCompression** member is BI\_RGB, the method returns the color masks that correspond to the bit depth. If the method fails (for example, the bit depth is less than 16), the method returns the array {0,0,0}.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




