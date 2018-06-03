---
title: MSPolicyDescriptor referrer property
description: The URL of the referrer.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 95D0B150-1C36-4EC9-967C-3067B6077C48
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSPolicyDescriptor referrer property
topic_type:
- apiref
api_name:
- MSPolicyDescriptor referrer property
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSPolicyDescriptor referrer property

The URL of the referrer.

## Signature

``` syntax
@property (strong) NSURL *referrer;
```

## Property Values



| Name                  | Datatype                | Notes                               |
|-----------------------|-------------------------|-------------------------------------|
| *referrer*<br/> | **NSURL** \*<br/> | See **Remarks** section.<br/> |



 

## Defined in

MSPolicyDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

Set this property with a URL of a referrer as in this example:


```
policyDescriptor.referrer = [[NSURL alloc] initWithString@"https://contoso.com"];
```



 

 





