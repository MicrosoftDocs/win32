---
title: InvalidCertificateException class
description: Thrown when the SDK has received an invalid certificate. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0018671D-7962-4024-AB33-A3A0282293EE
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- InvalidCertificateException class
topic_type:
- apiref
api_name:
- InvalidCertificateException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InvalidCertificateException class

Thrown when the SDK has received an invalid certificate. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class InvalidCertificateException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                 | Description                                                                         |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**InvalidCertificateException**](invalidcertificateexception-constructor-java.md)<br/>                       | Initializes a new instance of the **InvalidCertificateException** class.<br/> |
| [**InvalidCertificateException(Throwable)**](invalidcertificateexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **InvalidCertificateException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                                 |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/>                |
| **getType**<br/>             | Returns the type of the exception. Inherited from [**ProtectionException**](protectionexception-class-java.md).<br/> |



 

## Defined in

InvalidCertificateException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

For more information, see the SDK documentation for the [**ProtectionException**](protectionexception-class-java.md) class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





