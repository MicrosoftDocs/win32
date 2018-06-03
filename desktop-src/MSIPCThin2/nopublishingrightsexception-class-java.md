---
title: NoPublishingRightsException class
description: Thrown when the user rights over the protected content have expired. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 2b0a3a7c-7b12-4546-9b29-54dd691c91de
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- NoPublishingRightsException class
topic_type:
- apiref
api_name:
- NoPublishingRightsException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NoPublishingRightsException class

Thrown when the user rights over the protected content have expired. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class NoPublishingRightsException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                         | Description                                                                         |
|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**NoPublishingRightsException(String)**](nopublishingrightsexception-constructor-java.md)<br/>                       | Initializes a new instance of the **NoPublishingRightsException** class.<br/> |
| [**NoPublishingRightsException(String, Throwable)**](nopublishingrightsexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **NoPublishingRightsException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>          | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

NoPublishingRightsException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **NoPublishingRightsException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





