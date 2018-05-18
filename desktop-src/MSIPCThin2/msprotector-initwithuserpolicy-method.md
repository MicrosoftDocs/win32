---
title: MSProtector initWithUserPolicy method
description: Used to initialize an MSProtector object with an MSUserPolicy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '63469A3F-9912-4406-8661-D8A06C4946CD'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSProtector initWithUserPolicy method"]
topic_type:
- apiref
api_name:
- MSProtector initWithUserPolicy method
api_type:
- NA
---

# MSProtector initWithUserPolicy method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Used to initialize an [**MSProtector**](msprotector-class-objc.md) object with an [**MSUserPolicy**](msuserpolicy-interface-objc.md).

## Signature

``` syntax
- (id)initWithUserPolicy:(MSUserPolicy *)userPolicy;
```

## Parameters



| Name                    | Datatype                                                          | Notes                               |
|-------------------------|-------------------------------------------------------------------|-------------------------------------|
| *userPolicy*<br/> | [**MSUserPolicy**](msuserpolicy-interface-objc.md) \*<br/> | Pointer to a user policy<br/> |



 

## Returns

id of the initialized [**MSProtector**](msprotector-class-objc.md) object.

## Defined in

MSProtection.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

[**templateListWithUserId**](mstemplatedescriptor-templatelistwithuserid-userid-authenticationcallback-completionblock-method-objc.md) should be invoked from the main thread.

 

 





