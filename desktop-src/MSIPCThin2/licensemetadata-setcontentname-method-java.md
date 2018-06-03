---
title: LicenseMetadata setContentName method
description: Sets the content file name of the document to be tracked, not including the path.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: B07468C1-A3B7-4A9C-895F-7443C4E5ED05
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- LicenseMetadata setContentName method
topic_type:
- apiref
api_name:
- LicenseMetadata setContentName method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LicenseMetadata setContentName method

Sets the content file name of the document to be tracked, not including the path. This property is required.

For more information see [**getContentName**](licensemetadata-getcontentname-method-java.md), [**getContentPath**](licensemetadata-getcontentpath-method-java.md) and [**setContentPath**](licensemetadata-setcontentpath-method-java.md).

## Signature

``` syntax
public void setContentName(String contentName);
```

## Parameters



| Parameter                | Datatype              | Notes                                             |
|--------------------------|-----------------------|---------------------------------------------------|
| *contentName*<br/> | **String**<br/> | Required<br/> Ex: "filename.txt"<br/> |



 

## Defined in

LicenseMetadata.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





