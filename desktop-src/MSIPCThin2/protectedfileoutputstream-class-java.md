---
title: ProtectedFileOutputStream class
description: A class that represents a stream that can write a protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 9db17918-51a4-4503-bfe3-f0149f67cf8a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ProtectedFileOutputStream class
topic_type:
- apiref
api_name:
- ProtectedFileOutputStream class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProtectedFileOutputStream class

A class that represents a stream that can write a protected file.

## Signature

``` syntax
public abstract class ProtectedFileOutputStream extends OutputStream
```

**ProtectedFileOutputStream** extends Android's base class. For information on base class methods see, [OutputStream](http://developer.android.com/reference/java/io/OutputStream.mdl)

## Methods



| Name                                                                                               | Description                                                            |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**create asynchronous**](customprotectedoutputstream-create-method-java.md)<br/>           | Asynchronously creates a new **ProtectedFileOutputStream**.<br/> |
| [**create asynchronous**](protectedfileoutputstream-create-synchronous-method-java.md)<br/> | Synchronously creates a new **ProtectedFileOutputStream**.<br/>  |
| [**getUserPolicy**](protectedfileoutputstream-getuserpolicy-method-java.md)<br/>            | Returns the protection policy associated with the stream.<br/>   |



 

## Defined in

ProtectedFileOutputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Remarks

The **ProtectedFileOutputStream** class inherits from the **OutputStream** class. For more information about this class and the members it exposes, see the Android developer documentation.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





