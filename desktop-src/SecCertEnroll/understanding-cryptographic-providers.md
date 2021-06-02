---
description: Providers implement cryptographic algorithms, generate keys, provide key storage, and authenticate users. Providers can be implemented in hardware, software, or both.
ms.assetid: 42f76d22-1f0e-4e20-a19e-e5e926ab27f9
title: Understanding Cryptographic Providers
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Cryptographic Providers

The cryptographic provider concept that was introduced in Cryptography API ([*CryptoAPI*](/windows/desktop/SecGloss/c-gly)) and which evolved somewhat in [*Cryptography API: Next Generation*](/windows/desktop/SecGloss/c-gly) (CNG) is central to the secure implementation of cryptographic functionality on Microsoft operating systems. These two SDKs have been used to create many applications and are called internally by other SDKs. For example, Active Directory Certificate Services and the Certificate Enrollment API rely on CryptoAPI and CNG.

In general, providers implement cryptographic algorithms, generate keys, provide key storage, and authenticate users. Providers can be implemented in hardware, software, or both. Applications built by using CryptoAPI or CNG cannot alter the keys created by providers, and they cannot alter cryptographic algorithm implementation. The multiple providers created by Microsoft are distributed with the operating systems. Other providers have been created and distributed by third parties.

The following topics highlight the differences between providers associated with CryptoAPI and those associated with CNG. Typically, this documentation refers to providers without reference to the SDK with which they are associated, noting the association only when it is relevant.

-   [CryptoAPI Cryptographic Service Providers](cryptoapi-cryptographic-service-providers.md)
-   [CNG Cryptographic Algorithm Providers](cng-cryptographic-algorithm-providers.md)
-   [CNG Key Storage Providers](cng-key-storage-providers.md)
-   [Enumerating Installed Providers](enumerating-installed-providers.md)

## Related topics

<dl> <dt>

[Using the Certificate Enrollment API](about-the-certificate-enrollment-api.md)
</dt> </dl>

 

 
