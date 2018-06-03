---
Description: Schannel uses CryptoAPI for cryptographic operations such as storing public/private keys.
ms.assetid: 5ad9a171-5f69-4035-aac5-ae8d27d0abfb
title: Schannel and CryptoAPI
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Schannel and CryptoAPI

Schannel uses [CryptoAPI](https://msdn.microsoft.com/windows/desktop/8ba85b5e-c80a-4781-a021-ac911b4fc7ca) for cryptographic operations such as storing [*public/private keys*](https://www.bing.com/search?q=*public/private keys*).

The following topics provide detailed information about how Schannel makes use of CryptoAPI.



| Topic                                                                   | Description                                                                                                          |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Certificate Stores](certificate-stores.md)<br/>                 | Both client and server certificates must be stored in a certificate store.<br/>                                |
| [CryptoAPI 2.0 Private Keys](cryptoapi-2-0-private-keys.md)<br/> | Schannel credentials are represented internally as [**CERT\_CONTEXT**](https://msdn.microsoft.com/windows/desktop/f0a3200e-6541-423d-a4a3-595a31026eea) structures.<br/> |



 

 

 




