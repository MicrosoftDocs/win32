---
title: MSNotificationType enum
description: Document tracking notification type.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '87762103-F048-4F9B-8CDC-982FE3F430AA'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSNotificationType enum"]
topic_type:
- apiref
api_name:
- MSNotificationType enum
api_type:
- NA
---

# MSNotificationType enum

Document tracking notification type.

## Signature

``` syntax
typedef NS_ENUM(NSUInteger, MSNotificationType) {
    NotificationTypeDisabled = 0,
    NotificationTypeEnabled = 1,
    NotificationTypeDenyOnly = 2
};
```

## Members



| Member                                  | Value        | Notes                                                                                               |
|-----------------------------------------|--------------|-----------------------------------------------------------------------------------------------------|
| **NotificationTypeDisabled**<br/> | 0<br/> | No email notifications will be sent.<br/>                                                     |
| **NotificationTypeEnabled**<br/>  | 1<br/> | Email notification will be sent.<br/>                                                         |
| **NotificationTypeDenyOnly**<br/> | 2<br/> | Email notification will only be sent for denied attempts to access the tracked document.<br/> |



 

## Defined in

MSMSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





