---
Description: The get\_WindowStyle method retrieves the standard window styles.
ms.assetid: 5c204814-5c7c-47e2-95dd-86455ed77cc7
title: CBaseControlWindow.get\_WindowStyle method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_WindowStyle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_WindowStyle method

The `get_WindowStyle` method retrieves the standard window styles.

## Syntax


```C++
HRESULT get_WindowStyle(
   long *pWindowStyle
);
```



## Parameters

<dl> <dt>

*pWindowStyle* 
</dt> <dd>

Pointer to window styles.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function returns the standard window styles, such as WS\_CHILD and WS\_VISIBLE. It calls the [**CBaseControlWindow::DoGetWindowStyle**](cbasecontrolwindow-dogetwindowstyle.md) member function.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




