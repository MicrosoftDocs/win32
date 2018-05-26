---
title: LicenseMetadata setContentDateModified method
description: Sets the modification date of the document to be tracked.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: CBC58BBF-25C6-4B65-8C70-31D0A21F23F0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- LicenseMetadata setContentDateModified method
topic_type:
- apiref
api_name:
- LicenseMetadata setContentDateModified method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LicenseMetadata setContentDateModified method

Sets the modification date of the document to be tracked. This property is optional.

## Signature

``` syntax
public void setContentDateModified(Date contentDateModified)
```

## Parameters



| Parameter                           | Datatype            | Notes                                                                                                                                                                                                         |
|-------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *setContentDateModified*<br/> | **Date**<br/> | Optional<br/> This property defaults to the current date and time if property not set.<br/> The format this property is governed by RFC3339. <br/> Example:  2015-08-20T15:17  .<br/> |



 

## Defined in

LicenseMetadata.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





