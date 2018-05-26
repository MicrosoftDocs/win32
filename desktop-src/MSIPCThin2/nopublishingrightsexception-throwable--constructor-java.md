---
title: NoPublishingRightsException(String, Throwable) constructor
description: Initializes a new instance of the NoPublishingRightsException class with a default message and tag and, a user ID and the specified inner exception.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 93df6252-427d-44b3-96d9-425a6265798d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- NoPublishingRightsException(String, Throwable) constructor
topic_type:
- apiref
api_name:
- NoPublishingRightsException(String, Throwable) constructor
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# NoPublishingRightsException(String, Throwable) constructor

Initializes a new instance of the [**NoPublishingRightsException**](nopublishingrightsexception-class-java.md) class with a default message and tag and, a user ID and the specified inner exception.

## Signature

``` syntax
public NoPublishingRightsException(String userId, Throwable e)
```

## Parameters



| Name                | Datatype                 | Description                                              |
|---------------------|--------------------------|----------------------------------------------------------|
| *userId*<br/> | **String**<br/>    | The user Id used while trying to communicate.<br/> |
| *e*<br/>      | **Throwable**<br/> | The inner exception.<br/>                          |



 

## Returns

[**NoPublishingRightsException**](nopublishingrightsexception-class-java.md)

## Defined in

NoPublishingRightsException.java

 

 





