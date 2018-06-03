---
title: MSUserRoles class
description: Represents a user's roles.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 50360807-3089-4D84-87E7-93E7533C45CA
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserRoles class
topic_type:
- apiref
api_name:
- MSUserRoles class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSUserRoles class

Represents a user's roles.

## Signature

``` syntax
@interface MSUserRoles : MSSecureCodableObject
```

## Methods



| Name                                                                      | Description                                                                                  |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**initWithUsers**](msuserroles-initwithusers-method-objc.md)<br/> | Initialize an MSUserRoles object's properties; a set of users and a set of roles.<br/> |



 

## Properties



| Name                                                        | Description                                         |
|-------------------------------------------------------------|-----------------------------------------------------|
| [**roles**](msuserroles-roles-property-objc.md)<br/> | The assigned roles.<br/>                      |
| [**users**](msuserroles-users-property-objc.md)<br/> | The users to whom the roles are assigned<br/> |



 

## Defined in

MSUserRoles.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





