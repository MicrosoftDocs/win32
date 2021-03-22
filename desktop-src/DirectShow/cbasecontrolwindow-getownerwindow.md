---
description: The GetOwnerWindow method retrieves the owning window handle, m\_hwndOwner.
ms.assetid: fa576b42-b4a7-4374-8ba4-7d21e86d9d61
title: CBaseControlWindow.GetOwnerWindow method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.GetOwnerWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.GetOwnerWindow method

The `GetOwnerWindow` method retrieves the owning window handle, **m\_hwndOwner**.

## Syntax


```C++
HWND GetOwnerWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns the owner window.

## Remarks

Retrieves the owning window without calling the interface method. Use this member function instead of [**CBaseControlWindow::get\_Owner**](cbasecontrolwindow-get-owner.md), unless you are calling this externally through the [**IVideoWindow::get\_Owner**](/windows/desktop/api/Control/nf-control-ivideowindow-get_owner) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




