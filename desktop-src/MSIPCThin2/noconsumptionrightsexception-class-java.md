---
title: NoConsumptionRightsException class
description: Signals that the user does not have consumption rights over the protected content. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '80d64c1f-6922-4887-9964-40d3f71bd5c9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["NoConsumptionRightsException class"]
topic_type:
- apiref
api_name:
- NoConsumptionRightsException class
api_type:
- NA
---

# NoConsumptionRightsException class

Signals that the user does not have consumption rights over the protected content. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class NoConsumptionRightsException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                                                             | Description                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**NoConsumptionRightsException(String, boolean, String)**](noconsumptionrightsexception-boolean--string--constructor-java.md)<br/>                       | Initializes a new instance of the **NoConsumptionRightsException** class.<br/> |
| [**NoConsumptionRightsException(String, boolean, String, Throwable)**](noconsumptionrightsexception-boolean--string--throwable--constructor-java.md)<br/> | Initializes a new instance of the **NoConsumptionRightsException** class.<br/> |



 

## Methods



| Name                                                                                   | Description                                                                                                  |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/>                                                     | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>                                                              | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |
| [**getReferrer**](noconsumptionrightsexception-getreferrer-method-java.md)<br/> | Gets the contact in case of missing rights to the document.<br/>                                       |



 

## Defined in

NoConsumptionRightsException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **NoConsumptionRightsException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





