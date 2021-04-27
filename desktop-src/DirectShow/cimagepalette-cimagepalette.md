---
description: CImagePalette.CImagePalette constructor - Constructor method.
ms.assetid: 50fa573c-a244-4a1e-9fd9-2b33a3427c84
title: CImagePalette.CImagePalette constructor (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImagePalette.CImagePalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImagePalette.CImagePalette constructor

Constructor method.

## Syntax


```C++
CImagePalette(
   CBaseFilter *pBaseFilter,
   CBaseWindow *pBaseWindow,
   CDrawImage  *pDrawImage
);
```



## Parameters

<dl> <dt>

*pBaseFilter* 
</dt> <dd>

Pointer to owning filter.

</dd> <dt>

*pBaseWindow* 
</dt> <dd>

Pointer to a **CBaseWindow** object, which manages the window where the palette is realized. This parameter can be **NULL**.

</dd> <dt>

*pDrawImage* 
</dt> <dd>

Pointer to a **CDrawImage** object, which draws the video image. This parameter can be **NULL**.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




