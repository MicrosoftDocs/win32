---
Description: Schannel uses CryptoAPI for cryptographic operations such as storing public/private keys.
ms.assetid: 5ad9a171-5f69-4035-aac5-ae8d27d0abfb
title: Schannel and CryptoAPI
ms.topic: article
ms.date: 05/31/2018
---

# Schannel and CryptoAPI

Schannel uses [CryptoAPI](https://msdn.microsoft.com/en-us/library/Aa380251(v=VS.85).aspx) for cryptographic operations such as storing [*public/private keys*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx).

The following topics provide detailed information about how Schannel makes use of CryptoAPI.



| Topic                                                                   | Description                                                                                                          |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Certificate Stores](certificate-stores.md)<br/>                 | Both client and server certificates must be stored in a certificate store.<br/>                                |
| [CryptoAPI 2.0 Private Keys](cryptoapi-2-0-private-keys.md)<br/> | Schannel credentials are represented internally as [**CERT\_CONTEXT**](https://msdn.microsoft.com/en-us/library/Aa377189(v=VS.85).aspx) structures.<br/> |



 

 

 




