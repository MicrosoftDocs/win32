---
title: MSUserPolicy issuedTo property
description: The email address of the original content owner.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 52A1433A-CF06-44CA-BA5D-7E8B107C1F5A
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserPolicy issuedTo property
topic_type:
- apiref
api_name:
- MSUserPolicy issuedTo property
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSUserPolicy issuedTo property

The email address of the original content owner. The **issuedTo** content owner is potentially different than the current [**owner**](msuserpolicy-owner-property-objc.md).

## Signature

``` syntax
@property(strong, readonly) NSString *issuedTo;
```

## Property Values



| Name                         | Datatype            | Notes |
|------------------------------|---------------------|-------|
| *isIssuedToOwner*<br/> | **BOOL**<br/> |       |



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





