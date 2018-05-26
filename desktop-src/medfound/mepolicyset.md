---
Description: Raised by an output trust authority (OTA) when the IMFOutputTrustAuthoritySetPolicy method completes asynchronously.
ms.assetid: c5d8a88e-2864-45a0-97b7-051341116a4c
title: MEPolicySet event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MEPolicySet event

Raised by an output trust authority (OTA) when the [**IMFOutputTrustAuthority::SetPolicy**](/windows/win32/mfidl/nf-mfidl-imfoutputtrustauthority-setpolicy?branch=master) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




