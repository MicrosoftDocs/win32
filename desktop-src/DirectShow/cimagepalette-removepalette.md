---
description: The RemovePalette method deletes the existing logical palette and calls CBaseWindow::UnsetPalette on the CBaseWindow object.
ms.assetid: fab531b8-8630-43f8-bf08-cd8f24659bef
title: CImagePalette.RemovePalette method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImagePalette.RemovePalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImagePalette.RemovePalette method

The `RemovePalette` method deletes the existing logical palette and calls [**CBaseWindow::UnsetPalette**](cbasewindow-unsetpalette.md) on the **CBaseWindow** object.

## Syntax


```C++
HRESULT RemovePalette();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




