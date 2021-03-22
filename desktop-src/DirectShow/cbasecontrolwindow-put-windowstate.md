---
description: The put\_WindowState method sets the window state.
ms.assetid: 0d22fa84-17bc-4228-b86e-d31857156802
title: CBaseControlWindow.put_WindowState method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_WindowState
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.put\_WindowState method

The `put_WindowState` method sets the window state.

## Syntax


```C++
HRESULT put_WindowState(
   long WindowState
);
```



## Parameters

<dl> <dt>

*WindowState* 
</dt> <dd>

New window state.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function takes the same parameters as the Microsoft Win32 **ShowWindow** function (for example, WS\_SHOWNORMAL, WS\_SHOWMINNOACTIVATE, and WS\_SHOWMAXIMIZED).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




