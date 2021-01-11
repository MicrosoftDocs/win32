---
description: Specifies a file path representing a storage location the Content Decryption Module (CDM) can use for content-specific data.
title: MF_CONTENTDECRYPTIONMODULE_INPRIVATESTOREPATH (mfcontentdecryptionmodule.h)
ms.topic: reference
ms.date: 01/31/2020
---

# MF\_CONTENTDECRYPTIONMODULE\_INPRIVATESTOREPATH property

Specifies a file path representing a storage location the Content Decryption Module (CDM) can use for content-specific data.


## Data type

**LPWSTR** (VT_LPWSTR)

## Property GUID

**MF\_CONTENTDECRYPTIONMODULE\_INPRIVATESTOREPATH**

## Property value

A file path representing a storage location the Content Decryption Module (CDM) can use for content-specific data.

## Remarks

The app should delete the store location after the CDM object has been released.

If this property isn't set, the system will use the path specified with the [MF_CONTENTDECRYPTIONMODULE_STOREPATH](mf-contentdecryptionmodule-storepath.md) property for content-specific data.

Set this property when you create a CDM by calling [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 April 2020 Update<br/>                                     |
| Header<br/>                   | <dl> <dt>mfcontentdecryptionmodule.h</dt> </dl> |



## See also

- [Media Foundation Properties](media-foundation-properties.md)
- [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule)


 

 




