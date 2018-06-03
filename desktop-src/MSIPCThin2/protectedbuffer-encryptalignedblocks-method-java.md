---
title: ProtectedBuffer.encryptAlignedBlocks method
description: Encrypts aligned blocks of data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: DE11C78E-06F0-4C09-8BE7-EA239546CB05
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ProtectedBuffer.encryptAlignedBlocks method
topic_type:
- apiref
api_name:
- ProtectedBuffer.encryptAlignedBlocks method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProtectedBuffer.encryptAlignedBlocks method

Encrypts aligned blocks of data. Use [**getBlockSize**](protectedbuffer-getblocksize-method-java.md) to retrieve the minimum block size. Valid data will be written to the *outputBuffer* from the position up to the limit index.

If this method does not receive aligned blocks an exception will be thrown.

## Signature

``` syntax
public int encryptAlignedBlocks(
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
| *inputBuffer*<br/>         | **ByteBuffer**<br/> | Unencrypted data \[position, limit\]<br/>                    |
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



 

 

 





