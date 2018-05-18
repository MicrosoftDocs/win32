---
title: MSLicenseMetadata contentDateModified property
description: Last date the tracked document was modified.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '172537FB-BD74-438D-9352-17E0DF5C7495'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSLicenseMetadata contentDateModified property"]
topic_type:
- apiref
api_name:
- MSLicenseMetadata contentDateModified property
api_type:
- NA
---

# MSLicenseMetadata contentDateModified property

Last date the tracked document was modified. This parameter is optional and can be set after the [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) object is initialized.

## Signature

``` syntax
@property (strong) NSDate *contentDateModified;
```

## Property Values



| Name                             | Datatype                 | Notes                                                                                                                                                                                     |
|----------------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *contentDateModified*<br/> | **NSDate** \*<br/> | This property defaults to the current date and time if property not set.<br/> The format this property is governed by RFC3339. <br/> Example: “2015-08-20T15:17” .<br/> |



 

## Defined in

MSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





