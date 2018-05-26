---
title: MSUserPolicy policyDescriptor property
description: The custom policy used to protect the content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: EE668E17-5DF7-4A7D-8EBA-E8965E100208
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserPolicy policyDescriptor property
topic_type:
- apiref
api_name:
- MSUserPolicy policyDescriptor property
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSUserPolicy policyDescriptor property

The custom policy used to protect the content. This property will be null for template based policies.

## Signature

``` syntax
@property (strong, readonly) MSPolicyDescriptor *policyDescriptor;
```

## Property Values



| Name                          | Datatype                                                                      | Notes |
|-------------------------------|-------------------------------------------------------------------------------|-------|
| *policyDescriptor*<br/> | [**MSPolicyDescriptor**](mspolicydescriptor-interface-objc.md) \*<br/> |       |



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





