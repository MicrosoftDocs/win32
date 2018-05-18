---
Description: 'The put\_AutoShow method sets the AutoShow state flag.'
ms.assetid: '857472b8-845b-46d3-8593-3fba9a9c8cdc'
title: 'CBaseControlWindow.put\_AutoShow method'
---

# CBaseControlWindow.put\_AutoShow method

The `put_AutoShow` method sets the AutoShow state flag.

## Syntax


```C++
HRESULT put_AutoShow(
   long AutoShow
);
```



## Parameters

<dl> <dt>

*AutoShow* 
</dt> <dd>

Automation Boolean flag (0 is off, –1 is on).

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This property simplifies window display access for applications. If this is set to –1 (on), the window, which is typically hidden after the filter is connected, will be displayed automatically when the filter pauses or runs. The window should not be hidden when the filter stops, however. If this is set to 0 (off), the window is made visible only when the application calls [**CBaseControlWindow::put\_Visible**](cbasecontrolwindow-put-visible.md) or [**CBaseControlWindow::put\_WindowState**](cbasecontrolwindow-put-windowstate.md) with the appropriate parameters.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




