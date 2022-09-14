---
description: The ShouldUpdate method determines whether it is necessary to create a new palette.
ms.assetid: 50886277-189b-4102-ade9-0366f64fdbcb
title: CImagePalette.ShouldUpdate method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImagePalette.ShouldUpdate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImagePalette.ShouldUpdate method

The `ShouldUpdate` method determines whether it is necessary to create a new palette.

## Syntax


```C++
BOOL ShouldUpdate(
   const VIDEOINFOHEADER *pNewInfo,
   const VIDEOINFOHEADER *pOldInfo
);
```



## Parameters

<dl> <dt>

*pNewInfo* 
</dt> <dd>

Pointer to a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure containing the new color table.

</dd> <dt>

*pOldInfo* 
</dt> <dd>

Pointer to a **VIDEOINFOHEADER** structure containing the old color table. This parameter can be **NULL**.

</dd> </dl>

## Return value

Returns **TRUE** if the palette needs to be updated, or **FALSE** otherwise.

## Remarks

-   If neither **VIDEOINFOHEADER** structure contains a color table, the method returns **FALSE**.
-   If only one structure contains a color table, or if *pOldInfo* is **NULL**, the method returns **TRUE**.
-   If both structures contain color tables, and the color entries match, the method returns **FALSE**.
-   If both structures contain color tables, but the color entries do not match, the method returns **TRUE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




