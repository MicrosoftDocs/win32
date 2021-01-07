---
description: Raised by an output trust authority (OTA) when the IMFOutputTrustAuthority::SetPolicy method completes asynchronously.
ms.assetid: c5d8a88e-2864-45a0-97b7-051341116a4c
title: MEPolicySet event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEPolicySet event

Raised by an output trust authority (OTA) when the [**IMFOutputTrustAuthority::SetPolicy**](/windows/desktop/api/mfidl/nf-mfidl-imfoutputtrustauthority-setpolicy) method completes asynchronously.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |
| VT\_UI4<br/> | An identifier that can be set on an [IMFOutputPolicy](/windows/win32/api/mfidl/nn-mfidl-imfoutputpolicy) through the [MF_POLICY_ID](mf-policy-id.md) attribute.<br/> <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




