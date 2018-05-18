---
title: DnsLookupException class
description: Thrown when the SDK has received an invalid DNS lookup message.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '52DD3A1A-E8F4-494A-9A85-8C3AA5C6AADB'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["DnsLookupException class"]
topic_type:
- apiref
api_name:
- DnsLookupException class
api_type:
- NA
---

# DnsLookupException class

Thrown when the SDK has received an invalid DNS lookup message.

## Signature

``` syntax
public class DnsLookupException extends ProtectionException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                               | Description                                                                |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [**DnsLookupException**](dnslookupexception-constructor-java.md)<br/>                       | Initializes a new instance of the **DnsLookupException** class.<br/> |
| [**DnsLookupException(Throwable)**](dnslookupexception-throwable--constructor-java.md)<br/> | Initializes a new instance of the **DnsLookupException** class.<br/> |



 

## Methods



| Name                               | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **getLocalizedMessage**<br/> | Returns a localized error message for the exception. Overrides **Throwable.getLocalizedMessage**.<br/> |



 

## Defined in

DnsLookupException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

For more information, see the SDK documentation for the [**ProtectionException**](protectionexception-class-java.md) class.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





