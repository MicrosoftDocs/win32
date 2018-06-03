---
title: PolicyAcquisitionOptions enumeration
description: Specifies the expected mode for an operation.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: T:Microsoft.RightsManagement.ProtectionOperationOptions
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyAcquisitionOptions enumeration
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.PolicyAcquisitionOptions
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PolicyAcquisitionOptions enumeration

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Specifies the expected mode for an operation meaning, whether the framework can show UI or connect to a network when performing an operation.

## Syntax


```C++
public enum class PolicyAcquisitionOptions
```



## Members

The **PolicyAcquisitionOptions** enumeration has these members.



| Member          | Value | Description                                                                                                                                                                                                                                                                                                |
|:----------------|:------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **None**        | 0     | The framework will try to perform the operation silently and offline, but will show a UI and connect to a network if necessary.<br/>                                                                                                                                                                 |
| **OfflineOnly** | 1     | The framework will try to perform the operation without connecting to a network. If it needs to connect to a network, the operation will fail. For example, an app can choose not to open a document on the device when it is not connected to a WiFi network unless it can be opened offline. <br/> |



## Thread Safety

Members of this class are not guaranteed to be thread safe.

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## Attributes

<dl></dl> <dl> <dt>

\[[Flags](https://msdn.microsoft.com/library/system.flagsattribute.aspx)()\]
</dt> </dl> <dl> <dt>

\[[Version](https://msdn.microsoft.com/library/windows/apps/br206718)\]
</dt> </dl>

 

 





