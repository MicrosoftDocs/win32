---
title: UserCancellationException class
description: Signals that the user has canceled an operation. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 4004A3A1-2AB9-4993-84C2-F3FDC8ABCF31
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserCancellationException class
topic_type:
- apiref
api_name:
- UserCancellationException class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserCancellationException class

Signals that the user has canceled an operation. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class UserCancellationException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                             | Description |
|------------------------------------------------------------------------------------------------------------------|-------------|
| [**UserCancellationException**](usercancellationexception-constructor.md)<br/>                            |             |
| [**UserCancellationException(Throwable)**](usercancellationexception-throwable--constructor-java.md)<br/> |             |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |



 

## Defined in

UserRightsExpiredException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The [**UserRightsExpiredException**](userrightsexpiredexception-class-java.md) class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





