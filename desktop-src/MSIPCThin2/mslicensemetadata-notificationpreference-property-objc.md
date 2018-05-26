---
title: MSLicenseMetadata notificationPreference property
description: Type of user notification preference of the tracked document.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: BEF6B0FE-4107-45D7-83E1-6C5E1A525988
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSLicenseMetadata notificationPreference property
topic_type:
- apiref
api_name:
- MSLicenseMetadata notificationPreference property
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSLicenseMetadata notificationPreference property

Type of user notification preference of the tracked document. This parameter is optional and can be set after the [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) object is initialized.

## Signature

``` syntax
@property (assign) MSNotificationPreference *notificationPreference;
```

## Property Values



| Name                                | Datatype                                                                             | Notes                                                                                                                                                                       |
|-------------------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *notificationPreference*<br/> | [**MSNotificationPreference**](msnotificationpreference-enum-objc.md) \*<br/> | If this property is not set, the system behaves as if its set to [**MSNotificationPreference.NotificationPrefDefault**](msnotificationpreference-enum-objc.md).<br/> |



 

## Defined in

MSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





