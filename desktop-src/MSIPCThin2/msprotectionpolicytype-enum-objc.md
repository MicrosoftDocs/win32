---
title: MSUserPolicyType enum
description: Protection policy type.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 441AFB9C-B362-4CCD-BD64-07A3BCE20729
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserPolicyType enum
topic_type:
- apiref
api_name:
- MSUserPolicyType enum
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSUserPolicyType enum

Protection policy type.

## Signature

``` syntax
typedef NS_ENUM(NSUInteger, MSUserPolicyType) {
    TemplateBased = 0,
    Custom = 1
};
```

## Members



| Member                       | Value        | Notes                                    |
|------------------------------|--------------|------------------------------------------|
| **TemplateBased**<br/> | 0<br/> | Policy is based on a template<br/> |
| **Custom**<br/>        | 1<br/> | Policy is custom<br/>              |



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





