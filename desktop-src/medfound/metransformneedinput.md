---
Description: Sent by an asynchronous Media Foundation transform (MFT) to request a new input sample.
ms.assetid: 5d5c50d9-fe4e-47ff-ae09-980911ebfb22
title: METransformNeedInput event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# METransformNeedInput event

Sent by an asynchronous Media Foundation transform (MFT) to request a new input sample.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description               |
|----------------------|---------------------------|
| VT\_EMPTY<br/> | No event data.<br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                        | Description                                                                           |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [MF\_EVENT\_MFT\_INPUT\_STREAM\_ID](mf-event-mft-input-stream-id.md)<br/> | The identifier of the stream that needs input data.<br/>*(Required)*<br/> |



## Remarks

Asynchronous MFTs send this event through the [**IMFMediaEventGenerator**](/windows/win32/mfobjects/nn-mfobjects-imfmediaeventgenerator?branch=master) interface. Synchronous MFTs never send this event.

When the client of the MFT receives this event, it should call [**IMFTransform::ProcessInput**](/windows/win32/mftransform/nf-mftransform-imftransform-processinput?branch=master) to deliver the next sample. The [MF\_EVENT\_MFT\_INPUT\_STREAM\_ID](mf-event-mft-input-stream-id.md) attribute of the event object specifies which input stream requires data.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Asynchronous MFTs](asynchronous-mfts.md)
</dt> </dl>

 

 




