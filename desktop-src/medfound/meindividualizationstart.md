---
description: Raised by the policy engine when individualization is about to begin. Individualization is performed using the applications implementation of the IMFContentProtectionManager interface.
ms.assetid: a3ba98ee-4d2e-466d-be9a-c7e3b5f920a7
title: MEIndividualizationStart event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEIndividualizationStart event

Raised by the policy engine when individualization is about to begin. Individualization is performed using the application's implementation of the [**IMFContentProtectionManager**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentprotectionmanager) interface.

An individualized application is one that has received an upgrade to its digital rights management (DRM) components that differentiates it from all other copies of the same application. Content owners can require that their protected files be played only on an application that has been individualized.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Remarks

When license acquisition is completed, the policy engine raises the [MEIndividualizationCompleted](meindividualizationcompleted.md) event.

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

 

 




