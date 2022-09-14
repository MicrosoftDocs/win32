---
description: Sent by the pipeline to encoder MFTs serially with media samples via IMFTransform::ProcessEvent.
ms.assetid: D5D4544B-CD8D-4C94-B050-7BA1944800CC
title: MEEncodingParameters event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEEncodingParameters event

Sent by the pipeline to encoder MFTs serially with media samples via [**IMFTransform::ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent).

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                         | Description                                                                                                                    |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes)<br/> | Contains the new ICodecAPI-based settings that the encoder should apply on subsequent incoming samples.<br/> <br/> |



## Remarks

Event payload is an attribute store (IMFAttributes pointer) that contains the new ICodecAPI-based /// settings that the encoder should apply on subsequent incoming samples.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




