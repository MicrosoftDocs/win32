---
title: FailedAuthenticationException(String, String, ProtectionException) constructor
description: Constructs a new authentication exception, FailedAuthenticationException class with a default message and tag a user id, challenge string and the previous exception.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 4A8A6CF3-059E-4EE2-AEE9-772051DB0FBC
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- FailedAuthenticationException(String, String, ProtectionException) constructor
topic_type:
- apiref
api_name:
- FailedAuthenticationException(String, String, ProtectionException) constructor
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FailedAuthenticationException(String, String, ProtectionException) constructor

Constructs a new authentication exception, [**FailedAuthenticationException**](failedauthenticationexception-class-java.md) class with a default message and tag a user id, challenge string and the previous exception.

## Signature

``` syntax
public FailedAuthenticationException(String userId, String challenge, 
                             ProtectionException e)
```

## Parameters



| Name                   | Datatype                                                                 | Notes                                                        |
|------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------|
| *userId*<br/>    | **String**<br/>                                                    | Id of the user the token was issued to.<br/>           |
| *challenge*<br/> | **String**<br/>                                                    | Challenge string used to generate the Id.<br/>         |
| *e*<br/>         | [**ProtectionException**](protectionexception-class-java.md)<br/> | The previous exception that this exception wraps.<br/> |



 

## Returns

[**FailedAuthenticationException**](failedauthenticationexception-class-java.md)

## Defined in

FailedAuthenticationException.java

 

 





