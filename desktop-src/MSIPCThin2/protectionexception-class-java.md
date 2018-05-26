---
title: ProtectionException class
description: Signals that a protection exception of some kind has occurred. This class is the general class used for exceptions produced by failed or interrupted RMS operations.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: afa00af9-c443-42f3-85f4-67e1415dc135
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ProtectionException class
topic_type:
- apiref
api_name:
- ProtectionException class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectionException class

Signals that a protection exception of some kind has occurred. This class is the general class used for exceptions produced by failed or interrupted RMS operations.

## Signature

``` syntax
public class ProtectionException extends IOException
```

## Constructors

> [!Note]  
> The constructors are documented here for your information and are not intended to be called by you, the application developer.

 



| Name                                                                                                                                  | Description                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**ProtectionException(String, String)**](protectionexception-string--string--constructor-java.md)<br/>                        | Initializes a new instance of the **ProtectionException** class with the specified tag and message.<br/>                   |
| [**ProtectionException(String, String, Throwable)**](protectionsexception-string--string--throwable--constructor-java.md)<br/> | Initializes a new instance of the **ProtectionException** class with the specified tag, message, and inner exception.<br/> |



 

## Methods



| Name                                                                       | Description                                                                         |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**getType**](protectionexception-gettype-method-java.md)<br/>      | Returns the type of the exception.<br/>                                       |
| [**getLogEntries**](protectionexception-getlogentries-java.md)<br/> | Gets the available log entries and removes them from the internal queue.<br/> |
| [**getScenarioId**](protectionexception-getscenarioid-java.md)<br/> | Returns the current scenario Id.<br/>                                         |



 

## Defined in

ProtectionException.java

## Package

com.microsoft.rightsmanagement.exceptions

## Remarks

The **ProtectionException** class extends the **IOException** class. For more information about the **IOException** class and the members it exposes, see the Android developer documentation.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





