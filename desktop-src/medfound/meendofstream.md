---
Description: Raised by a media stream when the stream ends.
ms.assetid: e793131a-f737-411f-a9fc-03b5b3d09aea
title: MEEndOfStream event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEEndOfStream event

Raised by a media stream when the stream ends.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

When the [Media Session](media-session.md) receives the MEEndOfStream event, it calls [**IMFStreamSink::PlaceMarker**](/windows/win32/mfidl/nf-mfidl-imfstreamsink-placemarker?branch=master) on the corresponding media sink, with the **MFSTREAMSINK\_MARKER\_ENDOFSEGMENT** marker type.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




