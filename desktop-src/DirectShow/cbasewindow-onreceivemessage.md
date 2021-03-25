---
description: The OnReceiveMessage method handles window messages.
ms.assetid: 0f074f9b-00e5-42ff-a491-020d441acad1
title: CBaseWindow.OnReceiveMessage method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.OnReceiveMessage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.OnReceiveMessage method

The `OnReceiveMessage` method handles window messages.

## Syntax


```C++
virtual LRESULT OnReceiveMessage(
   HWND   hwnd,
   INT    uMsg,
   WPARAM wParam,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle to the window.

</dd> <dt>

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

Returns 0 if the message was processed, or 1 if the message was not processed.

## Remarks

The base class handles the following messages:

-   WM\_CLOSE
-   WM\_MOVE
-   WM\_PALETTECHANGED
-   WM\_QUERYNEWPALETTE
-   WM\_SIZE
-   WM\_SYSCOLORCHANGE

A derived class can override this method to handle other messages. The derived class should call the base class method to handle any messages that the derived class ignores.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




