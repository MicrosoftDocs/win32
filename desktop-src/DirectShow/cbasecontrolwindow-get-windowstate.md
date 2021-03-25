---
description: The get\_WindowState method retrieves the current window state.
ms.assetid: 118b6710-b041-4a7d-8cdb-b96ae3dcbb09
title: CBaseControlWindow.get_WindowState method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_WindowState
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_WindowState method

The `get_WindowState` method retrieves the current window state.

## Syntax


```C++
HRESULT get_WindowState(
   long *pWindowState
);
```



## Parameters

<dl> <dt>

*pWindowState* 
</dt> <dd>

Pointer to the window state.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function returns a subset of the parameters of the Microsoft Win32 **ShowWindow** function. In particular, it returns SW\_SHOW and SW\_HIDE, depending on the current visibility of the window. It also returns SW\_MINIMIZE and SW\_MAXIMIZE, depending on whether the window is an icon or is expanded.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




