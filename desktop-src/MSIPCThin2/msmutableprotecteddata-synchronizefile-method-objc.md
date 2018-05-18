---
title: MSMutableProtectedData synchronizeFile method
description: Causes all in-memory data and attributes of the file represented by the receiver to be written to persistent storage.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '07eada60-290a-4129-bc04-9ce6e8ca0ede'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSMutableProtectedData synchronizeFile method"]
topic_type:
- apiref
api_name:
- MSMutableProtectedData synchronizeFile method
api_type:
- NA
---

# MSMutableProtectedData synchronizeFile method

Causes all in-memory data and attributes of the file represented by the receiver to be written to persistent storage. This method should be invoked by apps that require the file to always be in a known state. An invocation of this method does not return until memory is flushed.

## Signature

``` syntax
- (void)synchronizeFile;
```

## Defined in

MSMutableProtectedData.h

## Supported Platforms



|                                             |                                  |
|---------------------------------------------|----------------------------------|
| **Minimum supported OS version**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

Because protection finalizes its state by calling the [**close**](msmutableprotecteddata-close--method-objc.md) function, any remaining data smaller than the block size will not be flushed.

 

 





