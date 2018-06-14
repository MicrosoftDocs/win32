---
Description: Raised by the stream sinks of the enhanced video renderer (EVR) if the video device changes.
ms.assetid: 5b663d6b-5df8-4321-a6a5-a21b9810065a
title: MEStreamSinkDeviceChanged event
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MEStreamSinkDeviceChanged event

Raised by the stream sinks of the enhanced video renderer (EVR) if the video device changes. For example, the EVR raises this event when it receives an [**EC\_DISPLAY\_CHANGED**](https://msdn.microsoft.com/en-us/library/Dd319492(v=VS.85).aspx) event.

The Media Foundation pipeline responds to this event by resubmitting all sample requests that failed while the device was changing.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> </dl>

 

 




