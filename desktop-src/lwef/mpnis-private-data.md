---
title: MPNIS_PRIVATE_DATA structure (MpClient.h)
description: Private NIS notifications.
ms.assetid: 19B4928F-BC78-4DEA-A563-1516B6454465
keywords:
- MPNIS_PRIVATE_DATA structure Legacy Windows Environment Features
- PMPNIS_PRIVATE_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPNIS_PRIVATE_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPNIS\_PRIVATE\_DATA structure

Private NIS notifications.

## Syntax


```C++
typedef struct tagMPNIS_PRIVATE_DATA {
  DWORD dwNotificationType;
  DWORD cbDataSize;
  BYTE  *pbData;
} MPNIS_PRIVATE_DATA, *PMPNIS_PRIVATE_DATA;
```



## Members

<dl> <dt>

**dwNotificationType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Type of notification.

</dd> <dt>

**cbDataSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of reserved data, in bytes.

</dd> <dt>

**pbData**
</dt> <dd>

Type: **BYTE\***

</dd> <dd>

Pointer to reserved data.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





