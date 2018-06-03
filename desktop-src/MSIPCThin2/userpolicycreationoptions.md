---
title: UserPolicyCreationOptions enumeration
description: Used to set flags when creating UserPolicy objects.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: Microsoft.RightsManagement.UserPolicyCreationOptions
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserPolicyCreationOptions enumeration
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicyCreationOptions
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserPolicyCreationOptions enumeration

Used to set flags when creating [**UserPolicy**](userpolicy.md) objects.

## Syntax


```C++
public enum class UserPolicyCreationOptions
```



## Members

The **UserPolicyCreationOptions** enumeration has these members.



| Member                         | Value | Description                                                                                      |
|:-------------------------------|:------|:-------------------------------------------------------------------------------------------------|
| **None**                       | 0x0   |                                                                                                  |
| **AllowAuditedExtraction**     | 0x1   | Specifies whether the content can be opened in a non-RMS aware app or not.<br/>            |
| **PreferDeprecatedAlgorithms** | 0x2   | Specifies whether the [*deprecated algorithms*](terms.md) (ECB) is preferred or not.<br/> |



## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



 

 





