---
description: Sent by an asynchronous Media Foundation transform (MFT) when a drain operation is complete.
ms.assetid: 923055e5-a09a-402e-983b-6fa3cebb1b3a
title: METransformDrainComplete event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# METransformDrainComplete event

Sent by an asynchronous Media Foundation transform (MFT) when a drain operation is complete.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description               |
|----------------------|---------------------------|
| VT\_EMPTY<br/> | No event data.<br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                        | Description                                                                      |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [MF\_EVENT\_MFT\_INPUT\_STREAM\_ID](mf-event-mft-input-stream-id.md)<br/> | The identifier of the stream that was drained.<br/>*(Required)*<br/> |



## Remarks

Asynchronous MFTs send this event through the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. Synchronous MFTs never send this event.

To drain an MFT, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the **MFT\_MESSAGE\_COMMAND\_DRAIN** message. Specify the input stream to drain in the *ulParam* parameter. When the drain operation is completed, an asynchronous MFT sends the METransformDrainComplete event. The [MF\_EVENT\_MFT\_INPUT\_STREAM\_ID](mf-event-mft-input-stream-id.md) attribute of the event contains the stream identifier given in the *ulParam* parameter.

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

 

 




