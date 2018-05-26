---
title: PolicyDescriptor.OfflineCacheLifetimeInDays property
description: Gets or sets the time a user policy can be cached offline (in days).
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.PolicyDescriptor.OfflineCacheLifetimeInDays
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- OfflineCacheLifetimeInDays property
- OfflineCacheLifetimeInDays property, PolicyDescriptor class
- PolicyDescriptor class, OfflineCacheLifetimeInDays property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.PolicyDescriptor.OfflineCacheLifetimeInDays
- Microsoft.RightsManagement.PolicyDescriptor.
- Microsoft.RightsManagement.PolicyDescriptor.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PolicyDescriptor.OfflineCacheLifetimeInDays property

Gets or sets the time a user policy can be cached offline (in days). You can use constants from the [**OfflineCacheLifetimeConstants**](offlinecachelifetimeconstants.md) object.

## Syntax


```C++
public:
property int OfflineCacheLifetimeInDays { 
   int get();
   void set (int value);
}
```



## Property value

Type: **int**

The time a user policy can be cached offline (in days).

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[**PolicyDescriptor**](policydescriptor.md)
</dt> <dt>

[**OfflineCacheLifetimeConstants**](offlinecachelifetimeconstants.md)
</dt> </dl>

 

 





