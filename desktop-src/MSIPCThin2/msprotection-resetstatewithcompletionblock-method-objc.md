---
title: MSProtection resetStateWithCompletionBlock method
description: Use to reset the state.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: D3BFDAC7-C7B7-4FF5-BA50-C189CC250CD8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtection resetStateWithCompletionBlock method
topic_type:
- apiref
api_name:
- MSProtection resetStateWithCompletionBlock method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSProtection resetStateWithCompletionBlock method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Use to reset the state. This can clear all cache.

## Signature

``` syntax
+ (void)resetStateWithCompletionBlock:(void(^)())completionBlock;
```

## Parameters



| Name                         | Datatype        | Notes |
|------------------------------|-----------------|-------|
| *completionBlock*<br/> | void<br/> |       |



 

## Returns

void

## Defined in

MSProtection.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

[**templateListWithUserId**](mstemplatedescriptor-templatelistwithuserid-userid-authenticationcallback-completionblock-method-objc.md) should be invoked from the main thread.

 

 





