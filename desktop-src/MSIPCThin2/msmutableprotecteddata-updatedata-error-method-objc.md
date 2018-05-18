---
title: MSMutableProtectedData updateData error method
description: Replaces the entire protected contents of the receiver with the contents of another data object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'c392714b-e79f-4b93-bc32-b07d66d45090'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSMutableProtectedData updateData error method"]
topic_type:
- apiref
api_name:
- MSMutableProtectedData updateData error method
api_type:
- NA
---

# MSMutableProtectedData updateData:error method

Replaces the entire protected contents of the receiver with the contents of another data object. The new content will be protected immediately and does not including the metadata and the publishing license.

## Signature

``` syntax
- (BOOL)updateData:(NSData *)data error:(NSError **)errorPtr;
```

## Parameters



| Name                  | Datatype                    | Notes                                                                                                                       |
|-----------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| *data*<br/>     | **NSData** \*<br/>    | Required. The data object that contains the plaintext data to be protected and replace the data of the receiver.<br/> |
| *errorPtr*<br/> | **NSError** \*\*<br/> | Optional. If an error occurs, contains the error code and details.<br/>                                               |



 

## Returns

Type: **BOOL**

**YES** if the operation is successful; otherwise, **NO**. If the operation isn't successful, the *errorPtr* parameter references an **NSError** object that contains more information about the error.

## Defined in

MSMutableProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





