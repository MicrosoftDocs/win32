---
description: The get\_Height method retrieves the current window height.
ms.assetid: 841c7d5d-f633-41fb-9cde-6126cd1cab9b
title: CBaseControlWindow.get_Height method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_Height
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_Height method

The `get_Height` method retrieves the current window height.

## Syntax


```C++
HRESULT get_Height(
   long *pHeight
);
```



## Parameters

<dl> <dt>

*pHeight* 
</dt> <dd>

Pointer to the current window height, in pixels.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 




