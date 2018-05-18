---
title: CommunicationException class
description: Thrown when the device has no connection to the internet.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'f4a70adb-8911-4012-8bd9-7503c641fe82'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CommunicationException class"]
topic_type:
- apiref
api_name:
- CommunicationException class
api_type:
- NA
---

# CommunicationException class

Thrown when the device has no connection to the internet.

## Signature

``` syntax
public class CommunicationException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                               | Description                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**CommunicationException(String)**](communicationexception-string--string--constructor-java.md)<br/>                       | Initializes a new instance of the **CommunicationException** class.<br/> |
| [**CommunicationException(String, Throwable)**](communicationexception-string--string--throwable--constructor-java.md)<br/> | Initializes a new instance of the **CommunicationException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>          | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

CommunicationException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **CommunicationException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





