---
title: MSLicenseMetadata class
description: Information for the document tracking feature.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: CDEF128A-68F8-4B13-B6BF-80F24AC296C9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSLicenseMetadata class
topic_type:
- apiref
api_name:
- MSLicenseMetadata class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSLicenseMetadata class

Information for the document tracking feature. The required properties are **contentName** and **notificationType** which are set by the initializing method, [**initWithContentName**](mslicensemetadata-initwithcontentname-notificationtype-method-objc.md). The other properties are optional.

For more information, see [**How to: Use document tracking**](how-to--use-document-tracking.md).

## Signature

``` syntax
@interface MSLicenseMetadata : NSObject
```

## Properties



| Name                                                                                                | Description                                                                        |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**contentDateCreated**](mslicensemetadata-contentdatecreated-property-objc.md)<br/>         | Creation date of the tracked document.<br/>                                  |
| [**contentDateModified**](mslicensemetadata-contentdatemodified-property-objc.md)<br/>       | Last date the tracked document was modified.<br/>                            |
| [**contentName**](mslicensemetadata-contentname-property-objc.md)<br/>                       | Required<br/> Name of a content to be tracked.<br/>                    |
| [**contentPath**](mslicensemetadata-contentpath-property-objc.md)<br/>                       | Content path (file path) of the tracked document.<br/>                       |
| [**notificationPreference**](mslicensemetadata-notificationpreference-property-objc.md)<br/> | Type of user notification preference of the tracked document.<br/>           |
| [**notificationType**](mslicensemetadata-notificationtype-property-objc.md)<br/>             | Required<br/> Type of user notification for the tracked document.<br/> |



 

## Methods



| Name                                                                                                         | Description                                     |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [**initWithContentName**](mslicensemetadata-initwithcontentname-notificationtype-method-objc.md)<br/> | Creates an **MSLicenseMeta** object.<br/> |



 

## Defined in

MSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 





 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





