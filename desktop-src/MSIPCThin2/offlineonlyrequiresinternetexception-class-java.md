---
title: OfflineOnlyRequiresInternetException class
description: Thrown when communication is needed but the OFFLINE\_ONLY flag is set in consumption scenarios. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 11D18E89-3C9B-45D2-9F3A-46F85AD2654C
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- OfflineOnlyRequiresInternetException class
topic_type:
- apiref
api_name:
- OfflineOnlyRequiresInternetException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OfflineOnlyRequiresInternetException class

Thrown when communication is needed but the OFFLINE\_ONLY flag is set in consumption scenarios. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class OfflineOnlyRequiresInternetException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                                           | Description                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**OfflineOnlyRequiresInternetException(String)**](offlineonlyrequiresinternetexception-constructor-java.md)<br/>                       | Initializes a new instance of the **OfflineOnlyRequiresInternetException** class.<br/> |
| [**OfflineOnlyRequiresInternetException(String, Throwable)**](offlineonlyrequiresinternetexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **OfflineOnlyRequiresInternetException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>          | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

OfflineOnlyRequiresInternetException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

For more information, see the SDK documentation for the [**ProtectionException**](protectionexception-class-java.md) class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





