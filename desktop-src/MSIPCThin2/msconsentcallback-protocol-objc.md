---
title: MSConsentCallback protocol
description: Protocol for managing consent.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0B5D76B4-1EA4-4102-B853-7273DF1670BC
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSConsentCallback protocol
topic_type:
- apiref
api_name:
- MSConsentCallback protocol
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSConsentCallback protocol

Protocol for managing consent. Your application should implement this protocol's method and pass it to the Rights Management SDK 4.2 APIs that perform consent.

## Signature

``` syntax
@protocol MSConsentCallback <NSObject>
```

## Methods



| Name                                                                    | Description                                                        |
|-------------------------------------------------------------------------|--------------------------------------------------------------------|
| [**consents**](msconscentcallback-conscents-method-objc.md)<br/> | Implement this callback method to process user consent.<br/> |



 

## Defined in

MSConscentCallback.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





