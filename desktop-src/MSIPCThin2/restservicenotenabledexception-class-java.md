---
title: RestServiceNotEnabledException class
description: Thrown if the user has an Office 365 account, but the company has not provisioned or enabled RMSO; or if the company has provisioned RMSO, but has not enabled the REST service for any of the AD RMS clients. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 66bcb126-5caa-4f32-9ce3-17e6de24bf1b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- RestServiceNotEnabledException class
topic_type:
- apiref
api_name:
- RestServiceNotEnabledException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RestServiceNotEnabledException class

Thrown if the user has an Office 365 account, but the company has not provisioned or enabled RMSO; or if the company has provisioned RMSO, but has not enabled the REST service for any of the AD RMS clients. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class RestServiceNotEnabledException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                       | Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**RestServiceNotEnabledException**](restservicenotenabledexception-constructor-java.md)<br/>                       | Initializes a new instance of the **RestServiceNotEnabledException** class.<br/> |
| [**RestServiceNotEnabledException(Throwable)**](restservicenotenabledexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **RestServiceNotEnabledException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |



 

## Defined in

RestServiceNotEnabledException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **RestServiceNotEnabledException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

## See also

<dl> <dt>

[com.microsoft.rightsmanagement.exceptions](com-microsoft-rightsmanagement-exceptions.md)
</dt> <dt>

[**ProtectionException**](protectionexception-class-java.md)
</dt> </dl>

 

 





