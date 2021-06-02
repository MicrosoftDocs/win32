---
description: The put\_BorderColor method changes the border color.
ms.assetid: bb19d338-7fd1-448c-be94-1c71d4a9a330
title: CBaseControlWindow.put_BorderColor method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_BorderColor
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.put\_BorderColor method

The `put_BorderColor` method changes the border color.

## Syntax


```C++
HRESULT put_BorderColor(
   long Color
);
```



## Parameters

<dl> <dt>

*Color* 
</dt> <dd>

New border color.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

An application can establish a destination rectangle in which the video should be displayed. This rectangle is relative to the client area for the window. If this is done (the default is to always paint the entire window), there is a border surrounding the video. This property affects the color used by the border. Although the parameter is specified as a **LONG** type, it is actually a **COLORREF** value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




