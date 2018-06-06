---
Description: The Microsoft Base Cryptographic Provider is the initial cryptographic service provider (CSP) provider, and is distributed with CryptoAPI versions 1.0 and 2.0. It is a general-purpose provider that supports digital signatures and data encryption.
ms.assetid: c36025c5-a407-4a05-8780-23f8107730df
title: Microsoft Base Cryptographic Provider
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Base Cryptographic Provider

The Microsoft Base Cryptographic Provider is the initial [*cryptographic service provider*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CSP) provider, and is distributed with [*CryptoAPI*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) versions 1.0 and 2.0. It is a general-purpose provider that supports [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) and data encryption.

The RSA public key algorithm is used for all public key operations.

To maintain backward compatibility with earlier versions the new version of the provider retains the version 1.0 designation of the name in Wincrypt.h. However, version 2.0 of this provider is currently shipping. To determine the actual version of the provider in use, call [**CryptGetProvParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetprovparam) with the *dwParam* argument set to **PP\_VERSION**. If 0x0200 is returned in *pbData*, then you have version 2.0.

|                |                     |
|----------------|---------------------|
| Provider type: | **PROV\_RSA\_FULL** |
| Provider name: | **MS\_DEF\_PROV**   |



 

 

 



