---
title: MSLicenseMetadata contentName property
description: File name of the content to be tracked, not including the path.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 930BC0A9-29EA-48E4-B1DB-29E07D7F7F99
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSLicenseMetadata contentName property
topic_type:
- apiref
api_name:
- MSLicenseMetadata contentName property
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSLicenseMetadata contentName property

File name of the content to be tracked, not including the path. This property is required. For more information see [**MSLicenseMetadata.contentPath**](mslicensemetadata-contentpath-property-objc.md).

## Signature

``` syntax
@property (strong, readonly) NSString *contentName;
```

## Property Values



| Name                     | Datatype                   | Notes                                             |
|--------------------------|----------------------------|---------------------------------------------------|
| *contentName*<br/> | **NSString** \*<br/> | Required<br/> Ex: "filename.txt"<br/> |



 

## Defined in

MSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





