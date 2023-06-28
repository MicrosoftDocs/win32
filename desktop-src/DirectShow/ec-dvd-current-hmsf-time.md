---
description: Signals the current time, in DVD\_HMSF\_TIMECODE format, relative to the start of the title. This event is triggered at the beginning of every VOBU, which occurs every 0.4 to 1.0 seconds.
ms.assetid: 7c81a09a-21f3-49b2-b90a-7cbc9c815bad
title: EC_DVD_CURRENT_HMSF_TIME (Dvdevcode.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EC_DVD_CURRENT_HMSF_TIME
api_type: 
- HeaderDef
api_location: 
- dvdevcode.h
ms.custom: UpdateFrequency5
---

# EC\_DVD\_CURRENT\_HMSF\_TIME

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Signals the current time, in [**DVD\_HMSF\_TIMECODE**](/windows/win32/api/strmif/ns-strmif-dvd_hmsf_timecode) format, relative to the start of the title. This event is triggered at the beginning of every VOBU, which occurs every 0.4 to 1.0 seconds.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

A ULONG value that contains the DVD\_HMSF\_TIMECODE structure. Assign lParam1 to a ULONG variable and then cast that variable to a DVD\_HMSF\_TIMECODE to access its values.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

A ULONG value containing a union of [**DVD\_TIMECODE\_FLAGS**](/windows/win32/api/strmif/ne-strmif-dvd_timecode_flags).

</dd> </dl>

## Remarks

The DVD\_HMSF\_TIMECODE format is intended to replace the old BCD format that is returned in EC\_DVD\_CURRENT\_TIME events. The HMSF timecodes are easier to work with. To have the Navigator send EC\_DVD\_CURRENT\_HMSF\_TIME events instead of EC\_DVD\_CURRENT\_TIME events, an application must call `IDvdControl2::SetOption(DVD_HMSF_TimeCodeEvents, TRUE)`. When this flag is set, the Navigator will also expect all time parameters in the [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2) and [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2) methods to be passed as DVD\_HMSF\_TIMECODEs.

This event is raised in the title domains.

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

 

 




