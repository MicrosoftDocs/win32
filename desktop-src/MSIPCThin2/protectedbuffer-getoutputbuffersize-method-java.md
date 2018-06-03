---
title: ProtectedBuffer.getOutputBufferSize method
description: Gets the required minimum output buffer size, in bytes, for the operation.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 03C96B2B-6EC2-4490-B925-3B5C19FBED1B
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ProtectedBuffer.getOutputBufferSize method
topic_type:
- apiref
api_name:
- ProtectedBuffer.getOutputBufferSize method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProtectedBuffer.getOutputBufferSize method

Gets the required minimum output buffer size, in bytes, for the operation.

## Signature

``` syntax
public int getOutputBufferSize(
                                  int startingBlockNumber, 
                                  ByteBuffer inputBuffer, 
                                  boolean isEncrypt, 
                                  boolean isFinal) 
                              throws ProtectionException
```

## Parameters



| Name                             | Datatype                  | Notes                                                                                                                                                      |
|----------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *startingBlockNumber*<br/> | **int**<br/>        | The first block<br/>                                                                                                                                 |
| *inputBuffer*<br/>         | **ByteBuffer**<br/> | Encrypted data \[position, limit\]<br/>                                                                                                              |
| *isEncrypt*<br/>           | **boolean**<br/>    | Set to **true** if the buffer is going to be used for encryption.<br/> Set to **false** if the buffer is going to be used for decryption.<br/> |
| *isFinal*<br/>             | **boolean**<br/>    | Set to **true** for processing the final chunk of data.<br/>                                                                                         |



 

## Returns

An **int**, indicating the output buffer size in bytes.

## Defined in

ProtectedBuffer.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





