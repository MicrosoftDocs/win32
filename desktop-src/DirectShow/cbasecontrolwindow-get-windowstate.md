---
description: The get\_WindowState method retrieves the current window state.
ms.assetid: 118b6710-b041-4a7d-8cdb-b96ae3dcbb09
title: CBaseControlWindow.get_WindowState method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.get\_WindowState method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




