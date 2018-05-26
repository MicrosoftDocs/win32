---
Description: Raised by a stream sink when the stream has received enough pre-roll data to begin rendering. This event is raised by media sinks that support the IMFMediaSinkPreroll interface.
ms.assetid: 1ecb1805-73ce-4741-b969-6eb88982ee26
title: MEStreamSinkPrerolled event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEStreamSinkPrerolled event

Raised by a stream sink when the stream has received enough pre-roll data to begin rendering. This event is raised by media sinks that support the [**IMFMediaSinkPreroll**](/windows/win32/mfidl/nn-mfidl-imfmediasinkpreroll?branch=master) interface.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



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

 

 




