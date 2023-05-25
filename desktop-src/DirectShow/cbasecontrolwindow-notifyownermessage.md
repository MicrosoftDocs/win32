---
description: The NotifyOwnerMessage method passes along specific messages to the video window.
ms.assetid: 8b27281a-5b8a-46c3-aa66-390d4496f30e
title: CBaseControlWindow.NotifyOwnerMessage method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.NotifyOwnerMessage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.NotifyOwnerMessage method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `NotifyOwnerMessage` method passes along specific messages to the video window.

## Syntax


```C++
HRESULT NotifyOwnerMessage(
   long     hwnd,
   long     uMsg,
   LONG_PTR wParam,
   LONG_PTR lParam
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle to the video window.

</dd> <dt>

*uMsg* 
</dt> <dd>

Message details.

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

Returns NO\_ERROR.

## Remarks

When the video window is a child of another window, it does not receive certain top-level window messages. These messages can be valuable to a renderer, because they could affect its behavior. `NotifyOwnerMessage` passes any of the following messages to the video window.

-   WM\_ACTIVATEAPP
-   WM\_DEVMODECHANGE
-   WM\_DISPLAYCHANGE
-   WM\_PALETTECHANGED
-   WM\_PALETTEISCHANGING
-   WM\_QUERYNEWPALETTE
-   WM\_SYSCOLORCHANGE

You can request that the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) plug-in distributor (PID) make a window become a child of another window. When this occurs, the PID will look for certain messages that might be sent to the owning window. The PID will then forward those messages to the owned window. The default processing for the messages is to send them to the owned window procedure synchronously by calling the Win32 **SendMessage** function.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




