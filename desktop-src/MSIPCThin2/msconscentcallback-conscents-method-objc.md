---
title: MSConsentCallback consents method
description: Implement this callback method to process user consent.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 75B031C2-685F-4207-B20F-E84FE3742713
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSConsentCallback consents method
topic_type:
- apiref
api_name:
- MSConsentCallback consents method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSConsentCallback consents method

Implement this callback method to process user consent.

## Signature

``` syntax
- (void)consents:(NSArray *)consents 
   consentsCompletionBlock:(void(^)(NSArray *consentsResult))consentsCompletionBlock;
```

## Parameters



| Name                         | Datatype                                          | Notes                                                                     |
|------------------------------|---------------------------------------------------|---------------------------------------------------------------------------|
| *consents*<br/>        | **NSArray** \*<br/>                         | An array of [**MSConsent**](msconscent-class-objc.md) objects<br/> |
| *completionBlock*<br/> | void(^)(**NSArray** \* consentsResult)<br/> | An array of [**MSConsent**](msconscent-class-objc.md) objects<br/> |



 

## Defined in

MSConsent.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

This method must be implemented by you. The Rights Management SDK 4.2 will use this method via its APIs to process user consent for your application.

 

 





