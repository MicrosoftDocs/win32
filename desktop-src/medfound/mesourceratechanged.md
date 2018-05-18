---
Description: 'Raised by a media source when the playback rate changes. This event is sent after the IMFRateControl::SetRate method completes asynchronously.'
ms.assetid: '68a7fe64-e28a-4c20-830c-9402e1fb57f8'
title: MESourceRateChanged event
---

# MESourceRateChanged event

Raised by a media source when the playback rate changes. This event is sent after the [**IMFRateControl::SetRate**](imfratecontrol-setrate.md) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE           | Description                                   |
|-------------------|-----------------------------------------------|
| VT\_R4<br/> | The new playback rate.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Implementing Rate Control](implementing-rate-control.md)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Rate Control](rate-control.md)
</dt> <dt>

[**IMFRateControl::SetRate**](imfratecontrol-setrate.md)
</dt> </dl>

 

 




