---
title: PolicyDescriptor createPolicyDescriptorFromUserRoles method
description: Creates a new policy descriptor using a user roles list.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 928D3300-FD2F-4D34-8E89-F25598F88D1E
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyDescriptor createPolicyDescriptorFromUserRoles method
topic_type:
- apiref
api_name:
- PolicyDescriptor createPolicyDescriptorFromUserRoles method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PolicyDescriptor createPolicyDescriptorFromUserRoles method

Creates a new policy descriptor using a user roles list.

## Signature

``` syntax
public static PolicyDescriptor createPolicyDescriptorFromUserRoles(Collection<UserRoles> userRolesList)
```

## Parameters



| Name                       | Datatype                                    | Notes |
|----------------------------|---------------------------------------------|-------|
| *userRolesList*<br/> | **Collection**&lt;UserRoles&gt; <br/> |       |



 

## Returns

A [**PolicyDescriptor**](policydescriptor-interface-java.md) object initialized with passed in user roles list.

## Defined in

PolicyDescriptor.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





