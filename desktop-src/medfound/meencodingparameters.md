---
Description: Sent by the pipeline to encoder MFTs serially with media samples via IMFTransformProcessEvent.
ms.assetid: D5D4544B-CD8D-4C94-B050-7BA1944800CC
title: MEEncodingParameters event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEEncodingParameters event

Sent by the pipeline to encoder MFTs serially with media samples via [**IMFTransform::ProcessEvent**](/windows/win32/mftransform/nf-mftransform-imftransform-processevent?branch=master).

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                         | Description                                                                                                                    |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master)<br/> | Contains the new ICodecAPI-based settings that the encoder should apply on subsequent incoming samples.<br/> <br/> |



## Remarks

Event payload is an attribute store (IMFAttributes pointer) that contains the new ICodecAPI-based /// settings that the encoder should apply on subsequent incoming samples.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




