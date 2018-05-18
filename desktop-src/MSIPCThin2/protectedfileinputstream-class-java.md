---
title: ProtectedFileInputStream class
description: Implements a wrapper of the input stream allowing reading of an RMS protected input stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'd0042f09-287b-4957-9efb-cb67eb717a3f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectedFileInputStream class"]
topic_type:
- apiref
api_name:
- ProtectedFileInputStream class
api_type:
- NA
---

# ProtectedFileInputStream class

Implements a wrapper of the input stream allowing reading of an RMS protected input stream.

## Signature

``` syntax
public abstract class ProtectedFileInputStream extends InputStream
```

**ProtectedFileInputStream** extends Android's base class. For information on base class methods see, [InputStream](http://developer.android.com/reference/java/io/InputStream.mdl)

## Methods



| Name                                                                                                         | Description                                                                                              |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**create asynchronous**](customprotectedinputstream-create-method-java.md)<br/>                      | Asynchronously creates a **ProtectedFileInputStream** object from an existing protected file.<br/> |
| [**create synchronous**](protectedfileinputstream-create-synchronous-method.md)<br/>                  | Synchronously creates a **ProtectedFileInputStream** object from an existing protected file.<br/>  |
| [**getOriginalFileExtension**](protectedfileinputstream-getoriginalfileextension-method-java.md)<br/> | Gets the original file extension of the file before it was protected<br/>                          |
| [**getUserPolicy**](protectedfileinputstream-getuserpolicy-method-java.md)<br/>                       | Returns the protection policy associated with the stream.<br/>                                     |



 

## Defined in

ProtectedFileInputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Remarks

The **ProtectedFileInputStream** class inherits from the **InputStream** class. For more information about this class and the members it exposes, see the Android developer documentation.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





