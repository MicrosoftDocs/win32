---
title: MSMutableProtectedData appendBytes length error method
description: Appends the specified number of plaintext bytes from a given buffer to the receiver.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'b7c86d11-fdeb-4a79-aa7e-a410cb4f0d3c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSMutableProtectedData appendBytes length error method"]
topic_type:
- apiref
api_name:
- MSMutableProtectedData appendBytes length error method
api_type:
- NA
---

# MSMutableProtectedData appendBytes:length:error method

Appends the specified number of plaintext bytes from a given buffer to the receiver. First the bytes are encrypted, and then the cipher text bytes are appended to the receiver.

## Signature

``` syntax
- (BOOL)appendBytes:(const void *)bytes length:(NSUInteger)length error:(NSError **)errorPtr;
```

## Parameters



| Name                  | Datatype                     | Notes                                                                                          |
|-----------------------|------------------------------|------------------------------------------------------------------------------------------------|
| *bytes*<br/>    | **const void** \*<br/> | Required. The buffer that contains the plaintext data to be encrypted and appended.<br/> |
| *length*<br/>   | **NSUInteger**<br/>    | Required. The number of bytes to copy.<br/>                                              |
| *errorPtr*<br/> | **NSError** \*\*<br/>  | Optional. If an error occurs, contains the error code and details.<br/>                  |



 

## Returns

Type: **BOOL**

**YES** if the operation is successful; otherwise, **NO**. If the operation isn't successful, the *errorPtr* parameter references an **NSError** object that contains more information about the error.

## Defined in

MSMutableProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

The specified number of bytes are copied from the buffer, encrypted, and appended to the receiver's data.

 

 





