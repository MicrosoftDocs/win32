---
title: GetUserPolicyResultStatus enumeration
description: Provides constants for the result of the try at content consumption.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: T:Microsoft.RightsManagement.GetUserPolicyResultStatus
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GetUserPolicyResultStatus enumeration
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.GetUserPolicyResultStatus
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetUserPolicyResultStatus enumeration

Provides constants for the result of the try at content consumption.

## Syntax


```C++
public enum class GetUserPolicyResultStatus
```



## Members

The **GetUserPolicyResultStatus** enumeration has these members.



| Member       | Value | Description                                                                |
|:-------------|:------|:---------------------------------------------------------------------------|
| **Success**  | 0     | The operation worked.<br/>                                           |
| **NoRights** | 1     | The user does not have sufficient rights to access the content.<br/> |
| **Expired**  | 2     | The user's access is expired.<br/>                                   |



## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



 

 





