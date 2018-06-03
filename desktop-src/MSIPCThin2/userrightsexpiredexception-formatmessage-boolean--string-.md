---
title: UserRightsExpiredException.formatMessage(boolean, String)
description: Format the UserRightsExpiredException message.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: E74D5D67-EC40-4466-AC9C-59E7499EA820
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserRightsExpiredException.formatMessage(boolean, String)
topic_type:
- apiref
api_name:
- UserRightsExpiredException.formatMessage(boolean, String)
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserRightsExpiredException.formatMessage(boolean, String)

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Format the [**UserRightsExpiredException**](userrightsexpiredexception-class-java.md) message.

## Signature

``` syntax
private static String formatMessage(boolean isURIEmailAddress, String uri)
```

## Parameters



| Name                           | Datatype               | Description                                                 |
|--------------------------------|------------------------|-------------------------------------------------------------|
| *isURIEmailAddress*<br/> | **boolean**<br/> | Is the following URI parameter an email address.<br/> |
| *uri*<br/>               | **String**<br/>  |                                                             |



 

## Returns

A **String** containing the formatted message.

## Defined in

UserRightsExpiredException.java

 

 





