---
description: The UninitialiseWindow method releases the window's resources.
ms.assetid: 8c5bb0c1-1d92-4025-bbbd-1e57ddde4456
title: CBaseWindow.UninitialiseWindow method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.UninitialiseWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.UninitialiseWindow method

The `UninitialiseWindow` method releases the window's resources.

## Syntax


```C++
virtual HRESULT UninitialiseWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method frees resources that were acquired by the [**CBaseWindow::InitialiseWindow**](cbasewindow-initialisewindow.md) method. The [**CBaseWindow::DoneWithWindow**](cbasewindow-donewithwindow.md) method calls this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




