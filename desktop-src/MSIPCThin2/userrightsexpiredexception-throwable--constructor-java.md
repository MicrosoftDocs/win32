---
title: UserRightsExpiredException(boolean, String, Throwable) constructor
description: Initializes a new instance of the UserRightsExpiredException class with a default message and tag, a URI with flag, and the specified inner exception.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '6930b960-d9cc-4414-960d-cd946c4199f1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserRightsExpiredException(boolean, String, Throwable) constructor"]
topic_type:
- apiref
api_name:
- UserRightsExpiredException(boolean, String, Throwable) constructor
api_type:
- NA
---

# UserRightsExpiredException(boolean, String, Throwable) constructor

Initializes a new instance of the [**UserRightsExpiredException**](userrightsexpiredexception-class-java.md) class with a default message and tag, a URI with flag, and the specified inner exception.

## Signature

``` syntax
public UserRightsExpiredException(boolean isURIEmailAddress, String uri, Throwable e)
```

## Parameters



| Name                           | Datatype                 | Description                                                 |
|--------------------------------|--------------------------|-------------------------------------------------------------|
| *isURIEmailAddress*<br/> | **boolean**<br/>   | Is the following URI parameter an email address.<br/> |
| *uri*<br/>               | **String**<br/>    |                                                             |
| *e*<br/>                 | **Throwable**<br/> | The inner exception.<br/>                             |



 

## Returns

[**UserRightsExpiredException**](userrightsexpiredexception-class-java.md)

## Defined in

UserRightsExpiredException.java

 

 





