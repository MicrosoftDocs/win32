---
title: MSConsentType enum
description: Types of user consent.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 51B12F53-64D3-4A1A-A242-BA976B8CAF48
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSConsentType enum
topic_type:
- apiref
api_name:
- MSConsentType enum
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSConsentType enum

Types of user consent.

## Signature

``` syntax
typedef NS_ENUM(NSUInteger, MSConsentType) 
{
    DocumentTrackingConsent = 0,
    ServiceURLConsent = 1
};
```

## Members



| Member                                 | Value        | Notes |
|----------------------------------------|--------------|-------|
| **DocumentTrackingConsent**<br/> | 0<br/> |       |
| **ServiceURLConsent** <br/>      | 1<br/> |       |



 

## Defined in

MSConsent.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





