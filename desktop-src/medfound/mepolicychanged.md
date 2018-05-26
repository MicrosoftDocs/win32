---
Description: Raised by a pipeline component when the output policy for the stream changes. This event applies only to protected content.
ms.assetid: 9dc78dc6-3fc2-4a81-ad41-45ff3fdbdade
title: MEPolicyChanged event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEPolicyChanged event

Raised by a pipeline component when the output policy for the stream changes. This event applies only to protected content.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE                | Description                                                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the [**IMFOutputPolicy**](/windows/win32/mfidl/nn-mfidl-imfoutputpolicy?branch=master) interface of the new policy for the stream.<br/> <br/> |



## Remarks

All trusted outputs must handle this event. Media Foundation transforms (MFTs) receive this event through the [**IMFTransform::ProcessEvent**](/windows/win32/mftransform/nf-mftransform-imftransform-processevent?branch=master) method. Media sinks receive this event through the [**IMFStreamSink::PlaceMarker**](/windows/win32/mfidl/nf-mfidl-imfstreamsink-placemarker?branch=master) method.

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

 

 




