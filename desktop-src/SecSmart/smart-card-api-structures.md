---
title: Smart Card API Structures
description: The following structures are used by the smart card functions.
ms.assetid: e647fa49-a355-4c55-8919-fdc3b898e2ce
keywords:
- Smart Card API Smart Card , structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Smart Card API Structures

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The following structures are used by the smart card functions.

## Smart Card Module Structures

The following structures are used with smart card module functions.



| Structure                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CARD\_CAPABILITIES**](card-capabilities.md)             | Contains information about the capabilities of a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).<br/>                                                                                                                                                                                                                                                                                                                                                 |
| [**CARD\_DATA**](card-data.md)                             | Contains context information used during communication between a smart card module and the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md). The information contained by the structure includes function pointers for all of the functions implemented by the smart card module and for the functions that the Microsoft Base Smart Card Cryptographic Service Provider exports to the smart card module.<br/> |
| [**CARD\_DERIVE\_KEY**](card-derive-key.md)                | Contains the *key derivation function* (KDF) that the [**CardDeriveKey**](cardderivekey.md) function uses to derive a session key and receives the derived key on output.<br/>                                                                                                                                                                                                                                                                                                         |
| [**CARD\_DH\_AGREEMENT\_INFO**](card-dh-agreement-info.md) | Not currently supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**CARD\_FILE\_INFO**](card-file-info.md)                  | Contains information about a file on a smart card.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**CARD\_FREE\_SPACE\_INFO**](card-free-space-info.md)     | Contains information about the amount of available memory on a smart card.<br/>                                                                                                                                                                                                                                                                                                                                                                                                         |
| [**CARD\_KEY\_SIZES**](card-key-sizes.md)                  | Contains information about the [*key lengths*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-length-gly) supported by a smart card.<br/>                                                                                                                                                                                                                                                                                                                                        |
| [**CARD\_RSA\_DECRYPT\_INFO**](card-rsa-decrypt-info.md)   | Specifies the data to be encrypted by the [**CardRSADecrypt**](cardrsadecrypt.md) function as well as the private key used to perform the decryption.<br/>                                                                                                                                                                                                                                                                                                                             |
| [**CARD\_SIGNING\_INFO**](card-signing-info.md)            | Specifies data to be signed by a call to the [**CardSignData**](cardsigndata.md) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                        |
| [**CONTAINER\_INFO**](container-info.md)                   | Contains information about a key container on a smart card.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                        |



 

 

 





