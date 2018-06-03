---
title: MSPolicyDescriptor licenseMetadata property
description: Pointer to a MSLicenseMetadata object containing document tracking information.See \ 0034;Remarks \ 0034; section for more details.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: A8E46A26-653A-4353-B726-12F508B21050
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSPolicyDescriptor licenseMetadata property
topic_type:
- apiref
api_name:
- MSPolicyDescriptor licenseMetadata property
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSPolicyDescriptor licenseMetadata property

Pointer to a [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) object containing document tracking information.

See "Remarks" section for more details.

## Signature

``` syntax
@property(strong) MSLicenseMetadata *licenseMetadata;
```

## Property Values



| Name                         | Datatype                                                                | Notes                                                                                                                                                                                                                               |
|------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *licenseMetadata*<br/> | [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) \*<br/> | Must be initialized before creating the [**MSUserPolicy**](msuserpolicy-interface-objc.md) with the [**MSPolicyDescriptor**](mspolicydescriptor-interface-objc.md).<br/> See "Remarks" section for more details.<br/> |



 

## Defined in

MSPolicyDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

This property must be initialized prior to creating the [**MSUserPolicy**](msuserpolicy-interface-objc.md) only if you wish to make use of document tracking. If you don't want to enable document tracking, this property can be left uninitialized (nil) and the call to [**registerForDocTracking:userId:authenticationCallback:completionBlock**](msuserpolicy-registerfordoctracking-userid-authenticationcallback-completionblock-method-objc.md) on the **MSUserPolicy** can be skipped.

 

 





