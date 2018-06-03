---
title: MSProtector decryptAlignedBlocksWithStartingBlockNumber method
description: Used to decrypt a block of encrypted data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: DCF41EC8-F6A7-42A9-A111-4415118651F4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtector decryptAlignedBlocksWithStartingBlockNumber method
topic_type:
- apiref
api_name:
- MSProtector decryptAlignedBlocksWithStartingBlockNumber method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSProtector decryptAlignedBlocksWithStartingBlockNumber method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Used to decrypt a block of encrypted data.

## Signature

``` syntax
- (NSData *)decryptAlignedBlocksWithStartingBlockNumber:(NSUInteger)startingBlockNumber 
                                          encryptedData:(NSData *)encryptedData 
                                                isFinal:(BOOL)isFinal 
                                                  error:(NSError **)errorPtr;
```

## Parameters



| Name                             | Datatype                    | Notes                                                       |
|----------------------------------|-----------------------------|-------------------------------------------------------------|
| *startingBlockNumber*<br/> | **NSUInteger**<br/>   |                                                             |
| *encryptedData*<br/>       | **NSData** \*<br/>    |                                                             |
| *isFinal*<br/>             | **BOOL**<br/>         | Set to TRUE for the last block, otherwise FALSE.<br/> |
| *errorPtr*<br/>            | **NSError** \*\*<br/> |                                                             |



 

## Returns

Pointer to an **NSData** object containing the block of dencrypted data.

## Defined in

MSProtection.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

[**templateListWithUserId**](mstemplatedescriptor-templatelistwithuserid-userid-authenticationcallback-completionblock-method-objc.md) should be invoked from the main thread.

 

 





