---
description: Use cryptographic technologies for public key encryption, encryption algorithms, RSA encryption, and digital certificates.
ms.assetid: c53af815-ee3f-417a-8e62-3a3689715bc6
title: Cryptography
ms.topic: article
ms.date: 05/31/2018
---

# Cryptography

## Purpose

Cryptography is the use of codes to convert data so that only a specific recipient will be able to read it, using a key.

Microsoft cryptographic technologies include CryptoAPI, Cryptographic Service Providers (CSP), CryptoAPI Tools, CAPICOM, WinTrust, issuing and managing certificates, and developing customizable public key infrastructures. Certificate and smart card enrollment, certificate management, and custom module development are also described.

## Developer audience

CryptoAPI is intended for use by developers of Windows-based applications that will enable users to create and exchange documents and other data in a secure environment, especially over nonsecure media such as the Internet. Developers should be familiar with the C and C++ programming languages and the Windows programming environment. Although not required, an understanding of cryptography or security-related subjects is advised.

CAPICOM is a 32-bit only component that is intended for use by developers who are creating applications using Visual Basic Scripting Edition (VBScript) programming language or the C++ programming language. CAPICOM is available for use in the operating systems specified in Run-Time Requirements. For future development, we recommend that you use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).

## Run-time requirements

For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

CAPICOM 2.1.0.2 is supported on the following operating systems and versions:

-   Windows Server 2003
-   Windows XP

CAPICOM is available as a redistributable file that can be downloaded from Platform SDK Redistributable: CAPICOM.

Certificate Services requires the following versions of these operating systems:

-   Windows Server 2008 R2
-   Windows Server 2008
-   Windows Server 2003

## In this section



| Topic                                                           | Description                                                                                                                                                                                                                  |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Cryptography](about-cryptography.md)<br/>         | Key cryptography concepts and a high-level view of Microsoft cryptography technologies.<br/>                                                                                                                           |
| [Using Cryptography](using-cryptography.md)<br/>         | Cryptography processes, procedures, and extended samples of C and Visual Basic programs using CryptoAPI functions and CAPICOM objects.<br/>                                                                            |
| [Cryptography Reference](cryptography-reference.md)<br/> | Detailed descriptions of the Microsoft cryptography functions, interfaces, objects, structures, and other programming elements. Includes reference descriptions of the API for working with digital certificates.<br/> |



 

 

 




