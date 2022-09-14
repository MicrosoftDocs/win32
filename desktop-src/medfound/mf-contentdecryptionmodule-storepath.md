---
description: Specifies a file path representing a storage location the Content Decryption Module (CDM) can use for initialization.
title: MF_CONTENTDECRYPTIONMODULE_STOREPATH (mfcontentdecryptionmodule.h)
ms.topic: reference
ms.date: 01/31/2020
---

# MF\_CONTENTDECRYPTIONMODULE\_STOREPATH property

Specifies a file path representing a storage location the Content Decryption Module (CDM) can use for initialization.


## Data type

**LPWSTR** (VT_LPWSTR)

## Property GUID

**MF\_CONTENTDECRYPTIONMODULE\_STOREPATH**

## Property value

A file path representing a storage location the Content Decryption Module (CDM) can use for initialization.

## Remarks

The path specified with this property will also be used for content-specific data if the [MF_CONTENTDECRYPTIONMODULE_INPRIVATESTOREPATH](mf-contentdecryptionmodule-inprivatestorepath.md) property isn't set.

To improve COM performance, the app should not delete the store location after the CDM object has been released.



Set this property when you create a CDM by calling [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 April 2020 Update<br/>                                     |
| Header<br/>                   | <dl> <dt>mfcontentdecryptionmodule.h</dt> </dl> |



## See also

- [Media Foundation Properties](media-foundation-properties.md)
- [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule)


 

 




