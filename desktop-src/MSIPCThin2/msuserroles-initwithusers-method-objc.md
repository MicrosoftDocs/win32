---
title: MSUserRoles initWithUsers method
description: Initialize an MSUserRoles object with users and roles.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 2A2D0567-62A7-4222-997D-DBE5338955EF
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserRoles initWithUsers method
topic_type:
- apiref
api_name:
- MSUserRoles initWithUsers method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSUserRoles initWithUsers method

Initialize an [**MSUserRoles**](msuserroles-class.md) object with users and roles.

## Signature

``` syntax
- (id)initWithUsers:(NSArray/*NSString*/*)users
              roles:(NSArray/*NSString*/*)roles;
```

## Parameters



| Name               | Datatype                  | Notes                                                                |
|--------------------|---------------------------|----------------------------------------------------------------------|
| *users*<br/> | **NSArray** \*<br/> | Set of users to whom the roles are assigned.<br/>              |
| *roles*<br/> | **NSArray** \*<br/> | See [**MSRole**](msrole-class-objc.md) for types to use.<br/> |



 

## Returns

An identifier of type **id** of the initialized [**MSUserRoles**](msuserroles-class.md) object.

## Defined in

MSUserRoles.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





