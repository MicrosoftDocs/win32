---
description: The get\_Owner method retrieves the current window owner.
ms.assetid: f0eea5e7-4dfa-4973-ae12-487657e6be80
title: CBaseControlWindow.get_Owner method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_Owner
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_Owner method

The `get_Owner` method retrieves the current window owner.

## Syntax


```C++
HRESULT get_Owner(
   OAHWND *Owner
);
```



## Parameters

<dl> <dt>

*Owner* 
</dt> <dd>

Pointer to the window owner.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

The video window can play back within a document environment. To do this, the window must be made a child of another window (so that it is clipped and moved appropriately). This property allows the owner of the window to be set and retrieved. When the window is owned by another window, it simply calls the Microsoft Win32 **SetParent** function. An application calling this function will change the window styles to set the WS\_CHILD bit on.

When the window is owned by another window, it will automatically forward certain sets of messages (in particular, mouse and keyboard messages). This allows an application to do simple hot-spot editing and other interactions.

This member function is meant to be called by external objects through the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface, and therefore locks the critical section to synchronize with the associated filter. Call the [**CBaseControlWindow::GetOwnerWindow**](cbasecontrolwindow-getownerwindow.md) member function to retrieve this property if not calling from an external object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




