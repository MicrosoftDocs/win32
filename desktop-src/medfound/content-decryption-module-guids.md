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


## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>mfcontentdecryptionmodule.h</dt> </dl> |



## See also



- [Media Foundation Constants](media-foundation-constants.md)
- [IMFContentDecryptionModule](/windows/win32/api/mfcontentdecryptionmodule/nn-mfcontentdecryptionmodule-imfcontentdecryptionmodule
- [IMediaProtectionPMPServer](/uwp/api/windows.media.protection.mediaprotectionpmpserver)
- [IMFGetService](/windows/win32/api/mfidl/nn-mfidl-imfgetservice)


 

 




