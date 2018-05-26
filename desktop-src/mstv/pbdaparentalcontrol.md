---
title: PBDAParentalControl structure
description: Specifies the parental control policy for a digital television program.
ms.assetid: 4086651b-45b3-4896-9ae2-6db7e121eb5e
keywords:
- PBDAParentalControl structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- PBDAParentalControl
api_location:
- bdamedia.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PBDAParentalControl structure

Specifies the parental control policy for a digital television program.

## Syntax


```C++
typedef struct _PBDAParentalControl {
  ULONG ulStartTime;
  ULONG ulEndTime;
  ULONG ulPolicy;
} PBDAParentalControl;
```



## Members

<dl> <dt>

**ulStartTime**
</dt> <dd>

The start time when parental access is required, in seconds from midnight.

</dd> <dt>

**ulEndTime**
</dt> <dd>

The end time when parental access is longer required, in seconds from midnight.

</dd> <dt>

**ulPolicy**
</dt> <dd>

A member of the [**PBDAParentalControlPolicy**](pbdaparentalcontrolpolicy.md) enumeration.

</dd> </dl>

## Remarks

If parental access is not required, the **ulStartTime** and **ulEndTime** members are set to -1.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





