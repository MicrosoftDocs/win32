---
title: MSPolicyAcquisitionOptions enum
description: System operation control options.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'D5DEB8AA-FC2A-4D57-8B1B-F5626503447C'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSPolicyAcquisitionOptions enum"]
topic_type:
- apiref
api_name:
- MSPolicyAcquisitionOptions enum
api_type:
- NA
---

# MSPolicyAcquisitionOptions enum

System operation control options.

## Signature

``` syntax
typedef enum MSPolicyAcquisitionOptions : NSUInteger {
    Default = 0x0,
    OfflineOnly = 0x1
} MSPolicyAcquisitionOptions;
```

## Members



| Member                     | Value        | Notes                                                                                                                                         |
|----------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Default**<br/>     | 0<br/> | When specified, the SDK will attempt to perform the operation silently, and without using the network. This is not guaranteed.<br/>     |
| **OfflineOnly**<br/> | 1<br/> | When specified, the SDK will not show any UI (e.g. an email app can use this for trying to show a protected email on preview pane)<br/> |



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





