---
title: OnPremServersNotSupportedException class
description: Thrown when the SDK has tried to consume content published by an on-premises server. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7327da2a-1a23-4c91-881a-665c9513c515
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- OnPremServersNotSupportedException class
topic_type:
- apiref
api_name:
- OnPremServersNotSupportedException class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnPremServersNotSupportedException class

Thrown when the SDK has tried to consume content published by an on-premises server. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class OnPremServersNotSupportedException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                               | Description                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**OnPremServersNotSupportedException**](onpremserversnotsupportedexception-constructor-java.md)<br/>                       | Initializes a new instance of the **OnPremServersNotSupportedException** class.<br/> |
| [**OnPremServersNotSupportedException(Throwable)**](onpremserversnotsupportedexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **OnPremServersNotSupportedException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |



 

## Defined in

OnPremServersNotSupportedException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **OnPremServersNotSupportedException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





