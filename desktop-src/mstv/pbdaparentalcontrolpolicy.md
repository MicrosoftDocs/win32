---
title: PBDAParentalControlPolicy enumeration
description: Contains flags that describe parental control policy.
ms.assetid: bfd9da34-50e4-4e67-a17e-9f6366e5ef46
keywords:
- PBDAParentalControlPolicy enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- PBDAParentalControlPolicy
api_location:
- bdamedia.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PBDAParentalControlPolicy enumeration

Contains flags that describe parental control policy.

## Syntax


```C++
typedef enum  { 
  PBDAParentalControlGeneralPolicy   = 0,
  PBDAParentalControlLiveOnlyPolicy  = 1
} PBDAParentalControlPolicy;
```



## Constants

<dl> <dt>

<span id="PBDAParentalControlGeneralPolicy"></span><span id="pbdaparentalcontrolgeneralpolicy"></span><span id="PBDAPARENTALCONTROLGENERALPOLICY"></span>**PBDAParentalControlGeneralPolicy**
</dt> <dd>

The policy applies for general content access.

</dd> <dt>

<span id="PBDAParentalControlLiveOnlyPolicy"></span><span id="pbdaparentalcontrolliveonlypolicy"></span><span id="PBDAPARENTALCONTROLLIVEONLYPOLICY"></span>**PBDAParentalControlLiveOnlyPolicy**
</dt> <dd>

The policy applies only while the content is being recorded.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





