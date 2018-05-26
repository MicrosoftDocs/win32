---
title: LicenseMetadata setContentDateCreated method
description: Sets the creation date of the document to be tracked.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: DEE70646-D0C7-45A7-B7B5-92D055FA59D7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- LicenseMetadata setContentDateCreated method
topic_type:
- apiref
api_name:
- LicenseMetadata setContentDateCreated method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LicenseMetadata setContentDateCreated method

Sets the creation date of the document to be tracked. This property is optional.

## Signature

``` syntax
public void setContentDateCreated(Date contentDateCreated)
```

## Parameters



| Parameter                       | Datatype            | Notes                                                                                                                                                                                                         |
|---------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *contentDateCreated*<br/> | **Date**<br/> | Optional<br/> This property defaults to the current date and time if property not set.<br/> The format this property is governed by RFC3339. <br/> Example:  2015-08-20T15:17  .<br/> |



 

## Defined in

LicenseMetadata.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





