---
description: Specifies the algorithm used for signing, enveloping, and encrypting operations.
ms.assetid: 9a3071a3-e62d-43d3-acd7-0685592c78b4
title: Algorithm object (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Algorithm
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Algorithm object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**AlgorithmIdentifier Class**](/dotnet/api/system.security.cryptography.pkcs.algorithmidentifier?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography.Pkcs**](/dotnet/api/system.security.cryptography.pkcs?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Algorithm** object specifies the algorithm used for signing, enveloping, and encrypting operations.

## When to use

The **Algorithm** object is used to perform the following tasks:

-   Set or retrieve the algorithm to be used.
-   Set or retrieve the key length.

> [!Note]  
> CAPICOM attempts to use the system default cryptographic service provider (CSP). If that CSP cannot provide the requested algorithm or key length, CAPICOM searches for an available Microsoft-provided CSP that can handle the requested algorithm and key length, in this order of availability: Microsoft Enhanced Cryptographic Provider, Microsoft Strong Cryptographic Provider, Microsoft Base Cryptographic Provider.

 

## Members

The **Algorithm** object has these types of members:

-   [Properties](#properties)

### Properties

The **Algorithm** object has these properties.



| Property                                            | Access type           | Description                                                                                                                       |
|:----------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**KeyLength**](algorithm-keylength.md)<br/> | Read/write<br/> | Sets or retrieves the length of the key.<br/>                                                                               |
| [**Name**](algorithm-name.md)<br/>           | Read/write<br/> | Sets or retrieves the algorithm used for signing, enveloping, and encrypting operations. This is the default property.<br/> |



 

## Remarks

The **Algorithm** object cannot be created.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| Header<br/>                | <dl> <dt>Capicom.h</dt> </dl>   |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
