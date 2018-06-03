---
title: MSCustomProtectedData getEncryptedContentLengthWithPolicy policy contentLength
description: Returns the length of the encrypted content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 8C55C908-EEC3-493E-B9AC-A96856C9D801
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSCustomProtectedData getEncryptedContentLengthWithPolicy policy contentLength
topic_type:
- apiref
api_name:
- MSCustomProtectedData getEncryptedContentLengthWithPolicy policy contentLength
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCustomProtectedData getEncryptedContentLengthWithPolicy:policy:contentLength

Returns the length of the encrypted content.

## Signature

``` syntax
+ (NSUInteger)getEncryptedContentLengthWithPolicy:(MSUserPolicy *)policy 
                                    contentLength:(NSUInteger)contentLength;
```

## Parameters



| Name                       | Datatype                                                          | Notes                                                                                  |
|----------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| *policy*<br/>        | [**MSUserPolicy**](msuserpolicy-interface-objc.md) \*<br/> | Required. Pointer to the user policy for which you want the content length.<br/> |
| *contentLength*<br/> | **NSUInteger**<br/>                                         | Required. The length of the content.<br/>                                        |



 

## Returns

The encrypted content length as an **NSUInteger**.

## Defined in

MSCustomProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





