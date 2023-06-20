---
description: A stream-control start command has taken effect.
ms.assetid: e2f8d9a2-c96c-457c-8a88-7c86d4405928
title: EC_STREAM_CONTROL_STARTED (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EC\_STREAM\_CONTROL\_STARTED

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A stream-control start command has taken effect.

## Parameters

<dl> <dt>

<span id="pSender"></span><span id="psender"></span><span id="PSENDER"></span>*pSender*
</dt> <dd>

(**IUnknown**\*) Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface of the pin that started the stream.

</dd> <dt>

<span id="dwCookie"></span><span id="dwcookie"></span><span id="DWCOOKIE"></span>*dwCookie*
</dt> <dd>

(**DWORD**) User-defined value.

</dd> </dl>

## Default Action

None.

## Remarks

Filters send this event in response to the [**IAMStreamControl::StartAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-startat) method. This method specifies a reference time for a pin to begin streaming. When streaming does begin, the filter sends this event.

The *pSender* parameter specifies the pin that executes the start command. Depending on the implementation, it might not be the pin that received the [**StartAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-startat) call.

The *dwCookie* parameter is specified by the application in the [**StartAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-startat) method. This parameter enables the application to track multiple calls to the method.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




