---
title: DeviceRejectedException class
description: Implements a device rejected exception passed from the server.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '3a59301a-6e09-4a1b-8739-9266db52b28a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["DeviceRejectedException class"]
topic_type:
- apiref
api_name:
- DeviceRejectedException class
api_type:
- NA
---

# DeviceRejectedException class

Implements a device rejected exception passed from the server.

## Signature

``` syntax
public class DeviceRejectedException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                 | Description                                                                     |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**DeviceRejectedException(String)**](devicerejectedexception-constructor-java.md)<br/>                       | Initializes a new instance of the **DeviceRejectedException** class.<br/> |
| [**DeviceRejectedException(String, Throwable)**](devicerejectedexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **DeviceRejectedException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |
| **getMessage**<br/>          | Returns a message. Overrides **Throwable.getMessage**.<br/>                                            |



 

## Defined in

DeviceRejectedException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **DeviceRejectedException** class extends the [**ProtectionException**](protectionexception-class-java.md) class. For more information, see the SDK documentation for the **ProtectionException** class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





