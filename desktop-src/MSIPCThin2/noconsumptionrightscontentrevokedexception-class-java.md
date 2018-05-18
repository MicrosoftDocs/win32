---
title: NoConsumptionRightsContentRevokedException class
description: Signals that the user does not have consumption rights over the protected content. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '7B96B421-4105-4A67-AA8E-0518FF6D393C'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["NoConsumptionRightsContentRevokedException class"]
topic_type:
- apiref
api_name:
- NoConsumptionRightsContentRevokedException class
api_type:
- NA
---

# NoConsumptionRightsContentRevokedException class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Signals that the user does not have consumption rights over the protected content. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class NoConsumptionRightsException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                                                          | Description                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**NoConsumptionRightsContentRevokedException(String)**](noconsumptionrightscontentrevokedexception-string--method.md)<br/>                            | Initializes a new instance of the **NoConsumptionRightsContentRevokedException** class.<br/> |
| [**NoConsumptionRightsContentRevokedException(String, Throwable)**](noconsumptionrightscontentrevokedexception-string--throwable--method-java.md)<br/> | Initializes a new instance of the **NoConsumptionRightsContentRevokedException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>          | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

NoConsumptionRightsException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **NoConsumptionRightsContentRevokedException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





