---
title: MSConsentResult class
description: Defines the results of the consent process.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 6280341D-9DDD-417D-9735-0362D05404C4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSConsentResult class
topic_type:
- apiref
api_name:
- MSConsentResult class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSConsentResult class

Defines the results of the consent process.

## Signature

``` syntax
@interface MSConsentResult : NSObject
```

## Properties



| Name                                                                     | Note                                                                               |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**accepted**](msconscentresult-accepted-property-objc.md)<br/>   | Gets the state of the user's acceptance.<br/>                                |
| [**showAgain**](msconscentresult-showagain-property-objc.md)<br/> | Gets the user's choice whether to show the consent dialog again or not.<br/> |
| [**userId**](msconscentresult-userid-property-objc.md)<br/>       | Gets the *userId* of the consenting user.<br/>                               |



 

## Defined in

MSConsent.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





