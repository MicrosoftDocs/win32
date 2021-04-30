---
description: The OnClose method handles WM\_CLOSE messages.
ms.assetid: e562add4-752e-4665-a75e-a5526fb7f045
title: CBaseWindow.OnClose method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.OnClose
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.OnClose method

The `OnClose` method handles WM\_CLOSE messages.

## Syntax


```C++
virtual BOOL OnClose();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE**.

## Remarks

In the base class, this method simply hides the window. Typically, a derived class will override this method so that it sends an [**EC\_USERABORT**](ec-userabort.md) event as well. Do not override the method to destroy the window. Instead, call the [**CBaseWindow::DoneWithWindow**](cbasewindow-donewithwindow.md) method when the owning filter is destroyed.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




