---
description: Sent by the IMFMediaSource that encapsulates the device to indicate that the device has been preempted.
ms.assetid: 85EE663C-94B7-47EA-ABBA-A8371342EEB2
title: MEVideoCaptureDevicePreempted event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEVideoCaptureDevicePreempted event

Sent by the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) that encapsulates the device to indicate that the device has been preempted.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



## Remarks

This event is sent by the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) that encapsulates the device.

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

 

 




