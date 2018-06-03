---
title: LicenseMetadata setNotificationPreference method
description: Sets the notification preference of the document to be tracked.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: A3B611D3-6B88-454B-9D54-42B94C04CED3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- LicenseMetadata setNotificationPreference method
topic_type:
- apiref
api_name:
- LicenseMetadata setNotificationPreference method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LicenseMetadata setNotificationPreference method

Sets the notification preference of the document to be tracked. This property is optional.

## Signature

``` syntax
public void setNotificationPreference(NotificationPreference notificationPreference)
```

## Parameters



| Parameter                           | Datatype                                                            | Notes                                                                                                                                                          |
|-------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *notificationPreference*<br/> | [**NotificationPreference**](notificationpreference.md)<br/> | Optional<br/> If this property is not set, the system behaves as if its set to [**NOTIFICATION\_PREF\_DEFAULT**](notificationpreference.md).<br/> |



 

## Defined in

LicenseMetadata.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





