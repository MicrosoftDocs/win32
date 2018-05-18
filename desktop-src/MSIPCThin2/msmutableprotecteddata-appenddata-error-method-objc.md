---
title: MSMutableProtectedData appendData error method
description: Appends the content of another plaintext object to the receiver.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'b6c4c94c-eb53-453c-af58-a978b5f4a6b9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSMutableProtectedData appendData error method"]
topic_type:
- apiref
api_name:
- MSMutableProtectedData appendData error method
api_type:
- NA
---

# MSMutableProtectedData appendData:error method

Appends the content of another plaintext object to the receiver. First the data object is protected, and then the cipher text data is appended to the receiver.

## Signature

``` syntax
- (BOOL)appendData:(NSData *)other error:(NSError **)errorPtr;
```

## Parameters



| Name                  | Datatype                    | Notes                                                                                            |
|-----------------------|-----------------------------|--------------------------------------------------------------------------------------------------|
| *other*<br/>    | **NSData** \*<br/>    | Required. The data object containing the plaintext data to be protected and appended.<br/> |
| *errorPtr*<br/> | **NSError** \*\*<br/> | Optional. If an error occurs, contains the error code and details.<br/>                    |



 

## Returns

Type: **BOOL**

**YES** if the operation is successful; otherwise, **NO**. If the operation isn't successful, the *errorPtr* parameter references an **NSError** object that contains more information about the error.

## Defined in

MSMutableProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





