---
description: The IsCursorHidden method retrieves the current state of the m\_bCursorHidden data member.
ms.assetid: 4b97b89d-876a-470c-ac41-a88fecb52b2d
title: CBaseControlWindow.IsCursorHidden method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.IsCursorHidden
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.IsCursorHidden method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `IsCursorHidden` method retrieves the current state of the **m\_bCursorHidden** data member.

## Syntax


```C++
HRESULT IsCursorHidden(
   long *CursorHidden
);
```



## Parameters

<dl> <dt>

*CursorHidden* 
</dt> <dd>

Pointer to the value of **m\_bCursorHidden**.

</dd> </dl>

## Return value

When called without a parameter, returns OATRUE if the cursor is hidden, or OAFALSE if the cursor is visible.

## Remarks

Internal objects should call this member function without the *CursorHidden* parameter to avoid locking the critical section. External objects access this member function with the *CursorHidden* parameter through the [**IVideoWindow::IsCursorHidden**](/windows/desktop/api/Control/nf-control-ivideowindow-iscursorhidden) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




