---
title: MSLicenseMetadata initWithContentName notificationType method
description: Initialize an MSLicenseMeta object with the content name and notification type.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'A0C67BB1-5079-43E5-AD3F-994A0A7035C2'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSLicenseMetadata initWithContentName notificationType method"]
topic_type:
- apiref
api_name:
- MSLicenseMetadata initWithContentName notificationType method
api_type:
- NA
---

# MSLicenseMetadata initWithContentName:notificationType method

Initialize an [**MSLicenseMeta**](mslicensemetadata-class-objc.md) object with the content name and notification type.

## Signature

``` syntax
- (id)initWithContentName:(NSString *)contentName
notificationType:(MSNotificationType) notificationType;
```

## Parameters



| Name                          | Datatype                                                              | Notes               |
|-------------------------------|-----------------------------------------------------------------------|---------------------|
| *contentName*<br/>      | **NSString** \*<br/>                                            | Required<br/> |
| *notificationType*<br/> | [**MSNotificationType**](msnotificationtype-enum-objc.md)<br/> | Required<br/> |



 

## Returns

Id of the initialized [**MSLicenseMeta**](mslicensemetadata-class-objc.md).

## Defined in

MSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





