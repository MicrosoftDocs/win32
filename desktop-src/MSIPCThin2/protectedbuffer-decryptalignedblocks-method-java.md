---
title: ProtectedBuffer.decryptAlignedBlocks method
description: Decrypts aligned blocks of data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '591C03E7-D937-49B7-A5EE-40C22D19FF93'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectedBuffer.decryptAlignedBlocks method"]
topic_type:
- apiref
api_name:
- ProtectedBuffer.decryptAlignedBlocks method
api_type:
- NA
---

# ProtectedBuffer.decryptAlignedBlocks method

Decrypts aligned blocks of data. Use [**getBlockSize**](protectedbuffer-getblocksize-method-java.md) to retrieve the minimum block size. Valid data will be written to the *outputBuffer* from the position up to the limit index.

If this method does not receive aligned blocks an exception will be thrown.

## Signature

``` syntax
public int decryptAlignedBlocks(
                                  int startingBlockNumber, 
                                  ByteBuffer inputBuffer, 
                                  ByteBuffer outputBuffer, 
                                  boolean isFinal) 
                              throws ProtectionException
```

## Parameters



| Name                             | Datatype                  | Notes                                                              |
|----------------------------------|---------------------------|--------------------------------------------------------------------|
| *startingBlockNumber*<br/> | **int**<br/>        | The first block<br/>                                         |
| *inputBuffer*<br/>         | **ByteBuffer**<br/> | Encrypted data \[position, limit\]<br/>                      |
| *outputBuffer*<br/>        | **ByteBuffer**<br/> | Buffer required for decryption<br/>                          |
| *isFinal*<br/>             | **boolean**<br/>    | Set to **true** for processing the final chunk of data.<br/> |



 

## Returns

An **int** indicating the number of bytes actually written.

## Throws

[**ProtectionException**](protectionexception-class-java.md)

## Defined in

ProtectedBuffer.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





