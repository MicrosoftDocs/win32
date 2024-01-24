---
description: Lists the changes to the capabilities for enveloping data.
ms.assetid: b025a9c6-d6a3-40b2-9b7f-1e6caa706b59
title: Enveloped Data Additions
ms.topic: article
ms.date: 05/31/2018
---

# Enveloped Data Additions

The following changes have been made to enveloped data capabilities:

-   Recipient identification can be done not only by Issuer and Serial Number (PKCS \#7 1.5), but also by Key Identifier.
-   Three recipient key exchange choices are provided:
    -   Key Transport using RSA keys.
    -   Key Agreement using either Ephemeral-Static Diffie-Hellman algorithm keys wrapped with 3DES or RC2, or Ephemeral-Static Elliptic Curve Diffie-Hellman algorithm keys wrapped with AES.
    -   Key Encryption Key or Mail List key transfer where the key used to encrypt the content encryption key has already been distributed to the recipients. RC2, 3DES and AES are allowed as key-wrapping algorithms.
-   Unprotected attributes can be included in the message.
-   An **OriginatorInfo** field that contains information about the originator has been added that can contain certificates and CRLs.
-   Elliptic Curve Cryptography (ECC) based algorithms and AES require Windows Vista or later.

 

 



