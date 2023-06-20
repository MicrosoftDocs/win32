---
description: Signals that the current subpicture stream number changed for the main title.
ms.assetid: b6da3201-55df-47dc-ad4f-5cd2e78073ee
title: EC_DVD_SUBPICTURE_STREAM_CHANGE (Dvdevcode.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_SUBPICTURE_STREAM_CHANGE
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
ms.custom: UpdateFrequency5
---

# EC\_DVD\_SUBPICTURE\_STREAM\_CHANGE

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Signals that the current subpicture stream number changed for the main title.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the new user subpicture stream number. Subpicture stream numbers range from 0 to 31. Stream 0xFFFFFFFF indicates that no stream is selected.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Boolean value that indicates the subpicture's on/off state.

</dd> </dl>

## Remarks

The subpicture can change automatically with a navigation command authored on disc as well as through application control using [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2).

This event is raised in all domains.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdevcode.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> <dt>

[DVD Event Notification Codes](dvd-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




