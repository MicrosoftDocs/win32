---
title: MSUserPolicyCreationOptions enum
description: User policy creation option flags.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '0743FD52-B6E8-4364-9CB3-85D47A0C1367'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSUserPolicyCreationOptions enum"]
topic_type:
- apiref
api_name:
- MSUserPolicyCreationOptions enum
api_type:
- NA
---

# MSUserPolicyCreationOptions enum

User policy creation option flags.

## Signature

``` syntax
typedef enum MSUserPolicyCreationOptions : NSUInteger {
    None = 0x0,
    AllowAuditedExtraction = 0x1, 
    PreferDeprecatedAlgorithms = 0x2 
    
} MSUserPolicyCreationOptions;
```

## Members



| Member                                    | Value        | Notes                                                                                         |
|-------------------------------------------|--------------|-----------------------------------------------------------------------------------------------|
| **None**<br/>                       | 0<br/> | No options set<br/>                                                                     |
| **AllowAuditedExtraction**<br/>     | 1<br/> | Specifies whether the content can be opened in a non-RMS aware app or not<br/>          |
| **PreferDeprecatedAlgorithms**<br/> | 2<br/> | Specifies whether the [deprecated algorithms](terms.md) (ECB) is preferred or not<br/> |



 

## Defined in

TBD

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





