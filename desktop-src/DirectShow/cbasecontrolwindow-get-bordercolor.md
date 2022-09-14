---
description: The get\_BorderColor method retrieves the current border color.
ms.assetid: 4b4cae1d-bef7-4f8d-8011-c220fcfb73eb
title: CBaseControlWindow.get_BorderColor method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_BorderColor
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_BorderColor method

The `get_BorderColor` method retrieves the current border color.

## Syntax


```C++
HRESULT get_BorderColor(
   long *Color
);
```



## Parameters

<dl> <dt>

*Color* 
</dt> <dd>

Pointer to the current border color.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

An application can set a destination rectangle in which the video should be displayed. This rectangle is relative to the client area for the window. If this is done (the default is to always paint the entire window), there is a border surrounding the video. This property affects the color used by the border. Although the parameter is specified as a **LONG** type, it is actually a **COLORREF** value.

This member function is meant to be called by external objects through the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface, and therefore locks the critical section to synchronize with the associated filter. Call the [**CBaseControlWindow::GetBorderColour**](cbasecontrolwindow-getbordercolour.md) member function to retrieve this property if not calling from an external object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




