---
title: UserPolicy.accessCheck method
description: Does the user policy have the given right.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: A2E247BA-C6B8-464C-9191-972C27B8187B
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserPolicy.accessCheck method
topic_type:
- apiref
api_name:
- UserPolicy.accessCheck method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.accessCheck method

Does the user policy have the given right.

## Signature

``` syntax
public boolean accessCheck(String right)
```

## Parameters



| Name               | Datatype              | Notes |
|--------------------|-----------------------|-------|
| *right*<br/> | **String**<br/> |       |



 

## Returns

A **Boolean** indicating whether or not the checked right is granted.

## Defined in

UserPolicy.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





