---
description: The put\_MessageDrain method sets the window to receive window messages sent to the video renderer.
ms.assetid: b2d2d489-a66f-474a-b8bf-b019179f6f69
title: CBaseControlWindow.put_MessageDrain method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_MessageDrain
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.put\_MessageDrain method

The `put_MessageDrain` method sets the window to receive window messages sent to the video renderer.

## Syntax


```C++
HRESULT put_MessageDrain(
   OAHWND Drain
);
```



## Parameters

<dl> <dt>

*Drain* 
</dt> <dd>

Window to post messages to.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Messages sent to the video renderer filter can be posted to another window. This member function registers the window to receive these messages. Unlike the [**CBaseControlWindow::put\_Owner**](cbasecontrolwindow-put-owner.md) member function, this member function does not make the video window a child of another window. It is particularly useful for full-screen video renderers, which cannot be child windows.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




