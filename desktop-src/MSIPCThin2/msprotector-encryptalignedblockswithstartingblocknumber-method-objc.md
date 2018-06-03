---
title: MSProtector encryptAlignedBlocksWithStartingBlockNumber method
description: Used to encrypt a block of unencrypted data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: F8125664-C274-4C35-9BDD-F05A850AB256
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtector encryptAlignedBlocksWithStartingBlockNumber method
topic_type:
- apiref
api_name:
- MSProtector encryptAlignedBlocksWithStartingBlockNumber method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSProtector encryptAlignedBlocksWithStartingBlockNumber method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Used to encrypt a block of unencrypted data.

## Signature

``` syntax
- (NSData *)encryptAlignedBlocksWithStartingBlockNumber:(NSUInteger)startingBlockNumber 
                                        unEncryptedData:(NSData *)unEncryptedData 
                                                isFinal:(BOOL)isFinal 
                                                  error:(NSError **)errorPtr;
```

## Parameters



| Name                             | Datatype                    | Notes                                                       |
|----------------------------------|-----------------------------|-------------------------------------------------------------|
| *startingBlockNumber*<br/> | **NSUInteger**<br/>   |                                                             |
| *unEncryptedData*<br/>     | **NSData** \*<br/>    |                                                             |
| *isFinal*<br/>             | **BOOL**<br/>         | Set to TRUE for the last block, otherwise FALSE.<br/> |
| *errorPtr*<br/>            | **NSError** \*\*<br/> |                                                             |



 

## Returns

Pointer to an **NSData** object containing the block of encrypted data.

## Defined in

MSProtection.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

[**templateListWithUserId**](mstemplatedescriptor-templatelistwithuserid-userid-authenticationcallback-completionblock-method-objc.md) should be invoked from the main thread.

 

 





