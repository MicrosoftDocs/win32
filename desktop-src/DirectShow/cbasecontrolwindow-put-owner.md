---
description: The put\_Owner method sets the video window's parent window; the parent window then forwards certain messages to the video window.
ms.assetid: 8ed85cb0-47be-40c1-947a-dd9f7850d867
title: CBaseControlWindow.put_Owner method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_Owner
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.put\_Owner method

The `put_Owner` method sets the video window's parent window; the parent window then forwards certain messages to the video window.

## Syntax


```C++
HRESULT put_Owner(
   OAHWND Owner
);
```



## Parameters

<dl> <dt>

*Owner* 
</dt> <dd>

Handle to the parent window.

</dd> </dl>

## Return value

Returns NOERROR.

## Remarks

Internally, this method calls the Microsoft Win32 **SetParent** function to set the new owner and sets the parent window's style to WS\_CHILD. The parent window will then forward certain sets of messages (in particular, mouse and keyboard messages) to the video window.

After you set the video window's owner, you must set the owner to **NULL** and the owner's window style to WS\_OVERLAPPED and WS\_CLIPCHILDREN before releasing the filter graph. When you set the owner to **NULL**, this method turns off the parent window's WS\_CHILD bit. If you don't set the owner to **NULL**, the parent window will continue to pass messages to the video window and errors will likely occur when the application closes.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




