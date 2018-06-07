---
Description: The get\_Left method retrieves the current left window coordinate.
ms.assetid: 9ee71bd3-1ff5-4574-8dcd-5ba6490d9785
title: CBaseControlWindow.get\_Left method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseControlWindow.get\_Left method

The `get_Left` method retrieves the current left window coordinate.

## Syntax


```C++
HRESULT get_Left(
   long *pLeft
);
```



## Parameters

<dl> <dt>

*pLeft* 
</dt> <dd>

Pointer to the left coordinate, in pixels.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

The window has a position on the desktop. This position is expressed in pixels by four coordinates (left, top, right, and bottom). Interfaces that are automated by OLE typically express this position through left, top, width, and height; this is the convention used in DirectShow. All coordinates are expressed in pixels, and changing any coordinate will update the window immediately.

Setting the left or top coordinates moves the window left and up, respectively; these coordinates have no effect on the width and height of the window. Likewise, setting the width and height have no effect on the left and top coordinates.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




