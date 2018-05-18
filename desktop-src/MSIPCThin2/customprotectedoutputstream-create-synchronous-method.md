---
title: CustomProtectedOutputStream.create synchronous method
description: Synchronously creates an OutputStream for writing protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '46AE2AEF-C331-40CA-B1A9-B3077BB76662'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CustomProtectedOutputStream.create synchronous method"]
topic_type:
- apiref
api_name:
- CustomProtectedOutputStream.create synchronous method
api_type:
- NA
---

# CustomProtectedOutputStream.create synchronous method

Synchronously creates an **OutputStream** for writing protected content.

This method is synchronous and it may require server client communication.

When publishing content your app is required to call **CustomProtectedOutputStream.close** after it is finished writing the content to the [**CustomProtectedOutputStream**](customprotectedoutputstream-class-java.md). If the flush() is not called we cannot guarantee that all the encrypted data is stored to the backing stream.

## Signature

``` syntax
public static CustomProtectedOutputStream create(
                                       OutputStream backingOutputStream,
                                       UserPolicy userPolicy,
                                       Context applicationContext)
                             throws ProtectionException
```

## Parameters



| Name                             | Datatype                                               | Notes                                                                                                            |
|----------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| *backingOutputStream*<br/> | **OutputStream**<br/>                            |                                                                                                                  |
| *userPolicy*<br/>          | [**UserPolicy**](userpolicy-class-java.md)<br/> | Policy needed to create the [**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md)<br/> |
| *applicationContext*<br/>  | **Context**<br/>                                 |                                                                                                                  |



 

## Returns

[**CustomProtectedOutputStream**](customprotectedoutputstream-class-java.md)

## Throws

[**ProtectionException**](protectionexception-class-java.md). In the case of a consent / authentication cancellation a **UserCancellationException** is thrown.

## Defined in

CustomProtectedOutputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





