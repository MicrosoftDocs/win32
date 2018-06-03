---
title: UnsupportedSDKVersionException class
description: The operation is not supported by the version of the SDK. Extends the ProtectionException class.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 249627cb-60cd-460b-b338-9fa6f4a29856
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UnsupportedSDKVersionException class
topic_type:
- apiref
api_name:
- UnsupportedSDKVersionException class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UnsupportedSDKVersionException class

The operation is not supported by the version of the SDK. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

## Signature

``` syntax
public class UnsupportedSDKVersionException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                               | Description                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**UnsupportedSDKVersionException(String)**](unsupportedsdkversionexception-constructor-java.md)<br/>                       | Initializes a new instance of the **UnsupportedSDKVersionException** class.<br/> |
| [**UnsupportedSDKVersionException(String, Throwable)**](unsupportedsdkversionexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **UnsupportedSDKVersionException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>          | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

UnsupportedSDKVersionException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **UnsupportedSDKVersionException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





