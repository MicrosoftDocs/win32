---
description: Sent by an asynchronous Media Foundation transform (MFT) in response to an MFT\_MESSAGE\_COMMAND\_MARKER message.
ms.assetid: d0c0d62d-9133-4d4b-8606-c2ae1d4c9f0a
title: METransformMarker event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# METransformMarker event

Sent by an asynchronous Media Foundation transform (MFT) in response to an **MFT\_MESSAGE\_COMMAND\_MARKER** message.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description               |
|----------------------|---------------------------|
| VT\_EMPTY<br/> | No event data.<br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                      | Description                                                                                                                |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [MF\_EVENT\_MFT\_CONTEXT](mf-event-mft-context.md)<br/> | The value of the *ulParam* parameter from the **MFT\_MESSAGE\_COMMAND\_MARKER** message.<br/>*(Required)*<br/> |



## Remarks

Asynchronous MFTs send this event through the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. Synchronous MFTs never send this event.

The client of an asynchronous MFT can place a marker in the stream by calling [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the **MFT\_MESSAGE\_COMMAND\_MARKER** message. The *ulParam* parameter contains application-defined data.

When the MFT finishes processing all of the input data that was available at the time of the [**ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) call, the MFT queues an METransformMarker event. The [MF\_EVENT\_MFT\_CONTEXT](mf-event-mft-context.md) attribute of the event contains the value of the *ulParam* parameter. For more information, see [Asynchronous MFTs](asynchronous-mfts.md).

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

 

 




