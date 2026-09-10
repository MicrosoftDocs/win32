---
description: Use cryptographic technologies for public key encryption, encryption algorithms, RSA encryption, and digital certificates.
ms.assetid: c53af815-ee3f-417a-8e62-3a3689715bc6
title: Cryptography
ms.topic: concept-article
ms.date: 07/14/2025
---

# Cryptography

> [!IMPORTANT]
> **For new development, use [Cryptography API: Next Generation (CNG)](../SecCNG/cng-portal.md)** instead of CryptoAPI. CNG is the modern cryptographic API for Windows, available since Windows Vista and Windows Server 2008. It provides better security defaults, algorithm agility, and kernel-mode support. CryptoAPI is maintained for backward compatibility only. CAPICOM is obsolete and not supported on any currently supported version of Windows.

## Purpose

Cryptography is the use of codes to convert data so that only a specific recipient will be able to read it, using a key.

Microsoft cryptographic technologies include [Cryptography API: Next Generation (CNG)](../SecCNG/cng-portal.md) for new development, and the legacy CryptoAPI and Cryptographic Service Providers (CSP) for backward compatibility. Certificate and smart card enrollment, certificate management, and custom module development are also described.

## Developer audience

CryptoAPI is intended for use by developers of Windows-based applications that will enable users to create and exchange documents and other data in a secure environment, especially over nonsecure media such as the Internet. Developers should be familiar with the C and C++ programming languages and the Windows programming environment. Although not required, an understanding of cryptography or security-related subjects is advised.

> [!NOTE]
> CAPICOM is a legacy 32-bit COM component that was last supported on Windows XP and Windows Server 2003. It is not available on any currently supported version of Windows. Do not use CAPICOM in new applications. For alternatives, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).

## Run-time requirements

For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

## In this section



| Topic                                                           | Description                                                                                                                                                                                                                  |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Cryptography](about-cryptography.md)<br/>         | Key cryptography concepts and a high-level view of Microsoft cryptography technologies.<br/>                                                                                                                           |
| [Using Cryptography](using-cryptography.md)<br/>         | Cryptography processes, procedures, and extended samples of C and Visual Basic programs using CryptoAPI functions and CAPICOM objects.<br/>                                                                            |
| [Cryptography Reference](cryptography-reference.md)<br/> | Detailed descriptions of the Microsoft cryptography functions, interfaces, objects, structures, and other programming elements. Includes reference descriptions of the API for working with digital certificates.<br/> |



## Related content

- [Cryptography API: Next Generation (CNG)](../SecCNG/cng-portal.md) — the modern cryptographic API for new Windows development
- [Overview of typical CNG programming](../SecCNG/typical-cng-programming.md) — step-by-step guide to using CNG
- [Encrypting Data with CNG](../SecCNG/encrypting-data-with-cng.md) — modern encryption example using AES with CNG



 

 

 




