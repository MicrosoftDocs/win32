---
title: MSPolicyDescriptor initWithUserRights userRights method
description: Initialize an MSPolicyDescriptor with user rights.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '64FC474F-A20F-4D11-A797-FC7AB2306E5F'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSPolicyDescriptor initWithUserRights userRights method"]
topic_type:
- apiref
api_name:
- MSPolicyDescriptor initWithUserRights userRights method
api_type:
- NA
---

# MSPolicyDescriptor initWithUserRights:userRights method

Initialize an [**MSPolicyDescriptor**](mspolicydescriptor-interface-objc.md) with user rights.

## Signature

``` syntax
- (id)initWithUserRights:(NSArray /*MSUserRights*/ *)userRights;
```

## Parameters



| Name                    | Datatype                  | Notes                                                                       |
|-------------------------|---------------------------|-----------------------------------------------------------------------------|
| *userRights*<br/> | **NSArray** \*<br/> | An array of [**MSUserRights**](msuserrights-interface-objc.md).<br/> |



 

## Returns

Id of the initialized [**MSPolicyDescriptor**](mspolicydescriptor-interface-objc.md).

## Defined in

MSPolicyDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





