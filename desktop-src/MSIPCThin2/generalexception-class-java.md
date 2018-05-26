---
title: GeneralException class
description: A general exception used to wrap exceptions with a simplified error message.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 75019a9e-818a-41f4-935f-71536fc6894d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GeneralException class
topic_type:
- apiref
api_name:
- GeneralException class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GeneralException class

A general exception used to wrap exceptions with a simplified error message. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.

## Signature

``` syntax
public class GeneralException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                           | Description                                                              |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**GeneralException**](generalexception-constructor-java.md)<br/>                       | Initializes a new instance of the **GeneralException** class.<br/> |
| [**GeneralException(Throwable)**](generalexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **GeneralException** class.<br/> |



 

## Methods



| Name                   | Description                                                                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **getType**<br/> | Returns the type of the exception. Inherited from [**ProtectionException**](protectionexception-class-java.md).<br/> |



 

## Defined in

GeneralException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **GeneralException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





