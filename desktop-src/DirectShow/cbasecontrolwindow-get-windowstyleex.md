---
Description: 'The get\_WindowStyleEx method retrieves the extended window styles.'
ms.assetid: '72955958-bbda-4b8f-9c28-6d3f5eb56a82'
title: 'CBaseControlWindow.get\_WindowStyleEx method'
---

# CBaseControlWindow.get\_WindowStyleEx method

The `get_WindowStyleEx` method retrieves the extended window styles.

## Syntax


```C++
HRESULT get_WindowStyleEx(
   long *pWindowStyleEx
);
```



## Parameters

<dl> <dt>

*pWindowStyleEx* 
</dt> <dd>

Pointer to extended window styles.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function retrieves the extended window styles. It calls the [**CBaseControlWindow::DoGetWindowStyle**](cbasecontrolwindow-dogetwindowstyle.md) member function.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




