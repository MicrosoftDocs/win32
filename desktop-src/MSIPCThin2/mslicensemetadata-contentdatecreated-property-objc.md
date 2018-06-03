---
title: MSLicenseMetadata contentDateCreated property
description: Creation date of the tracked document.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: F75D68E7-5527-4E1C-9476-7904DF4DA5DB
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSLicenseMetadata contentDateCreated property
topic_type:
- apiref
api_name:
- MSLicenseMetadata contentDateCreated property
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSLicenseMetadata contentDateCreated property

Creation date of the tracked document. This parameter is optional and can be set after the [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) object is initialized.

## Signature

``` syntax
@property (strong) NSDate *contentDateCreated;
```

## Property Values



| Name                            | Datatype                 | Notes                                                                                                                                                                                     |
|---------------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *contentDateCreated*<br/> | **NSDate** \*<br/> | This property defaults to the current date and time if property not set.<br/> The format this property is governed by RFC3339. <br/> Example:  2015-08-20T15:17  .<br/> |



 

## Defined in

MSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





