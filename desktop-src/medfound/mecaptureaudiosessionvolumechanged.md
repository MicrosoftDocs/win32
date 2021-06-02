---
description: Sent by an audio capture source when the volume changes.
ms.assetid: 4A525D5F-9226-4277-BDB7-174BF65FE320
title: MECaptureAudioSessionVolumeChanged event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MECaptureAudioSessionVolumeChanged event

Sent by an audio capture source when the volume changes.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



## Remarks

This event is sent by the media stream of the audio capture source.

The audio capture source sends this event if an external action changes the volume—for example, if the user changes the volume through the Control Panel. The capture source does not send the event if the application changes the volume directly on the source.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




