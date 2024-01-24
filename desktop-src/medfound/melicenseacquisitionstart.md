---
description: Raised by the policy engine when license acquisition is about to begin. License acquisition is performed using the applications implementation of the IMFContentProtectionManager interface.
ms.assetid: c328743c-a69b-431e-8a05-0e140aad9b4d
title: MELicenseAcquisitionStart event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MELicenseAcquisitionStart event

Raised by the policy engine when license acquisition is about to begin. License acquisition is performed using the application's implementation of the [**IMFContentProtectionManager**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentprotectionmanager) interface.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

When license acquisition is completed, the policy engine raises the [MELicenseAcquisitionCompleted](melicenseacquisitioncompleted.md) event.

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

 

 




