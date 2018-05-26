---
title: CreationCallback T interface
description: An application implements a CreationCallback T .
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 10317c82-b99b-44d1-9417-d3991603b39d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CreationCallback T interface
topic_type:
- apiref
api_name:
- CreationCallback T interface
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreationCallback&lt;T&gt; interface

An application implements a **CreationCallback&lt;T&gt;** and passes it to the appropriate method in [**ProtectedFileInputStream**](protectedfileinputstream-class-java.md) when creating a new protected stream.

## Signature

``` syntax
public interface CreationCallback<T> extends ContextCallback
```

## Methods



| Name                                                                                                                | Description                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**getContext**](creationcallback-getcontext-method-java.md)<br/>                                            | Must return the current context in order to call context dependent operations. (e.g. accessing resources and opening UI elements)<br/> |
| [**onSuccess(T)**](creationcallback-t--onsuccess-t---method-java.md)<br/>                                    | Called upon successful creation of a protected stream.<br/>                                                                            |
| [**onFailure(ProtectionException)**](creationcallback-t--onfailure-protectionexception--method-java.md)<br/> | Called upon failure to create a protected stream.<br/>                                                                                 |
| [**onCancel**](creationcallback-t--oncancel-method-java.md)<br/>                                             | Called when the operation is canceled.<br/>                                                                                            |



 

## Defined in

CreationCallback.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





