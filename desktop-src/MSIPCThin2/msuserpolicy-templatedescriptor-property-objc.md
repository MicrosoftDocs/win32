---
title: MSUserPolicy templateDescriptor property
description: The template used to protect the content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: C1B252FF-EDAB-4825-9E53-BA06F542A254
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserPolicy templateDescriptor property
topic_type:
- apiref
api_name:
- MSUserPolicy templateDescriptor property
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSUserPolicy templateDescriptor property

The template used to protect the content. This property will be null for custom policies.

## Signature

``` syntax
@property (strong, readonly) MSTemplateDescriptor *templateDescriptor;
```

## Property Values



| Name                            | Datatype                                                                          | Notes |
|---------------------------------|-----------------------------------------------------------------------------------|-------|
| *templateDescriptor*<br/> | [**MSTemplateDescriptor**](mstemplatedescriptor-interface-objc.md) \*<br/> |       |



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





