---
description: Raised by a pipeline component when the configuration changes for one of the output protection schemes. This event applies only to protected content.
ms.assetid: 0a13fc08-2bbe-46d8-a076-6165cca6ea36
title: MEContentProtectionMessage event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEContentProtectionMessage event

Raised by a pipeline component when the configuration changes for one of the output protection schemes. This event applies only to protected content.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

All trusted outputs must handle this event. Media Foundation transforms (MFTs) receive this event through the [**IMFTransform::ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent) method. Media sinks receive this event through the [**IMFStreamSink::PlaceMarker**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamsink-placemarker) method.

The trusted output must apply the policy changes or return the error code MF\_E\_POLICY\_UNSUPPORTED.

The event data and attributes depend on the content protection system in use.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




