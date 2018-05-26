---
Description: Sent by the IMFMediaSource that encapsulates the device to indicate that the device has been removed.
ms.assetid: 107AFF19-B444-4B62-9217-46A99AC3632C
title: MEVideoCaptureDeviceRemoved event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEVideoCaptureDeviceRemoved event

Sent by the [**IMFMediaSource**](/windows/win32/mfidl/nn-mfidl-imfmediasource?branch=master) that encapsulates the device to indicate that the device has been removed.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE               | Description                           |
|-----------------------|---------------------------------------|
| VT\_EMPTY <br/> | No event data.<br/> <br/> |



## Remarks

This event is sent by the [**IMFMediaSource**](/windows/win32/mfidl/nn-mfidl-imfmediasource?branch=master) that encapsulates the device.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




