---
Description: The RemovePalette method deletes the existing logical palette and calls CBaseWindowUnsetPalette on the CBaseWindow object.
ms.assetid: fab531b8-8630-43f8-bf08-cd8f24659bef
title: CImagePalette.RemovePalette method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




