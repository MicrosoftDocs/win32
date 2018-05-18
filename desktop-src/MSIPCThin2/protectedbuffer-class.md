---
title: ProtectedBuffer class
description: Used to process a protected buffer.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'C88245B9-0ECE-419A-96CF-FC23D3CCAF63'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectedBuffer class"]
topic_type:
- apiref
api_name:
- ProtectedBuffer class
api_type:
- NA
---

# ProtectedBuffer class

Used to process a protected buffer

## Signature

``` syntax
public class ProtectedBuffer
```

## Methods



| Name                                                                                        | Description                                                                                 |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**create**](protectedbuffer-create-method-java.md)<br/>                             | Creates **ProtectedBuffer** using a [**UserPolicy**](userpolicy-class-java.md).<br/> |
| [**getBlockSize**](protectedbuffer-getblocksize-method-java.md)<br/>                 | Gets the minimum block size that decryption and encryption calls should use.<br/>     |
| [**getOutputBufferSize**](protectedbuffer-getoutputbuffersize-method-java.md)<br/>   | Gets the required minimum output buffer size, in bytes, for the operation.<br/>       |
| [**decryptAlignedBlocks**](protectedbuffer-decryptalignedblocks-method-java.md)<br/> | Decrypts aligned blocks of data.<br/>                                                 |
| [**encryptAlignedBlocks**](protectedbuffer-encryptalignedblocks-method-java.md)<br/> | Encrypts aligned blocks of data.<br/>                                                 |



 

## Defined in

ProtectedBuffer.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





