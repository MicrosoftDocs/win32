---
title: UserRightsExpiredException class
description: Thrown when the user rights over the protected content have expired. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 448dcc01-a19c-40ff-b6ee-f39950f2651e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserRightsExpiredException class
topic_type:
- apiref
api_name:
- UserRightsExpiredException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserRightsExpiredException class

Thrown when the user rights over the protected content have expired. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class UserRightsExpiredException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                                | Description                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**UserRightsExpiredException(boolean, String)**](userrightsexpiredexception-constructor-java.md)<br/>                       | Initializes a new instance of the **UserRightsExpiredException** class.<br/> |
| [**UserRightsExpiredException(boolean, String, Throwable)**](userrightsexpiredexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **UserRightsExpiredException** class.<br/> |



 

## Methods



| Name                                                                                          | Description                                                                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**formatMessage**](userrightsexpiredexception-formatmessage-boolean--string-.md)<br/> | Format the **UserRightsExpiredException** message.<br/>                                                |
| [**getReferrer**](userrightsexpiredexception-getreferrer-method-java.md)<br/>          | Gets the contact in case of missing rights to the document.<br/>                                       |
| **getLocalizedMessage**<br/>                                                            | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>                                                                     | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

UserRightsExpiredException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **UserRightsExpiredException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





