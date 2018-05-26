---
title: MSConsent class
description: Contains the consent process type and result.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 12C3DEF6-4D54-43A0-9408-018529B3B323
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSConsent class
topic_type:
- apiref
api_name:
- MSConsent class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSConsent class

Contains the consent process type and result.

## Signature

``` syntax
@interface MSConsent : NSObject
```

## Properties



| Name                                                                       | Description                                                                                                         |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**type**](msconscent-type-property-objc.md)<br/>                   | Gets the type of consent<br/>                                                                                 |
| [**consentResult**](msconscent-consentresult-property-objc.md)<br/> | Gets the result of the consent as an instance of [**MSConsentResult**](msconscentresult-class-objc.md).<br/> |



 

## Defined in

MSConsent.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





