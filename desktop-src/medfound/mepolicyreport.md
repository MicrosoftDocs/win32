---
description: Raised by a trusted output to send status information about the enforcement of the output policy.
ms.assetid: 4906f6c3-1570-421f-aef1-914bd338bb1f
title: MEPolicyReport event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEPolicyReport event

Raised by a trusted output to send status information about the enforcement of the output policy.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

Attributes and status codes for this event depend on the specific content protection system enforced by the trusted output.

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

 

 




