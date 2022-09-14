---
description: The OnSize method handles WM\_SIZE messages.
ms.assetid: 21d867a4-4321-478a-9beb-5d3053569369
title: CBaseWindow.OnSize method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.OnSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.OnSize method

The `OnSize` method handles WM\_SIZE messages.

## Syntax


```C++
virtual BOOL OnSize(
   LONG Width,
   LONG Height
);
```



## Parameters

<dl> <dt>

*Width* 
</dt> <dd>

Width of the client area, in pixels.

</dd> <dt>

*Height* 
</dt> <dd>

Height of the client area, in pixels.

</dd> </dl>

## Return value

Returns **TRUE**.

## Remarks

This method stores the new width and height. To retrieve these values, call the [**CBaseWindow::GetWindowHeight**](cbasewindow-getwindowheight.md) and [**CBaseWindow::GetWindowWidth**](cbasewindow-getwindowwidth.md) methods.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




