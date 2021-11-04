---
description: The GetColourMask method retrieves the color masks for the current display format.
ms.assetid: 386d0439-8502-411d-935c-3c2153a8b5b4
title: CImageDisplay.GetColourMask method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay.GetColourMask
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageDisplay.GetColourMask method

The `GetColourMask` method retrieves the color masks for the current display format.

## Syntax


```C++
BOOL GetColourMask(
   DWORD *pMaskRed,
   DWORD *pMaskGreen,
   DWORD *pMaskBlue
);
```



## Parameters

<dl> <dt>

*pMaskRed* 
</dt> <dd>

Pointer to a variable that receives the red-component mask.

</dd> <dt>

*pMaskGreen* 
</dt> <dd>

Pointer to a variable that receives the green-component mask.

</dd> <dt>

*pMaskBlue* 
</dt> <dd>

Pointer to a variable that receives the blue-component mask.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




