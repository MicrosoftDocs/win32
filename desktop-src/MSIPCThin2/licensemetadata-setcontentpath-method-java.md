---
title: LicenseMetadata setContentPath method
description: Sets the content file path of the document to be tracked, not including the file name.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 273FA3BA-BFB5-4AC2-8B75-96DC084EF2D9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- LicenseMetadata setContentPath method
topic_type:
- apiref
api_name:
- LicenseMetadata setContentPath method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LicenseMetadata setContentPath method

Sets the content file path of the document to be tracked, not including the file name. This property is optional.

For more information see [**getContentName**](licensemetadata-getcontentname-method-java.md), [**getContentPath**](licensemetadata-getcontentpath-method-java.md) and **getContentPath**.

## Signature

``` syntax
public void setContentPath(String contentPath);
```

## Parameters



| Parameter                | Datatype              | Notes                                                                                                                                  |
|--------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| *contentPath*<br/> | **String**<br/> | Optional<br/> Ex: "C:\\MyDocs\\"<br/> If this property is not set the system initializes it to an empty string.<br/> |



 

## Defined in

LicenseMetadata.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





