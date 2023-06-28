---
description: The PossiblyEatMessage method forwards keyboard and mouse messages to the message-drain window.
ms.assetid: 8e344c5d-2f94-454f-89b7-45c539b6e833
title: CBaseControlWindow.PossiblyEatMessage method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.PossiblyEatMessage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.PossiblyEatMessage method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `PossiblyEatMessage` method forwards keyboard and mouse messages to the message-drain window.

## Syntax


```C++
BOOL PossiblyEatMessage(
   UINT   uMsg,
   WPARAM wParam,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*uMsg* 
</dt> <dd>

Window message.

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

Returns **TRUE** if the message was forwarded to the window, or **FALSE** otherwise.

## Remarks

The message-drain window is a window designated to receive certain mouse and keyboard messages. Initially the window is **NULL**; it can be set by calling [**CBaseControlWindow::put\_MessageDrain**](cbasecontrolwindow-put-messagedrain.md).

If the message-drain window is non-**NULL**, `PossiblyEatMessage` posts the following messages to that window:

-   WM\_CHAR
-   WM\_DEADCHAR
-   WM\_KEYDOWN
-   WM\_KEYUP
-   WM\_LBUTTONDBLCLK
-   WM\_LBUTTONDOWN
-   WM\_LBUTTONUP
-   WM\_MBUTTONDBLCLK
-   WM\_MBUTTONDOWN
-   WM\_MBUTTONUP
-   WM\_MOUSEACTIVATE
-   WM\_MOUSEMOVE
-   WM\_NCLBUTTONDBLCLK
-   WM\_NCLBUTTONDOWN
-   WM\_NCLBUTTONUP
-   WM\_NCMBUTTONDBLCLK
-   WM\_NCMBUTTONDOWN
-   WM\_NCMBUTTONUP
-   WM\_NCMOUSEMOVE
-   WM\_NCRBUTTONDBLCLK
-   WM\_NCRBUTTONDOWN
-   WM\_NCRBUTTONUP
-   WM\_RBUTTONDBLCLK
-   WM\_RBUTTONDOWN
-   WM\_RBUTTONUP
-   WM\_SYSCHAR
-   WM\_SYSDEADCHAR
-   WM\_SYSKEYDOWN
-   WM\_SYSKEYUP

It ignores other messages. If the message-drain window is **NULL**, the method ignores all window messages. The method returns **TRUE** if it posts the message, or **FALSE** otherwise. The **CBaseWindow** class calls this method when it receives a window message.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




