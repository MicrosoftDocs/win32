---
title: MSMutableCustomProtectedData class
description: Provides a mutable custom protected data object that can be used to encrypt a block of RMS-protected data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: fc7a8c55-da96-4937-8011-ff12e61ec231
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSMutableCustomProtectedData class
topic_type:
- apiref
api_name:
- MSMutableCustomProtectedData class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSMutableCustomProtectedData class

Provides a mutable custom protected data object that can be used to encrypt a block of RMS-protected data. Use **MSMutableCustomProtectedData** when encrypting files that are protected using a custom protected file format rather than Microsoft Protected File format. When decrypting files that are protected using a custom protected file format, use [**MSCustomProtectedData**](mscustomprotecteddata-interface-objc.md).

> \[!Important\]  
> RMS applications that use **MSMutableCustomProtectedData** may be incompatible with SharePoint, Exchange, and other RMS applications. For most applications, it is recommended that you use [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) instead.

 

## Signature

``` syntax
@interface MSMutableCustomProtectedData : MSMutableProtectedData
```

## Methods



| Name                                                                                                                                                                                      | Description                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**customProtectorWithProtectionPolicy**](msmutablecustomprotecteddata-customprotectorwithprotectionpolicy-backingdata-protectedcontentoffset-completionblock-method-objc.md)<br/> | Asynchronously creates an **MSMutableCustomProtectedData** object that can be used to encrypt plaintext data and write to the specified backing **NSMutableData** object.<br/> |



 

## Defined in

MSMutableCustomProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

**MSMutableCustomProtectedData** and its super-class [**MSCustomProtectedData**](mscustomprotecteddata-interface-objc.md) provide data objects, object-oriented wrappers for byte buffers containing RMS-encrypted data.

These objects provide

-   automatic decryption when data is read
-   automatic encryption when data is written

These objects can be used wherever **NSData** and **NSMutableData** are required

The methods of the [**MSCustomProtectedData**](mscustomprotecteddata-interface-objc.md) class that write data transparently encrypt the plaintext data and write the ciphertext to the backing **NSMutableData** object.

Data written using this class must be 16-byte aligned.

[**MSCustomProtectedData**](mscustomprotecteddata-interface-objc.md) and **MSMutableCustomProtectedData** are used to read and write data for files that are protected with a custom protected file format instead of the Microsoft Protected File format. To read and write files that are protected with the Microsoft Protected File format, use [**MSProtectedData**](msprotecteddata-interface-objc.md) and [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





