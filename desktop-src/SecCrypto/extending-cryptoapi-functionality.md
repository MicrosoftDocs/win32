---
Description: The future of cryptography and secure communications cannot easily be predicted.
ms.assetid: 41c1758d-1213-47a6-81d5-7755b41c3007
title: Extending CryptoAPI Functionality
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Extending CryptoAPI Functionality

The future of [*cryptography*](security.c_gly#-security-cryptography-gly) and secure communications cannot easily be predicted. New certificate types might emerge, various certificate extensions might find common usage, and new message types might be introduced. Because of this, extensibility is part of the design of key [*CryptoAPI*](security.c_gly#-security-cryptoapi-gly) functions.

The following sections present overviews on the use of OIDs for extending CryptoAPI functions.



| Topic                                                                              | Contents                                                                                                                            |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [OID Overview](oid-overview.md)                                                   | OID fundamental concepts.                                                                                                           |
| [Creating the New Functionality](creating-the-new-functionality.md)               | Creating OIDs and functions to extend the use of existing APIs.                                                                     |
| [Registering the New Functionality](registering-the-new-functionality.md)         | Setting up new OID-related functions.                                                                                               |
| [Installing the New Functionality](installing-the-new-functionality.md)           | Installing OID functions to memory to improve performance.                                                                          |
| [Extending CertOpenStore Functionality](extending-certopenstore-functionality.md) | Extending [**CertOpenStore**](/windows/win32/Wincrypt/nf-wincrypt-certopenstore?branch=master) functionality using installable or registered certificate-store-provider function. |



 

 

 



