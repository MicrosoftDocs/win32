---
description: Raised by a trusted output if an error occurs while enforcing the output policy.
ms.assetid: 0cc62915-1ed6-4d1d-9600-0dac0b9034e3
title: MEPolicyError event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEPolicyError event

Raised by a trusted output if an error occurs while enforcing the output policy.

If the Media Session receives this event, it stops playback and forwards the event to the application.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

Possible values retrieved from [**IMFMediaEvent::GetStatus**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getstatus) include the following.



| Value                      | Description                                                    |
|----------------------------|----------------------------------------------------------------|
| MF\_E\_POLICY\_UNSUPPORTED | The trusted output does not support the current output policy. |



 

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

 

 




