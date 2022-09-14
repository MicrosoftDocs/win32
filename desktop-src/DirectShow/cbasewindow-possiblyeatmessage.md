---
description: The PossiblyEatMessage method enables a derived class to forward messages to another window.
ms.assetid: d8775182-44ed-4df2-b4b8-1fdf289e2c1a
title: CBaseWindow.PossiblyEatMessage method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.PossiblyEatMessage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.PossiblyEatMessage method

The `PossiblyEatMessage` method enables a derived class to forward messages to another window.

## Syntax


```C++
virtual BOOL PossiblyEatMessage(
   UINT   uMsg,
   WPARAM wParam,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*uMsg* 
</dt> <dd>

Message identifier.

</dd> <dt>

*wParam* 
</dt> <dd>

First message parameter.

</dd> <dt>

*lParam* 
</dt> <dd>

Second message parameter.

</dd> </dl>

## Return value

Returns **TRUE** if the message was forwarded, or **FALSE** otherwise. The base class returns **FALSE**.

## Remarks

Before the [**CBaseWindow::OnReceiveMessage**](cbasewindow-onreceivemessage.md) method handles a message, it calls `PossiblyEatMessage`. If `PossiblyEatMessage` returns **TRUE**, **OnReceiveMessage** ignores the message. A derived class can override `PossiblyEatMessage` so that it forwards some messages to an owner window. For example, the [**CBaseControlWindow**](cbasecontrolwindow.md) class, which derives from **CBaseWindow**, forwards keyboard and mouse messages.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




