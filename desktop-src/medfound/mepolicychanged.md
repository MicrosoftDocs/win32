---
Description: 'Raised by a pipeline component when the output policy for the stream changes. This event applies only to protected content.'
ms.assetid: '9dc78dc6-3fc2-4a81-ad41-45ff3fdbdade'
title: MEPolicyChanged event
---

# MEPolicyChanged event

Raised by a pipeline component when the output policy for the stream changes. This event applies only to protected content.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFOutputPolicy**](imfoutputpolicy.md) interface of the new policy for the stream.<br/> <br/> |



## Remarks

All trusted outputs must handle this event. Media Foundation transforms (MFTs) receive this event through the [**IMFTransform::ProcessEvent**](imftransform-processevent.md) method. Media sinks receive this event through the [**IMFStreamSink::PlaceMarker**](imfstreamsink-placemarker.md) method.

The trusted output must apply the new policy or return the error code MF\_E\_POLICY\_UNSUPPORTED.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




