---
description: Specifies a context string used by Content Decryption Module (CDM) implementations that use MediaProtectionPMPServer.
title: MF_CONTENTDECRYPTIONMODULE_PMPSTORECONTEXT (mfcontentdecryptionmodule.h)
ms.topic: reference
ms.date: 01/31/2020
---

# MF\_CONTENTDECRYPTIONMODULE\_PMPSTORECONTEXT property

Specifies a context string used by Content Decryption Module (CDM) implementations that use [MediaProtectionPMPServer](/uwp/api/windows.media.protection.mediaprotectionpmpserver).


## Data type

**LPWSTR** (VT_LPWSTR)

## Property GUID

**MF\_CONTENTDECRYPTIONMODULE\_PMPSTORECONTEXT**

## Property value

A  a context string used by Content Decryption Module (CDM) implementations.

## Remarks

The CDM implementer should look for this value and pass the value to the 
[MediaProtectionPMPServer constructor](/uwp/api/windows.media.protection.mediaprotectionpmpserver.-ctor) using the property name "Windows.Media.Protection.PMPStoreContext".


Apps should not create this property when calling [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 April 2020 Update<br/>                                     |
| Header<br/>                   | <dl> <dt>mfcontentdecryptionmodule.h</dt> </dl> |



## See also

- [Media Foundation Properties](media-foundation-properties.md)
- [MediaProtectionPMPServer](/uwp/api/windows.media.protection.mediaprotectionpmpserver)


 

 




