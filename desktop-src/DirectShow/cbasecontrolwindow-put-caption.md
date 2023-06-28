---
description: The put\_Caption method sets the window title or caption.
ms.assetid: 6671805a-e1ef-40f1-bc3f-bf7954ff9851
title: CBaseControlWindow.put_Caption method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_Caption
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.put\_Caption method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `put_Caption` method sets the window title or caption.

## Syntax


```C++
HRESULT put_Caption(
   BSTR strCaption
);
```



## Parameters

<dl> <dt>

*strCaption* 
</dt> <dd>

New window caption.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Most top-level windows on a Windows-based desktop have a title (caption) associated with them. This property can be queried and set through the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface. Any caption set will be visible only if the window has the WS\_CAPTION style applied. If it does not, the caption can still be set (and retrieved), although it will not be visible to the user.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




