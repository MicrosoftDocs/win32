---
title: CommunicationException(String, Throwable) constructor
description: Initializes a new instance of the CommunicationException class with a default message and, tag and the application name and inner exception.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '19ae9865-f80a-406b-b02b-2e7ab313222e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CommunicationException(String, Throwable) constructor"]
topic_type:
- apiref
api_name:
- CommunicationException(String, Throwable) constructor
api_type:
- NA
---

# CommunicationException(String, Throwable) constructor

Initializes a new instance of the [**CommunicationException**](communicationexception-class-java.md) class with a default message and, tag and the application name and inner exception.

## Signature

``` syntax
public CommunicationException(String applicationName, Throwable e)
```

## Parameters



| Name                         | Datatype                 | Description                                                                                                                                                               |
|------------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *applicationName*<br/> | **String**<br/>    |                                                                                                                                                                           |
| *e*<br/>               | **Throwable**<br/> | The inner exception. If the inner exception is a [**GeneralException**](generalexception-class-java.md), its type will be the one used for the new exception.<br/> |



 

## Returns

[**CommunicationException**](communicationexception-class-java.md)

## Defined in

CommunicationException.java

 

 





