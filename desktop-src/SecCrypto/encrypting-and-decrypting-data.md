---
description: When a document or text needs to have privacy protected by a single user or when the document is to be shared among a small group of people who all have access to the same secret password, simple encryption/decryption can be done.
ms.assetid: 68eefd24-c924-4dd1-8cb3-cc20106f9605
title: Encrypting and Decrypting Data
ms.topic: article
ms.date: 05/31/2018
---

# Encrypting and Decrypting Data

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

When a document or text needs to have privacy protected by a single user or when the document is to be shared among a small group of people who all have access to the same secret password, simple encryption/decryption can be done. CAPICOM does not support the PKCS \#7 EncryptedData content type but uses a non-standard ASN structure for EncryptedData. Therefore, only CAPICOM can decrypt a CAPICOM EncryptedData object.

The following sections show examples for encryption and decryption tasks:

-   [Encrypting a Message in CAPICOM](encrypting-a-message-in-capicom.md)
-   [Decrypting a Message in CAPICOM](decrypting-a-message-in-capicom.md)

 

 



