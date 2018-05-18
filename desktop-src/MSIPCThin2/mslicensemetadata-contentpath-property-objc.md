---
title: MSLicenseMetadata contentPath property
description: Full path of the document to be tracked up to but not including the file name.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '4A0F0508-9354-4509-8ED8-C9583B777331'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSLicenseMetadata contentPath property"]
topic_type:
- apiref
api_name:
- MSLicenseMetadata contentPath property
api_type:
- NA
---

# MSLicenseMetadata contentPath property

Full path of the document to be tracked up to but not including the file name. This parameter is optional and can be set after the [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) object is initialized.

## Signature

``` syntax
@property (strong) NSString *contentPath;
```

## Property Values



| Name                     | Datatype                   | Notes                                                                                                                                  |
|--------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| *contentPath*<br/> | **NSString** \*<br/> | Optional<br/> Ex: "C:\\MyDocs\\"<br/> If this property is not set the system initializes it to an empty string.<br/> |



 

## Defined in

MSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





