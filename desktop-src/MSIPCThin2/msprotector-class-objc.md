---
title: MSProtector class
description: Enables you to encrypt or decrypt any chunk of data and manage the stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: FEE226D2-AA7E-474D-8D17-1E9130560E34
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtector class
topic_type:
- apiref
api_name:
- MSProtector class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSProtector class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Enables you to encrypt or decrypt any chunk of data and manage the stream.

## Signature

``` syntax
@interface MSProtector : NSObject
```

## Properties



| Name                                                                | Description                                         |
|---------------------------------------------------------------------|-----------------------------------------------------|
| [**blockSize**](msprotector-blocksize-property-objc.md)<br/> | Minimum block size decryption/encryption<br/> |



 

## Methods



| Name                                                                                                                                  | Description                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**initWithUserPolicy**](msprotector-initwithuserpolicy-method.md)<br/>                                                        | Used to initialize an **MSProtector** object with an [**MSUserPolicy**](msuserpolicy-interface-objc.md).<br/> |
| [**encryptAlignedBlocksWithStartingBlockNumber**](msprotector-encryptalignedblockswithstartingblocknumber-method-objc.md)<br/> | Used to encrypt a block of unencrypted data.<br/>                                                              |
| [**decryptAlignedBlocksWithStartingBlockNumber**](msprotector-decryptalignedblockswithstartingblocknumber-method-objc.md)<br/> | Used to decrypt a block of encrypted data.<br/>                                                                |



 

## Defined in

MSProtection.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 





 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





