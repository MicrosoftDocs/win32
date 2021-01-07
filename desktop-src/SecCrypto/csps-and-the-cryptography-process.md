---
description: CryptoAPI functions use cryptographic service providers (CSPs) to perform encryption and decryption, and to provide key storage and security.
ms.assetid: 7977e59b-7ce1-4bb4-aae4-d67b7d646493
title: CSPs and the Cryptography Process
ms.topic: article
ms.date: 05/31/2018
---

# CSPs and the Cryptography Process

[*CryptoAPI*](../secgloss/c-gly.md) functions use [*cryptographic service providers*](../secgloss/c-gly.md) (CSPs) to perform encryption and decryption, and to provide key storage and security. These CSPs are independent modules. Ideally, CSPs are written to be independent of a particular application, so that any application will run with a variety of CSPs. In reality, however, some applications have specific requirements that require a customized CSP. This compares to the Windows [*GDI*](../secgloss/g-gly.md) model. CSPs are analogous to graphics device drivers.

The quality of protection for keys within the system is a design parameter of the CSP and not of the system as a whole. This allows an application to run in a variety of security contexts without modification.

The access applications have to the cryptographic internals is carefully restricted. This facilitates secure and portable application development.

The following three design rules apply:

-   Applications cannot directly access keying material. Because all keying material is generated within the CSP and used by the application through opaque handles, there is no risk of an application or its associated DLLs either divulging keying material or choosing keying material from poor random sources.
-   Applications cannot specify the details of cryptographic operations. The CSP interface allows an application to choose an encryption or signature algorithm, but the implementation of every cryptographic operation is done by the CSP.
-   Applications do not handle user [*credentials*](../secgloss/c-gly.md) or other user authentication data. User authentication is done by the CSP; therefore, future CSPs with advanced authentication capabilities, such as biometric inputs, will function without needing to change the application authentication model.

At a minimum, a CSP consists of a dynamic-link library (DLL) and a [*signature file*](../secgloss/s-gly.md). The signature file is necessary to ensure that the [*CryptoAPI*](../secgloss/c-gly.md) recognizes the CSP. CryptoAPI validates this signature periodically to ensure that any tampering with the CSP is detected.

Some CSPs can implement a fraction of their functionality in an address-separated service called through local RPC or in hardware called through a system device driver. Isolating global key-state and central cryptographic operations in an address-separated service or in hardware keeps keys and operations safe from tampering within an application data space.

It is unwise for applications to take advantage of attributes particular to a specific CSP. For example, the Microsoft Base Cryptographic Provider (supplied with CryptoAPI) supports 40-bit session keys and 512-bit public keys. Applications manipulating these keys must avoid assumptions about the amount of memory needed to store these keys because the application is likely to fail if a different CSP is used. Well-written applications must work with a variety of CSPs.

For details about cryptographic provider types and predefined CSPs that can be used with CryptoAPI, see [Cryptographic Provider Types](cryptographic-provider-types.md) and [Microsoft Cryptographic Service Providers](microsoft-cryptographic-service-providers.md).

 

 
