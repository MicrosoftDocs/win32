---
title: MSCustomProtectedData class
description: Provides a custom protected data object that can be used to read RMS-protected data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7445b13e-6291-4061-9e2d-f260089d5ca2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSCustomProtectedData class
topic_type:
- apiref
api_name:
- MSCustomProtectedData class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCustomProtectedData class

Provides a custom protected data object that can be used to read RMS-protected data. Use **MSCustomProtectedData** when reading files that are protected using a custom protected file format rather than Microsoft Protected File format. When encrypting content for files that are protected using a custom protected file format, use [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md) For more information, see **Remarks** section.

> \[!Important\]  
> RMS applications that use **MSCustomProtectedData** may be incompatible with SharePoint, Exchange, and other RMS applications. For most applications, it is recommended that you use [**MSProtectedData**](msprotecteddata-interface-objc.md) instead.

 

## Signature

``` syntax
@interface MSCustomProtectedData : MSProtectedData
```

## Methods



| Name                                                                                                                                                                               | Description                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**customProtectedDataWithPolicy**](mscustomprotecteddata-customprotecteddatawithpolicy-protecteddata-contentstartposition-contentsize-completionblock-method-objc.md)<br/> | Asynchronously creates an **MSCustomProtectedData** object that can be used to decrypt the specified block of protected data.<br/> |
| [**getEncryptedContentLengthWithPolicy**](mscustomprotecteddata-getencryptedcontentlengthwithpolicy-protectionpolicy-contentlength.md)<br/>                                 | Returns the size of the encrypted content.<br/>                                                                                    |



 

## Defined in

MSCustomProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

**MSCustomProtectedData** and its mutable subclass [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md) provide data objects, object-oriented wrappers for byte buffers containing RMS-encrypted data.

These objects provide

-   automatic decryption when data is read
-   automatic encryption when data is written

These objects can be used wherever **NSData** and **NSMutableData** are required

**MSCustomProtectedData** and [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md) are used to read and write data for files that are protected with a custom protected file format instead of the Microsoft Protected File format. To read and write files that are protected with the Microsoft Protected File format, use [**MSProtectedData**](msprotecteddata-interface-objc.md) and [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





