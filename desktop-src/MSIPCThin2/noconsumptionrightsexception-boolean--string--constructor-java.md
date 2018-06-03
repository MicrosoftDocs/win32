---
title: NoConsumptionRightsException(String, boolean, String) constructor
description: Initializes a new instance of the NoConsumptionRightsException class with a default tag and message.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: b3fd2ba6-da27-4723-a11d-05b26bbfc952
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- NoConsumptionRightsException(String, boolean, String) constructor
topic_type:
- apiref
api_name:
- NoConsumptionRightsException(String, boolean, String) constructor
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NoConsumptionRightsException(String, boolean, String) constructor

Initializes a new instance of the [**NoConsumptionRightsException**](noconsumptionrightsexception-class-java.md) class with a default tag and message.

## Signature

``` syntax
public NoConsumptionRightsException(String userId, boolean isURIEmailAddress, String uri, Throwable e)
```

## Parameters



| Name                           | Datatype               | Description                                                                            |
|--------------------------------|------------------------|----------------------------------------------------------------------------------------|
| *userId*<br/>            | **String**<br/>  | The user Id used while trying to communicate.<br/>                               |
| *isURIEmailAddress*<br/> | **boolean**<br/> | A flag designating if the following parameter is an email address or a URI.<br/> |
| *uri*<br/>               | **String**<br/>  |                                                                                        |



 

## Returns

[**NoConsumptionRightsException**](noconsumptionrightsexception-class-java.md)

## Defined in

NoConsumptionRightsException.java

## Remarks

The tag and message are also logged.

## See also

<dl> <dt>

[**NoConsumptionRightsException**](noconsumptionrightsexception-class-java.md)
</dt> </dl>

 

 





