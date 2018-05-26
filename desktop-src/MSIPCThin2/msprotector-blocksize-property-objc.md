---
title: MSProtector blockSize property
description: Gets the minimum block size decryption/encryption calls should use, except with the last block.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: ABC846F8-B55D-4C28-9FB1-956127DDA924
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtector blockSize property
topic_type:
- apiref
api_name:
- MSProtector blockSize property
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSProtector blockSize property

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Gets the minimum block size decryption/encryption calls should use, except with the last block.

## Signature

``` syntax
@property (readonly) uint32_t blockSize;
```

## Property Values



| Name                   | Datatype                   | Note                                  |
|------------------------|----------------------------|---------------------------------------|
| *blockSize*<br/> | **NSString** \*<br/> | Minimum block size to use.<br/> |



 

## Defined in

MSProtector.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





