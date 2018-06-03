---
title: MSUserRights initWithUsers method
description: Initialize an MSUserRights object's properties.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0e609e7b-996a-46bf-b56e-f2962a8519c3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserRights initWithUsers method
topic_type:
- apiref
api_name:
- MSUserRights initWithUsers method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSUserRights initWithUsers method

Initialize an [**MSUserRights**](msuserrights-interface-objc.md) object's properties.

## Signature

``` syntax
- (id)initWithUsers:(NSArray *)users
             rights:(NSArray/*NSString*/*)rights;
```

## Parameters



| Name                | Datatype                   | Notes                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *users*<br/>  | **NSString** \*<br/> | Set of users to whom the rights are granted<br/>                                                                                                                                                                                                                                                                                                                 |
| *rights*<br/> | **NSArray** \*<br/>  | For more information on managing user rights, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md) as well as [**MSCommonRights**](mscommonrights-interface-objc.md), [**MSEditableDocumentRights**](mseditabledocumentrights-interface-objc.md) and [**MSEmailRights**](msemailrights-interface-objc.md).<br/> |



 

## Returns

An identifier of type **id** referencing the initialized [**MSUserRights**](msuserrights-interface-objc.md) object.

## Defined in

MSUserRights.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





