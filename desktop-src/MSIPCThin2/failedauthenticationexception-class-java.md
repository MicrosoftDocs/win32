---
title: FailedAuthenticationException class
description: Signals that authentication failure has occurred. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0068DDF6-167B-4ABC-9DAE-DA0C4771604F
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- FailedAuthenticationException class
topic_type:
- apiref
api_name:
- FailedAuthenticationException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FailedAuthenticationException class

Signals that authentication failure has occurred. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class FailedAuthenticationException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                                                       | Description                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**FailedAuthenticationException(String, String)**](failedauthenticationexception-string--constructor-java.md)<br/>                                 | Initializes a new instance of the **FailedAuthenticationException** class.<br/> |
| [**FailedAuthenticationException(String, String, Throwable)**](failedauthenticationexception-string--protectionexception--constructor-java.md)<br/> | Initializes a new instance of the **FailedAuthenticationException** class.<br/> |



 

## Methods



| Name                                                                                                         | Description                                                                                                  |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/>                                                                           | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>                                                                                    | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |
| [**getWWWAuthenticateHeader**](failedauthenticationexception-getwwwauthenticateheader-method.md)<br/> | Gets the WWW Authentication Header.<br/>                                                               |



 

## Defined in

FailedAuthenticationException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

For more information, see the SDK documentation for the [**ProtectionException**](protectionexception-class-java.md) class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





