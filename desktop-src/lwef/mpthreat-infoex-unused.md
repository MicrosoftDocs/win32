---
title: MPTHREAT_INFOEX_UNUSED structure (MpClient.h)
description: Dummy structure for non-behavior modification type threats.
ms.assetid: 3C5305CD-D533-47B5-ADD3-BD8DA05F2046
keywords:
- MPTHREAT_INFOEX_UNUSED structure Legacy Windows Environment Features
- PMPTHREAT_INFOEX_UNUSED structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_INFOEX_UNUSED
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_INFOEX\_UNUSED structure

Dummy structure for non-behavior modification type threats.

## Syntax


```C++
typedef struct tagMPTHREAT_INFOEX_UNUSED {
  DWORD dwNone;
} MPTHREAT_INFOEX_UNUSED, *PMPTHREAT_INFOEX_UNUSED;
```



## Members

<dl> <dt>

**dwNone**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





