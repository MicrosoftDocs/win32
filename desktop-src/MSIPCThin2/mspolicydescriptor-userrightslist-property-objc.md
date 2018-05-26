---
title: MSPolicyDescriptor userRightsList property
description: Rights granted to users for this policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0B22EB3A-EC0B-4C3E-A5FE-DC4547679ADC
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSPolicyDescriptor userRightsList property
topic_type:
- apiref
api_name:
- MSPolicyDescriptor userRightsList property
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSPolicyDescriptor userRightsList property

Rights granted to users for this policy

## Signature

``` syntax
@property (strong, readonly) NSArray/*MSUserRights*/ *userRightsList;
```

## Property Values



| Name                        | Datatype                  | Notes                                                                      |
|-----------------------------|---------------------------|----------------------------------------------------------------------------|
| *userRightsList*<br/> | **NSArray** \*<br/> | An array of [**MSUserRights**](msuserrights-interface-objc.md)<br/> |



 

## Defined in

MSPolicyDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





