---
title: MSUserPolicy accessCheck method
description: Returns a value that indicates whether the current user has the specified right.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'b2fd849f-ffdb-42ec-b5f1-03195c9bc4a8'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSUserPolicy accessCheck method"]
topic_type:
- apiref
api_name:
- MSUserPolicy accessCheck method
api_type:
- NA
---

# MSUserPolicy accessCheck method

Returns a value that indicates whether the current user has the specified right.

## Signature

``` syntax
- (BOOL)accessCheck:(NSString *)right;
```

## Parameters



| Name               | Datatype                   | Notes                                    |
|--------------------|----------------------------|------------------------------------------|
| *right*<br/> | **NSString** \*<br/> | Required. The right to check.<br/> |



 

## Returns

Type: **BOOL**

**YES** if the current user has the right; otherwise, **NO**.

> [!Note]  
> When called on behalf of the content owner, returns **YES** for any right that is specified.

 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





