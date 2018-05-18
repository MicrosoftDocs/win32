---
title: ProtectedFileOutputStream.create synchronous method
description: Synchronously creates a new ProtectedFileOutputStream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'E55677B6-FA72-4ACC-BF13-D56D5F5709FB'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectedFileOutputStream.create synchronous method"]
topic_type:
- apiref
api_name:
- ProtectedFileOutputStream.create synchronous method
api_type:
- NA
---

# ProtectedFileOutputStream.create synchronous method

Synchronously creates a new [**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md).

## Signature

``` syntax
public static ProtectedFileOutputStream create(
                                       final OutputStream outputStream,
                                       UserPolicy policy,
                                       String originalFileExtension,
                                       Context applicationContext)
                              throws ProtectionException
```

## Parameters



| Name                               | Datatype                                               | Notes                                                                                                                                                                                           |
|------------------------------------|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *outputStream*<br/>          | **OutputStream**<br/>                            | The **OutputStream** that will be converted into a [**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md)<br/>                                                         |
| *policy*<br/>                | [**UserPolicy**](userpolicy-class-java.md)<br/> | The policy needed to create the [**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md),<br/> If this parameter is null, a regular output stream is created.<br/> |
| *originalFileExtension*<br/> | **String**<br/>                                  |                                                                                                                                                                                                 |
| *applicationContext*<br/>    | **Context**<br/>                                 |                                                                                                                                                                                                 |



 

## Returns

[**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md)

## Throws

[**ProtectionException**](protectionexception-class-java.md)

## Defined in

ProtectedFileOutputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





