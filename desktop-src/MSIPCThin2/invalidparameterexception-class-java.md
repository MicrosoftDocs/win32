---
title: InvalidParameterException class
description: Signals an invalid parameter exception has occurred. Extends the ProtectionException class.This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '947c218f-18ad-452e-8d54-c1ecd90bff2a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["InvalidParameterException class"]
topic_type:
- apiref
api_name:
- InvalidParameterException class
api_type:
- NA
---

# InvalidParameterException class

Signals an invalid parameter exception has occurred. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.

## Signature

``` syntax
public class InvalidParameterException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                             | Description                                                                       |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**InvalidParameterException(String, String)**](invalidparameterexception-constructor-java.md)<br/>       | Initializes a new instance of the **InvalidParameterException** class.<br/> |
| [**InvalidParameterException(Throwable)**](invalidparameterexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **InvalidParameterException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |



 

## Defined in

InvalidParameterException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **InvalidParameterException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





