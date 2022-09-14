---
description: The get\_Top method retrieves the top window coordinate.
ms.assetid: 1e7910bd-e38e-4586-9dd6-701f69c0f6e7
title: CBaseControlWindow.get_Top method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_Top
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_Top method

The `get_Top` method retrieves the top window coordinate.

## Syntax


```C++
HRESULT get_Top(
   long *pTop
);
```



## Parameters

<dl> <dt>

*pTop* 
</dt> <dd>

Pointer to the top coordinate, in pixels.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

The window has a position on the desktop. This is expressed in pixels by four coordinates (left, top, right, and bottom). Interfaces that are automated by OLE typically express this position through left, top, width, and height; this is the convention used in DirectShow. All coordinates are expressed in pixels, and changing any coordinate will update the window immediately.

Setting the left or top coordinates moves the window left or up, respectively; these coordinates have no effect on the width and height of the window. Likewise, setting the width and height does not affect the left and top coordinates.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




