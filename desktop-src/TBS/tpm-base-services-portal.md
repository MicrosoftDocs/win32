---
title: TPM Base Services
description: TPM software provides services as an API exposed through remote procedure call. Use TPM to create a TPM module.
ms.assetid: ae6e7fe9-585d-467a-8456-e008b8ea89a0
keywords:
- TPM Base Services TBS
- TPM Base Services TBS , home page
ms.topic: article
ms.date: 05/31/2018
---

# TPM Base Services

## Purpose

The Trusted Platform Module (TPM) Base Services (TBS) feature centralizes TPM access across applications.

The TBS feature runs as a system service in Windows Server 2008, Windows Vista, or newer operating systems. It provides services as an API exposed through remote procedure calls (RPC). The TBS feature uses priorities specified by calling applications to cooperatively schedule TPM access.

> [!Note]
>
> The TPM can be used for key storage operations. However, developers are encouraged to use the [Key Storage APIs](/windows/desktop/SecCNG/key-storage-and-retrieval) for these scenarios instead. The Key Storage APIs provide the functionality to create, sign or encrypt with, and persist cryptographic keys, and they are higher-level and easier to use than the TBS for these targeted scenarios.

 

## Developer audience

TBS is intended for use by developers of applications based on the Windows operating systems. Developers should be familiar with the C and C++ programming languages and the Microsoft Windows programming environment.

## Run-time requirements

The TBS feature requires at least Windows Server 2008 or Windows Vista operating system. For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

## In this section



| Topic                                         | Description                                                                     |
|-----------------------------------------------|---------------------------------------------------------------------------------|
| [About TBS](about-tbs.md)<br/>         | Key concepts and a high-level view of the TBS feature.<br/>               |
| [Using TBS](using-tbs.md)<br/>         | TBS processes and procedures for using the TBS API.<br/>                  |
| [TBS Reference](tbs-reference.md)<br/> | Documentation about the TBS functions, structures, and return codes.<br/> |



 

 

