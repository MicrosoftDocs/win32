---
title: MPSAMPLE_DATA structure (MpClient.h)
description: Notification data passed to the sample submission callback function.
ms.assetid: 58F348C6-411D-4545-9D4D-A80095FD139B
keywords:
- MPSAMPLE_DATA structure Legacy Windows Environment Features
- PMPSAMPLE_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSAMPLE_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSAMPLE\_DATA structure

Notification data passed to the sample submission callback function.

## Syntax


```C++
typedef struct tagMPSAMPLE_DATA {
  DWORD dwSampleIndex;
} MPSAMPLE_DATA, *PMPSAMPLE_DATA;
```



## Members

<dl> <dt>

**dwSampleIndex**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Index of the sample item for which the submission status is reported.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





