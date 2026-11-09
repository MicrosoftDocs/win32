---
description: Specifies a SHA-256 hash of an origin ID that identifies the source of content for a Content Decryption Module (CDM).
title: MF_CONTENTDECRYPTIONMODULE_ORIGINID (mfcontentdecryptionmodule.h)
ms.topic: reference
ms.date: 11/04/2026
---

# MF_CONTENTDECRYPTIONMODULE_ORIGINID property

Specifies a SHA-256 hash of an origin ID that identifies the source of content for a Content Decryption Module (CDM).

## Data type

**VT_BLOB**

## Property key

**MF_CONTENTDECRYPTIONMODULE_ORIGINID**

This constant is a **PROPERTYKEY**.

## Property value

A binary blob containing the SHA-256 hash of the origin ID. The origin ID is a UTF-8 string that specifies the content's domain.

Calculate the hash over every byte of the UTF-8 string except the terminating null byte. The hash must be deterministic and calculated without a nonce, so that the same domain produces the same hash.

## Remarks

Set this property on the [IPropertyStore](/windows/win32/api/propsys/nn-propsys-ipropertystore) that you pass to [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule).

To set the property, call [IPropertyStore::SetValue](/windows/win32/api/propsys/nf-propsys-ipropertystore-setvalue) with **MF_CONTENTDECRYPTIONMODULE_ORIGINID** as the property key and a **PROPVARIANT** whose **vt** member is **VT_BLOB**. Set **blob.cbSize** to the size of the hash and **blob.pBlobData** to the hash bytes.

The CDM uses the origin ID when establishing the client ID for the license.

## Requirements

| Requirement | Value |
| --- | --- |
| Header | mfcontentdecryptionmodule.h |

## See also

- [Media Foundation Properties](media-foundation-properties.md)
- [IMFContentDecryptionModuleAccess::CreateContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nf-mfcontentdecryptionmodule-imfcontentdecryptionmoduleaccess-createcontentdecryptionmodule)
