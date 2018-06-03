---
title: MSUserPolicy isIssuedToOwner property
description: Is the current user the original owner .
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: A79F886D-9C0F-4156-A222-9716D80C150A
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserPolicy isIssuedToOwner property
topic_type:
- apiref
api_name:
- MSUserPolicy isIssuedToOwner property
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSUserPolicy isIssuedToOwner property

Is the current user the original owner?

## Signature

``` syntax
@property (readonly) BOOL isIssuedToOwner;
```

## Property Values



| Name                    | Datatype                   | Notes                                                                                                                                              |
|-------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| *isIssuedTo*<br/> | **NSString** \*<br/> | Compares the [**issuedTo**](msuserpolicy-issuedto-property-objc.md) and the current [**owner**](msuserpolicy-owner-property-objc.md).<br/> |



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





