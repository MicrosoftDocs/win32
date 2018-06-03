---
title: CustomProtectedOutputStream.create asynchronous method
description: Asynchronously creates an OutputStream for writing protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: FE3A1E48-5929-40EA-8DC9-7B1C40C0D4CC
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CustomProtectedOutputStream.create asynchronous method
topic_type:
- apiref
api_name:
- CustomProtectedOutputStream.create asynchronous method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CustomProtectedOutputStream.create asynchronous method

Asynchronously creates an **OutputStream** for writing protected content.

This method is asynchronous as it may require server client communication.

When publishing content your app is required to call **CustomProtectedOutputStream.close** after it is finished writing the content to the [**CustomProtectedOutputStream**](customprotectedoutputstream-class-java.md). If the flush() is not called we cannot guarantee that all the encrypted data is stored to the backing stream.

## Signature

``` syntax
public static IAsyncControl create(OutputStream backingOutputStream,
                                       UserPolicy userPolicy,
                                       CreationCallback<CustomProtectedOutputStream> callback)
            throws InvalidParameterException
```

## Parameters



| Name                             | Datatype                                                                                                         | Notes |
|----------------------------------|------------------------------------------------------------------------------------------------------------------|-------|
| *backingOutputStream*<br/> | **OutputStream**<br/>                                                                                      |       |
| *userPolicy*<br/>          | [**UserPolicy**](userpolicy-class-java.md)<br/>                                                           |       |
| *callback*<br/>            | CreationCallback&lt;[**CustomProtectedOutputStream**](customprotectedoutputstream-class-java.md)&gt;<br/> |       |



 

## Returns

[**IAsyncControl**](iasynccontrol-interface.md) if an async operation is in progress else null is returned.

## Throws

[**InvalidParameterException**](invalidparameterexception-class-java.md) if no callback is available that onFailure can be called.

## Defined in

CustomProtectedOutputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





