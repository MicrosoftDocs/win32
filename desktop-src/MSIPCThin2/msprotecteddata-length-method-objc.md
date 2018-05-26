---
title: MSProtectedData length method
description: Returns the number of bytes contained in the receiver.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: b4862bd9-dcbc-4036-a5a1-ce501b3ec668
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSProtectedData length method
topic_type:
- apiref
api_name:
- MSProtectedData length method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSProtectedData length method

Returns the number of bytes contained in the receiver.

## Signature

``` syntax
- (int64_t)length:(NSError **)errorPtr;
```

## Parameters



| Name                  | Datatype                    | Notes                                                            |
|-----------------------|-----------------------------|------------------------------------------------------------------|
| *errorPtr*<br/> | **NSError** \*\*<br/> | Optional. If an error occurs, contains error details.<br/> |



 

## Returns

Type: **int64\_t**

The number of bytes of the plaintext data contained in the protected file (not including the metadata and the publishing license).

## Defined in

MSProtectedData.h

## Supported Platforms



|                                              |                                 |
|----------------------------------------------|---------------------------------|
| **Minimum supported OS versions**<br/> | OS 6.0 and OS X 10.8<br/> |



 

 

 





