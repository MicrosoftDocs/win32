---
title: PolicyDescriptor createPolicyDescriptorFromUserRights method
description: Creates a new policy descriptor using a user rights list.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: F18703D7-A031-4016-9750-D0A7D675E81C
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyDescriptor createPolicyDescriptorFromUserRights method
topic_type:
- apiref
api_name:
- PolicyDescriptor createPolicyDescriptorFromUserRights method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PolicyDescriptor createPolicyDescriptorFromUserRights method

Creates a new policy descriptor using a user rights list.

## Signature

``` syntax
public static PolicyDescriptor createPolicyDescriptorFromUserRights(Collection<UserRights> userRightsList)
```

## Parameters



| Name                        | Datatype                                                                      | Notes |
|-----------------------------|-------------------------------------------------------------------------------|-------|
| *userRightsList*<br/> | **Collection**&lt;[**UserRights**](userrights-class-java.md)&gt; <br/> |       |



 

## Returns

A [**PolicyDescriptor**](policydescriptor-interface-java.md) object initialized with passed in user rights list.

## Defined in

PolicyDescriptor.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





