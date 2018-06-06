---
Description: With Hash and Digital Signature Functions, a user can digitally sign data so that any other user can verify that the data has not been changed since it was signed. The identity of the user who signed the data can also be verified.
ms.assetid: dbe70506-f0d9-4239-a3af-8494fd6d4149
title: Hashes and Digital Signatures
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Hashes and Digital Signatures

With [Hash and Digital Signature Functions](cryptography-functions.md#hash-and-digital-signature-functions), a user can digitally sign data so that any other user can verify that the data has not been changed since it was signed. The identity of the user who signed the data can also be verified.

A [*digital signature*](security.d_gly#-security-digital-signature-gly) consists of a small amount of binary data, typically less than 256 bytes. This signature can be bundled with the signed message or stored separately, depending on how a particular application has been implemented.

The Microsoft Strong Cryptographic Provider creates digital signatures that conform to the RSA [*Public Key Cryptography Standards*](security.p_gly#-security-public-key-cryptography-standards-gly) (PKCS) \#1.

 

 



