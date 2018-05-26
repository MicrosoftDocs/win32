---
title: MSMutableProtectedData class
description: MSMutableProtectedData and its super-class MSProtectedData provide protected file data objects, object-oriented wrappers for files that are protected using the Microsoft Protected File format.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 23928d37-0adf-43ea-98a7-b4f288c9643d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSMutableProtectedData class
topic_type:
- apiref
api_name:
- MSMutableProtectedData class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSMutableProtectedData class

**MSMutableProtectedData** and its super-class [**MSProtectedData**](msprotecteddata-interface-objc.md) provide protected file data objects, object-oriented wrappers for files that are protected using the Microsoft Protected File format. Use [**MSProtectedData**](msprotecteddata-interface-objc.md) to read (and transparently decrypt) protected files in consumption scenarios and **MSMutableProtectedData** to write (and transparently encrypt) data to protected files in publishing scenarios.

## Signature

``` syntax
@interface MSMutableProtectedData : MSProtectedData
```

## Methods



| Name                                                                                                                                    | Description                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**protectedDataWithPolicy**](msmutableprotecteddata-protecteddatawithpolicy-path-completionblock-method-objc.md)<br/>           | Asynchronously creates and returns an empty **MSMutableProtectedData** object that can be used to write and protect data to the specified file.<br/>   |
| [**protectedDataInFile**](msmutableprotecteddata---protecteddatainfile-withprotectionpolicy-completionblock-method-objc.md)<br/> | Protects the receiver's data and creates a new **MSMutableProtectedData** object with the protected data and its metadata.<br/>                        |
| [**appendBytes**](msmutableprotecteddata-appendbytes-length-error-method-objc.md)<br/>                                           | Appends the specified number of plaintext bytes from a given buffer to the receiver.<br/>                                                              |
| [**appendData**](msmutableprotecteddata-appenddata-error-method-objc.md)<br/>                                                    | Appends the content of another plaintext object to the receiver.<br/>                                                                                  |
| [**updateData**](msmutableprotecteddata-updatedata-error-method-objc.md)<br/>                                                    | Replaces the entire protected contents of the receiver with the contents of another data object.<br/>                                                  |
| [**close**](msmutableprotecteddata-close--method-objc.md)<br/>                                                                   | Writes and finalizes the protection of any remaining data, smaller than the block size, that is left over from preceding append and update calls.<br/> |
| [**synchronizeFile**](msmutableprotecteddata-synchronizefile-method-objc.md)<br/>                                                | Causes all in-memory data and attributes of the file represented by the receiver to be written to persistent storage.<br/>                             |



 

## Defined in

MSMutableProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 





 

## Remarks

The methods of the **MSMutableProtectedData** class that write data transparently encrypt the plaintext data.

[**MSProtectedData**](msprotecteddata-interface-objc.md) and **MSMutableProtectedData** are used to read and write files that are protected with the Microsoft Protected File format. To read and write data for files that are protected with a custom protected file format, use [**MSCustomProtectedData**](mscustomprotecteddata-interface-objc.md) and [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





