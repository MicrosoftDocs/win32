---
title: CustomProtectedOutputStream class
description: Implements a wrapper of the input stream allowing writing of a custom RMS protected output stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '3DC4E885-CCA4-4EE1-888F-C6872EF6743F'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CustomProtectedOutputStream class"]
topic_type:
- apiref
api_name:
- CustomProtectedOutputStream class
api_type:
- NA
---

# CustomProtectedOutputStream class

Implements a wrapper of the input stream allowing writing of a custom RMS protected output stream. Custom denotes that the class is more configurable than the base output stream.

## Signature

``` syntax
public class CustomProtectedOutputStream extends OutputStream
```

**CustomProtectedOutputStream** extends Android's base class. For information on base class methods see, [OutputStream](http://developer.android.com/reference/java/io/OutputStream.mdl).

## Methods



| Name                                                                                                              | Description                                                                          |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**create asynchronous**](customprotectedoutputstream-create-method-java.md)<br/>                          | Asynchronously creates an **OutputStream** for reading protected content.<br/> |
| [**create synchronous**](customprotectedoutputstream-create-synchronous-method.md)<br/>                    | Synchronously creates an **OutputStream** for reading protected content.<br/>  |
| [**getEncryptedContentLength**](customprotectedoutputstream-getencryptedcontentlength-method-java.md)<br/> | Gets the calculated size of the encrypted content.<br/>                        |
| [**getUserPolicy**](customprotectedoutputstream-getuserpolicy-method-java.md)<br/>                         | Gets the user policy associated with the stream.<br/>                          |



 

## Defined in

CustomProtectedOutputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





