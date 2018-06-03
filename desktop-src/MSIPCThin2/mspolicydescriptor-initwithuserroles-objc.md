---
title: MSPolicyDescriptor initWithUserRoles userRoles method
description: Initialize an MSPolicyDescriptor with user roles.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: D7A52307-8EE2-45E8-BF2B-F1EB11FD9FAC
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSPolicyDescriptor initWithUserRoles userRoles method
topic_type:
- apiref
api_name:
- MSPolicyDescriptor initWithUserRoles userRoles method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSPolicyDescriptor initWithUserRoles:userRoles method

Initialize an [**MSPolicyDescriptor**](mspolicydescriptor-interface-objc.md) with user roles.

## Signature

``` syntax
- (id)initWithUserRoles:(NSArray /*MSUserRoles*/ *)userRoles;
```

## Parameters



| Name                   | Datatype                  | Notes                                                           |
|------------------------|---------------------------|-----------------------------------------------------------------|
| *userRoles*<br/> | **NSArray** \*<br/> | An array of [**MSUserRoles**](msuserroles-class.md)<br/> |



 

## Returns

Id of the initialized [**MSPolicyDescriptor**](mspolicydescriptor-interface-objc.md).

## Defined in

MSPolicyDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





