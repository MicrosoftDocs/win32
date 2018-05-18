---
title: ProtectedFileOutputStream.create asynchronous method
description: Asynchronously implements a wrapper of the output stream allowing writing of an RMS protected output stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '66E52329-A2C4-41B5-8D0A-BF382EB03C4F'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectedFileOutputStream.create asynchronous method"]
topic_type:
- apiref
api_name:
- ProtectedFileOutputStream.create asynchronous method
api_type:
- NA
---

# ProtectedFileOutputStream.create asynchronous method

Asynchronously implements a wrapper of the output stream allowing writing of an RMS protected output stream.

## Signature

``` syntax
public static IAsyncControl create(final OutputStream outputStream,
                                       UserPolicy policy,
                                       String originalFileExtension,
                                       final CreationCallback<ProtectedFileOutputStream> callback)
```

## Parameters



| Name                               | Datatype                                                                                                         | Notes                                                                                                                                                                                           |
|------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *outputStream*<br/>          | **InputStream**<br/>                                                                                       | The **OutputStream** that will be converted into a [**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md)<br/>                                                         |
| *policy*<br/>                | [**UserPolicy**](userpolicy-class-java.md)<br/>                                                           | The policy needed to create the [**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md),<br/> If this parameter is null, a regular output stream is created.<br/> |
| *originalFileExtension*<br/> | **String**<br/>                                                                                            |                                                                                                                                                                                                 |
| *callback*<br/>              | **CreationCallback**&lt;[**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md)&gt;<br/> |                                                                                                                                                                                                 |



 

## Returns

An [**IAsyncControl**](iasynccontrol-interface.md) object if an asynchronous operation is in progress else, null is returned.

## Throws

[**InvalidParameterException**](invalidparameterexception-class-java.md) if no callback is available that [**onFailure**](authenticationcompletioncallback-onfailure-method-java.md) can be called.

## Defined in

ProtectedFileOutputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





