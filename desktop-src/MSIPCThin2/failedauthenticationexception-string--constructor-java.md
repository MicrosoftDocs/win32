---
title: FailedAuthenticationException(String, String) constructor
description: Constructs a new authentication exception, FailedAuthenticationException class with a default message and tag, and a user id and challenge string.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'CAE502BF-BF1C-45D3-8A12-8D3415A043E9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["FailedAuthenticationException(String, String) constructor"]
topic_type:
- apiref
api_name:
- FailedAuthenticationException(String, String) constructor
api_type:
- NA
---

# FailedAuthenticationException(String, String) constructor

Constructs a new authentication exception, [**FailedAuthenticationException**](failedauthenticationexception-class-java.md) class with a default message and tag, and a user id and challenge string.

## Signature

``` syntax
public FailedAuthenticationException(String userId, String challenge)
```

## Parameters



| Name                   | Datatype              | Notes                                                |
|------------------------|-----------------------|------------------------------------------------------|
| *userId*<br/>    | **String**<br/> | Id of the user the token was issued to.<br/>   |
| *challenge*<br/> | **String**<br/> | Challenge string used to generate the Id.<br/> |



 

## Returns

[**FailedAuthenticationException**](failedauthenticationexception-class-java.md)

## Defined in

FailedAuthenticationException.java

 

 





