---
title: MSProtectedData class
description: MSProtectedData and its mutable subclass MSMutableProtectedData provide protected file data objects, object-oriented wrappers for files that are protected using the Microsoft Protected File format.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '586ac0f1-43d3-4111-b7e2-f9ffbe4606a1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSProtectedData class"]
topic_type:
- apiref
api_name:
- MSProtectedData class
api_type:
- NA
---

# MSProtectedData class

**MSProtectedData** and its mutable subclass [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) provide protected file data objects, object-oriented wrappers for files that are protected using the Microsoft Protected File format. Use **MSProtectedData** to read (and transparently decrypt) protected files in consumption scenarios and [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) to write (and transparently encrypt) data to protected files in publishing scenarios.

## Signature

``` syntax
@interface MSProtectedData : NSSecureCodableObject
```

## Properties



| Name                                                                              | Description                                      |
|-----------------------------------------------------------------------------------|--------------------------------------------------|
| [**originalFileExtension**](msprotecteddata-originalfileextension.md)<br/> | The file extension before encryption.<br/> |
| [**userPolicy**](msprotecteddata-userpolicy-property-objc.md)<br/>         | Gets the user policy.<br/>                 |



 

## Methods



| Name                                                                                                                            | Description                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**protectedDataWithProtectedFile**](msprotecteddata-protecteddatawithprotectedfile-completionblock-method-objc.md)<br/> | Asynchronously creates and returns a protected file data object that can be used to read (and decrypt) data from a file protected with Microsoft Protected File format.<br/>                                                    |
| [**getBytes:length**](msprotecteddata-getbytes-length-error-method-objc.md)<br/>                                         | Copies the specified number of plaintext bytes from the start of the receiver’s data into a given buffer. Decryption is transparently performed during the execution of the method.<br/>                                        |
| [**getBytes:range**](msprotecteddata-getbytes-range-error-method-objc.md)<br/>                                           | Copies a range of plaintext bytes from the receiver’s data into a given buffer. Decryption is transparently performed during the execution of the method.<br/>                                                                  |
| [**length**](msprotecteddata-length-method-objc.md)<br/>                                                                 | Returns the number of bytes contained in the receiver.<br/>                                                                                                                                                                     |
| [**retrieveData**](msprotecteddata-retrievedata-method-objc.md)<br/>                                                     | Returns an **NSData** data object that contains a copy of all of the receiver’s plaintext bytes. Decryption is transparently performed during the execution of the method.<br/>                                                 |
| [**subdataWithRange**](msprotecteddata-subdatawithrange-method-objc.md)<br/>                                             | Returns an **NSData** data object that contains a copy of the receiver’s plaintext bytes that fall within the limits specified by a given range. Decryption is transparently performed during the execution of the method.<br/> |



 

## Defined in

MSProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 





 

## Remarks

The methods of the **MSProtectedData** class that read data transparently decrypt the protected content and return plaintext data.

**MSProtectedData** and [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) are used to read and write files that are protected with the Microsoft Protected File format. To read and write data for files that are protected with a custom protected file format, use [**MSCustomProtectedData**](mscustomprotecteddata-interface-objc.md) and [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





