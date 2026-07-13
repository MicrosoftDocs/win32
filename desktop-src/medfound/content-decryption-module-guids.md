---
description: The following GUIDs support Content Decryption Module (CDM) implementations.
title: Content Decryption Module (CDM) GUIDs
ms.topic: reference
ms.date: 01/21/2018
---

# Content Decryption Module (CDM) GUIDs

The following GUIDs support Content Decryption Module (CDM) implementations.

**MF_CONTENTDECRYPTIONMODULE_SERVICE**

Service GUID used to obtain interfaces from an [IMFContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nn-mfcontentdecryptionmodule-imfcontentdecryptionmodule) implementation,such as the WinRT [IMediaProtectionPMPServer](/uwp/api/windows.media.protection.mediaprotectionpmpserver) interface. An implementation of **IMFContentDecryptionModule** should implement [IMFGetService](/windows/win32/api/mfidl/nn-mfidl-imfgetservice) and support this service GUID.


**MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATE**

The CLSID for instantiating a proxy object that implements [IMFActivate](/windows/win32/api/mfobjects/nn-mfobjects-imfactivate). Use this proxy object to instantiate and initialize an Encrypted Media Extension (EME) object in an external process. For more information on using this proxy, see [MF_ENCRYPTEDMEDIAEXTENSIONS_ACTIVATABLE_CLASS_ID](mf-encryptedmediaextensions_activatable_class_id.md) and [MF_ENCRYPTEDMEDIAEXTENSIONS_INITIALIZATION_DATA](mf-encryptedmediaextensions_initialization_data.md).

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>mfcontentdecryptionmodule.h</dt> </dl> |



## See also



- [Media Foundation Constants](media-foundation-constants.md)
- [IMFContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nn-mfcontentdecryptionmodule-imfcontentdecryptionmodule
- [IMediaProtectionPMPServer](/uwp/api/windows.media.protection.mediaprotectionpmpserver)
- [IMFGetService](/windows/win32/api/mfidl/nn-mfidl-imfgetservice)


 

 




