---
title: MSProtectedData getBytes length error method
description: Copies the specified number of plaintext bytes from the start of the receiver s data into a given buffer. Decryption is transparently performed during the execution of the method.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: fff7d7d4-e2aa-4246-8e5f-89d9d253bce7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtectedData getBytes length error method
topic_type:
- apiref
api_name:
- MSProtectedData getBytes length error method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSProtectedData getBytes:length:error method

Copies the specified number of plaintext bytes from the start of the receiver s data into a given buffer. Decryption is transparently performed during the execution of the method.

## Signature

``` syntax
- (BOOL)getBytes:(void *)buffer length:(NSUInteger)length error:(NSError **)errorPtr;
```

## Parameters



| Name                  | Datatype                    | Notes                                                                         |
|-----------------------|-----------------------------|-------------------------------------------------------------------------------|
| *buffer*<br/>   | **void** \*<br/>      | Required. The buffer into which to copy the plaintext data.<br/>        |
| *length*<br/>   | **NSUInteger**<br/>   | Required. The number of bytes to copy.<br/>                             |
| *errorPtr*<br/> | **NSError** \*\*<br/> | Optional. If an error occurs, contains the error code and details.<br/> |



 

## Returns

Type: **BOOL**

**YES** if the operation is successful; otherwise, **NO**.

## Defined in

MSProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

The specified number of bytes beginning at the start of the receiver's data are copied into the buffer. The number of bytes copied is the smaller of that specified in the *length* parameter and the data encapsulated in the object.

## See also

<dl> <dt>

[**MSProtectedData Class**](msprotecteddata-interface-objc.md)
</dt> </dl>

 

 





