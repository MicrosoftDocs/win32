---
title: IAsyncControl.cancel method
description: Cancels the associated asynchronous task running.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: bc141067-4bfe-4949-94a8-5a9967cf3fb7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IAsyncControl.cancel method
topic_type:
- apiref
api_name:
- IAsyncControl.cancel method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IAsyncControl.cancel method

Cancels the associated asynchronous task running. At any time, many tasks can be concurrently running. For each async task there is a corresponding [**IAsyncControl**](iasynccontrol-interface.md) object that can be used to cancel it.

## Signature

``` syntax
public void cancel()
```

## Defined in

IAsyncControl.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Remarks

Invoking this method multiple times does not change the effect.

 

 





