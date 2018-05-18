---
title: LicenseMetadata LicenseMetadata method
description: Creates a license metadata object for document tracking.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '26AF4429-B5DA-47FE-8A44-BA5B86BBCDE9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["LicenseMetadata LicenseMetadata method"]
topic_type:
- apiref
api_name:
- LicenseMetadata LicenseMetadata method
api_type:
- NA
---

# LicenseMetadata LicenseMetadata method

Creates a license metadata object for document tracking. For more information, see [**How to: Use document tracking**](how-to--use-document-tracking.md).

## Signature

``` syntax
public LicenseMetadata(String contentName, NotificationType notificationType)
```

## Parameters



| Parameter                     | Datatype                                                     | Notes                                             |
|-------------------------------|--------------------------------------------------------------|---------------------------------------------------|
| *contentName*<br/>      | **String**<br/>                                        | Required<br/> Ex: "filename.txt"<br/> |
| *notificationType*<br/> | [**NotificationType**](notificationtype-java.md)<br/> | Required<br/>                               |



 

## Defined in

LicenseMetadata.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





