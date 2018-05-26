---
title: MSUserPolicy owner property
description: The email address of the current content owner.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: f1504666-1a84-413e-8092-a1a5450b812c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserPolicy owner property
topic_type:
- apiref
api_name:
- MSUserPolicy owner property
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSUserPolicy owner property

The email address of the current content owner. The current content **owner** is potentially different than the [**issuedTo**](msuserpolicy-issuedto-property-objc.md) owner, the original content owner.

## Signature

``` syntax
@property(strong, readonly) NSString *owner;
```

## Property Values



| Name               | Datatype                   | Notes |
|--------------------|----------------------------|-------|
| *owner*<br/> | **NSString** \*<br/> |       |



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





