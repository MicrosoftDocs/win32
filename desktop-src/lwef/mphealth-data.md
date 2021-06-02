---
title: MPHEALTH_DATA structure (MpClient.h)
description: Health notification data.
ms.assetid: 37A87F77-386A-4508-B338-ED2151518968
keywords:
- MPHEALTH_DATA structure Legacy Windows Environment Features
- PMPHEALTH_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPHEALTH_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPHEALTH\_DATA structure

Health notification data.

## Syntax


```C++
typedef struct tagMPHEALTH_DATA {
  DWORD dwNotificationType;
  DWORD dwNotificationFlag;
} MPHEALTH_DATA, *PMPHEALTH_DATA;
```



## Members

<dl> <dt>

**dwNotificationType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Type of notification.

</dd> <dt>

**dwNotificationFlag**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Unused.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





