---
title: MSUserRights class
description: Represents a user's rights.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '225fe1f3-8bef-455e-b818-a96c6b8e4195'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSUserRights class"]
topic_type:
- apiref
api_name:
- MSUserRights class
api_type:
- NA
---

# MSUserRights class

Represents a user's rights.

## Signature

``` syntax
@interface MSUserRights : MSSecurableCodeObject
```

## Methods



| Name                                                                       | Description                                                                                        |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**initWithUsers**](msuserrights-initwithusers-method-objc.md)<br/> | Initialize an **MSUserRights** object's properties; a set of users and a set of rights.<br/> |



 

## Properties



| Name                                                           | Description                                         |
|----------------------------------------------------------------|-----------------------------------------------------|
| [**rights**](msuserrights-rights-property-objc.md)<br/> | The rights that are granted<br/>              |
| [**users**](msuserrights-users-property-objc.md)<br/>   | The users to whom the rights are granted<br/> |



 

## Defined in

MSUserRights.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





