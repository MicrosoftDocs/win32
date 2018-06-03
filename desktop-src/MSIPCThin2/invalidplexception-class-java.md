---
title: InvalidPLException class
description: Thrown when the publishing license that was supplied is corrupted. Extends the ProtectionException class.This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: c37ba2b8-5edf-4e89-b448-5afbc31976d3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- InvalidPLException class
topic_type:
- apiref
api_name:
- InvalidPLException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InvalidPLException class

Thrown when the publishing license that was supplied is corrupted. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.

## Signature

``` syntax
public class InvalidPLException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                               | Description                                                                |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [**InvalidPLException**](invalidplexception-constructor-java.md)<br/>                       | Initializes a new instance of the **InvalidPLException** class.<br/> |
| [**InvalidPLException(Throwable)**](invalidplexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **InvalidPLException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |



 

## Defined in

InvalidPLException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **InvalidPLException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





