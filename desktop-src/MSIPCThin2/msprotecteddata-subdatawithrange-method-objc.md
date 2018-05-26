---
title: MSProtectedData subdataWithRange method
description: Returns an NSData data object that contains a copy of the receiver s plaintext bytes that fall within the limits specified by a given range.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 9f76c5c9-e3f3-48ce-a211-c08412f52e0e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtectedData subdataWithRange method
topic_type:
- apiref
api_name:
- MSProtectedData subdataWithRange method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSProtectedData subdataWithRange method

Returns an **NSData** data object that contains a copy of the receiver s plaintext bytes that fall within the limits specified by a given range. Decryption is transparently performed during the execution of the method.

## Signature

``` syntax
- (NSData *)subdataWithRange:(NSRange)range;
```

## Parameters



| Name               | Datatype               | Description                                                                                                                                            |
|--------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| *range*<br/> | **NSRange**<br/> | Required. The range of plaintext bytes in the receiver s data to copy. The range must lie within the range of bytes of the receiver s data.<br/> |



 

## Returns

A pointer to an **NSData** object that contains a copy of the receiver s plaintext bytes that fall within the limits specified by the *range* parameter.

## Defined in

MSProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

If the range specified in the *range* parameter isn t within the receiver s range of bytes, an **NSRangeException** is raised.

## See also

<dl> <dt>

[**MSProtectedData Class**](msprotecteddata-interface-objc.md)
</dt> </dl>

 

 





