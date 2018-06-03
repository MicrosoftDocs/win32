---
title: ProtectionException(String, String, Throwable) constructor
description: Initializes a new instance of the ProtectionException class with the specified tag, message, and inner exception.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: b4e1de36-2adc-46cc-90e3-31caa64ef6b9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ProtectionException(String, String, Throwable) constructor
topic_type:
- apiref
api_name:
- ProtectionException(String, String, Throwable) constructor
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProtectionException(String, String, Throwable) constructor

Initializes a new instance of the [**ProtectionException**](protectionexception-class-java.md) class with the specified tag, message, and inner exception.

## Signature

``` syntax
public ProtectionException(String tag, String message, Throwable e)
```

## Parameters



| Name                 | Datatype                 | Notes                                                                                                                                                                                       |
|----------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *tag*<br/>     | **String**<br/>    | The tag for logging.<br/>                                                                                                                                                             |
| *message*<br/> | **String**<br/>    | The exception message.<br/>                                                                                                                                                           |
| *e*<br/>       | **Throwable**<br/> | The inner exception.<br/> If the inner exception is an [**ProtectionException**](protectionexception-class-java.md), its type will be the one used for the new exception.<br/> |



 

## Returns

[**ProtectionException**](protectionexception-class-java.md)

## Defined in

ProtectionException.java

 

 





