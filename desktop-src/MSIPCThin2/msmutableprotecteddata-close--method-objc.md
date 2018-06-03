---
title: MSMutableProtectedData close method
description: Writes and finalizes the protection of any remaining data, smaller than the block size, that is left over from preceding append and update calls.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: ef0b5ca3-de07-4075-b430-22c6103d7f95
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSMutableProtectedData close method
topic_type:
- apiref
api_name:
- MSMutableProtectedData close method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSMutableProtectedData close method

Writes and finalizes the protection of any remaining data, smaller than the block size, that is left over from preceding append and update calls.

## Signature

``` syntax
- (BOOL)close:(NSError **)errorPtr; 
```

## Parameters



| Name                  | Datatype                    | Notes                                                                         |
|-----------------------|-----------------------------|-------------------------------------------------------------------------------|
| *errorPtr*<br/> | **NSError** \*\*<br/> | Optional. If an error occurs, contains the error code and details.<br/> |



 

## Returns

Type: **BOOL**

**YES** if the operation is successful; otherwise, **NO**. If the operation isn't successful, the *errorPtr* parameter references an **NSError** object that contains more information about the error.

## Defined in

MSMutableProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





