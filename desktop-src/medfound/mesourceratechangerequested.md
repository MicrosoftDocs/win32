---
description: Raised by a media source to request a new playback rate. The application should call IMFRateControl::SetRate with the requested rate. A media source might raise this event if it cannot continue playback at the current rate.
ms.assetid: 705e5a79-836b-417b-a7ed-c733572f6905
title: MESourceRateChangeRequested event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESourceRateChangeRequested event

Raised by a media source to request a new playback rate. The application should call [**IMFRateControl::SetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratecontrol-setrate) with the requested rate. A media source might raise this event if it cannot continue playback at the current rate.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE           | Description                                             |
|-------------------|---------------------------------------------------------|
| VT\_R4<br/> | The requested new playback rate.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                    | Description                                                                       |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**MF\_EVENT\_DO\_THINNING**](mf-event-do-thinning-attribute.md)<br/> | Specifies whether the media source also requests thinning.<br/> <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




