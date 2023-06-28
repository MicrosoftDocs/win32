---
description: The put\_WindowState method sets the window state.
ms.assetid: 0d22fa84-17bc-4228-b86e-d31857156802
title: CBaseControlWindow.put_WindowState method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.put\_WindowState method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




