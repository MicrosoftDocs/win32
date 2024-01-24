---
description: Sent by an asynchronous Media Foundation transform (MFT) to request a new input sample.
ms.assetid: 5d5c50d9-fe4e-47ff-ae09-980911ebfb22
title: METransformNeedInput event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# METransformNeedInput event

Sent by an asynchronous Media Foundation transform (MFT) to request a new input sample.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description               |
|----------------------|---------------------------|
| VT\_EMPTY<br/> | No event data.<br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                        | Description                                                                           |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [MF\_EVENT\_MFT\_INPUT\_STREAM\_ID](mf-event-mft-input-stream-id.md)<br/> | The identifier of the stream that needs input data.<br/>*(Required)*<br/> |



## Remarks

Asynchronous MFTs send this event through the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. Synchronous MFTs never send this event.

When the client of the MFT receives this event, it should call [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) to deliver the next sample. The [MF\_EVENT\_MFT\_INPUT\_STREAM\_ID](mf-event-mft-input-stream-id.md) attribute of the event object specifies which input stream requires data.

## Requirements



| Requirement | Value |
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

 

 




