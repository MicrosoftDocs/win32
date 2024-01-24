---
description: Raised by the Media Session when the playback rate changes. This event is sent after the IMFRateControl::SetRate method completes asynchronously.
ms.assetid: 6bef923f-4083-46e1-9a2e-49a6825467ec
title: MESessionRateChanged event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESessionRateChanged event

Raised by the Media Session when the playback rate changes. This event is sent after the [**IMFRateControl::SetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratecontrol-setrate) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE           | Description                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------|
| VT\_R4<br/> | The new playback rate, expressed as a ratio of the normal playback rate.<br/> <br/> |



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

 

 




