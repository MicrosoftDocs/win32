---
Description: Sent by an asynchronous Media Foundation transform (MFT) when new output data is available from the MFT.
ms.assetid: a9403ad3-81bf-4cd7-ba7f-816b901bb02c
title: METransformHaveOutput event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# METransformHaveOutput event

Sent by an asynchronous Media Foundation transform (MFT) when new output data is available from the MFT.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description               |
|----------------------|---------------------------|
| VT\_EMPTY<br/> | No event data.<br/> |



## Attributes

No attributes are defined for this event.

## Remarks

Asynchronous MFTs send this event through the [**IMFMediaEventGenerator**](/windows/win32/mfobjects/nn-mfobjects-imfmediaeventgenerator?branch=master) interface. Synchronous MFTs never send this event.

When the client of the MFT receives this event, it should call [**IMFTransform::ProcessOutput**](/windows/win32/mftransform/nf-mftransform-imftransform-processoutput?branch=master) to get the output.

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

 

 




