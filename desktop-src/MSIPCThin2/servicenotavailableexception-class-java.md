---
title: ServiceNotAvailableException class
description: Implements an exception which is used when a retry can help in solving the error which occurred Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'bdab43de-f6b3-4c44-8c89-d2431323856a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ServiceNotAvailableException class"]
topic_type:
- apiref
api_name:
- ServiceNotAvailableException class
api_type:
- NA
---

# ServiceNotAvailableException class

Implements an exception which is used when a retry can help in solving the error which occurred Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class ServiceNotAvailableException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                           | Description                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**ServiceNotAvailableException(String)**](servicenotavailableexception-constructor-java.md)<br/>                       | Initializes a new instance of the **ServiceNotAvailableException** class.<br/> |
| [**ServiceNotAvailableException(String, Throwable)**](servicenotavailableexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **ServiceNotAvailableException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>          | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

ServiceNotAvailableException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **ServiceNotAvailableException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





