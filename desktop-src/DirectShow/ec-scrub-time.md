---
description: Specifies the time stamp for the most recent frame step.
ms.assetid: 2c2ef8b8-7bee-4cd8-ad87-b48d6a48aa0e
title: EC_SCRUB_TIME (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC\_SCRUB\_TIME

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the time stamp for the most recent frame step.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**DWORD**) Lower 32 bits of the time stamp.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

(**DWORD**) Upper 32 bits of the time stamp.

</dd> </dl>

## Default Action

None.

## Remarks

The presenter for the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) filter sends this message to the EVR when it completes a frame step.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> </dl>

 

 




