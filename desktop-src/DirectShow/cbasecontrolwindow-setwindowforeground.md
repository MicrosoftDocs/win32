---
description: The SetWindowForeground method moves the video window to the foreground and optionally gives it focus.
ms.assetid: 41c26bff-0023-41ad-bca8-8f0c43c94814
title: CBaseControlWindow.SetWindowForeground method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.SetWindowForeground
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.SetWindowForeground method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetWindowForeground` method moves the video window to the foreground and optionally gives it focus.

## Syntax


```C++
HRESULT SetWindowForeground(
   long Focus
);
```



## Parameters

<dl> <dt>

*Focus* 
</dt> <dd>

Value that specifies whether the video window will get focus. A value of  1 gives the window focus and 0 does not.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                           | Description                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**NOERROR**</dt> </dl>                | The method succeeded.<br/>                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>          | Focus doesn't equal  1 or 0.<br/>                                   |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The current filter isn't connected to a complete filter graph.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




