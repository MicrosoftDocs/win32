---
title: MSProtectedData getBytes range error method
description: Copies a range of plaintext bytes from the receiver’s data into a given buffer. Decryption is transparently performed during the execution of the method.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '9ae184df-4dc7-47ea-962d-c8ea4778817c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSProtectedData getBytes range error method"]
topic_type:
- apiref
api_name:
- MSProtectedData getBytes range error method
api_type:
- NA
---

# MSProtectedData getBytes:range:error method

Copies a range of plaintext bytes from the receiver’s data into a given buffer. Decryption is transparently performed during the execution of the method.

## Signature

``` syntax
- (BOOL)getBytes:(void *)buffer range:(NSRange)range error:(NSError **)errorPtr;
```

## Parameters



| Name                  | Datatype                    | Notes                                                                                                                                                                |
|-----------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *buffer*<br/>   | **void** \*<br/>      | Required. The buffer into which to copy the plaintext data.<br/>                                                                                               |
| *range*<br/>    | **NSRange**<br/>      | Required. The range of plaintext bytes in the receiver’s data to copy to the buffer. The range must lie within the range of bytes of the receiver’s data.<br/> |
| *errorPtr*<br/> | **NSError** \*\*<br/> | Optional. If an error occurs, contains the error code and details.<br/>                                                                                        |



 

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

If the range specified in the *range* parameter isn’t within the receiver’s range of bytes, an **NSRangeException** is raised.

 

 





