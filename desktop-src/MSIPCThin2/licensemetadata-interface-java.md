---
title: LicenseMetadata interface
description: Information for the document tracking feature.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 6D2AEF01-70A9-47BB-BAA4-70ADF7690C18
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- LicenseMetadata interface
topic_type:
- apiref
api_name:
- LicenseMetadata interface
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LicenseMetadata interface

Information for the document tracking feature.

The required properties are **contentName** and **notificationType** which are set by the initializing method, [**LicenseMetadata**](licensemetadata-licensemetadata.md). The other properties are optional.

For more information, see [**How to: Use document tracking**](how-to--use-document-tracking.md).

## Signature

``` syntax
public class LicenseMetadata implements Serializable
```

## Methods



| Name                                                                                                  | Description                                                                      |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**LicenseMetadata**](licensemetadata-licensemetadata.md)<br/>                                 | Initializes a license metadata object.<br/>                                |
| [**getContentName**](licensemetadata-getcontentname-method-java.md)<br/>                       | Get the name of a content to be tracked.<br/>                              |
| [**getContentPath**](licensemetadata-getcontentpath-method-java.md)<br/>                       | Get the content path (file path) of the tracked document.<br/>             |
| [**getContentDateCreated**](licensemetadata-getcontentdatecreated-method-java.md)<br/>         | Get the creation date of the tracked document.<br/>                        |
| [**getContentDateModified**](licensemetadata-getcontentdatemodified-method-java.md)<br/>       | Get the last date the tracked document was modified.<br/>                  |
| [**getNotificationPreference**](licensemetadata-getnotificationpreference-method-java.md)<br/> | Get the type of user notification preference of the tracked document.<br/> |
| [**getNotificationType**](licensemetadata-getnotificationtype-method-java.md)<br/>             | Gets the type of user notification for the tracked document.<br/>          |
| [**setContentName**](licensemetadata-setcontentname-method-java.md)<br/>                       | Set the name of a content to be tracked.<br/>                              |
| [**setContentPath**](licensemetadata-setcontentpath-method-java.md)<br/>                       | Set the content path (file path) of the tracked document.<br/>             |
| [**setContentDateCreated**](licensemetadata-setcontentdatecreated-method-java.md)<br/>         | Set the creation date of the tracked document.<br/>                        |
| [**setContentDateModified**](licensemetadata-setcontentdatemodified-method-java.md)<br/>       | Set the last date the tracked document was modified.<br/>                  |
| [**setNotificationPreference**](licensemetadata-setnotificationpreference-method-java.md)<br/> | Set the type of user notification preference of the tracked document.<br/> |
| [**setNotificationType**](licensemetadata-setnotificationtype-method.md)<br/>                  | Sets the type of user notification for the tracked document.<br/>          |



 

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Defined in

LicenseMetadata.java

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





