---
title: NoConsumptionRightsException(String, boolean, String, Throwable) constructor
description: Initializes a new instance of the NoConsumptionRightsException class with the specified exception and a default tag and message.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '3f95c3d5-55e2-41ee-869c-8bbd1605c1a2'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["NoConsumptionRightsException(String, boolean, String, Throwable) constructor"]
topic_type:
- apiref
api_name:
- NoConsumptionRightsException(String, boolean, String, Throwable) constructor
api_type:
- NA
---

# NoConsumptionRightsException(String, boolean, String, Throwable) constructor

Initializes a new instance of the [**NoConsumptionRightsException**](noconsumptionrightsexception-class-java.md) class with the specified exception and a default tag and message.

## Signature

``` syntax
public NoConsumptionRightsException(String userId, boolean isURIEmailAddress, String uri, Throwable e)
```

## Parameters



| Name                           | Datatype                 | Description                                                                            |
|--------------------------------|--------------------------|----------------------------------------------------------------------------------------|
| *userId*<br/>            | **String**<br/>    | The user Id used while trying to communicate.<br/>                               |
| *isUriEmailAddress*<br/> | **boolean**<br/>   | A flag designating if the following parameter is an email address or a URI.<br/> |
| *uri*<br/>               | **String**<br/>    |                                                                                        |
| *e*<br/>                 | **Throwable**<br/> | The exception being thrown.<br/>                                                 |



 

## Returns

[**NoConsumptionRightsException**](noconsumptionrightsexception-class-java.md)

## Defined in

NoConsumptionRightsException.java

 

 





