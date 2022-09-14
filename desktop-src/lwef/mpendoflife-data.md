---
title: MPENDOFLIFE_DATA structure (MpClient.h)
description: '\ 0034;End of life \ 0034; notification data.'
ms.assetid: 00C2E707-9034-4BBC-99CF-3DFA4B8C08D9
keywords:
- MPENDOFLIFE_DATA structure Legacy Windows Environment Features
- PMPENDOFLIFE_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPENDOFLIFE_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPENDOFLIFE\_DATA structure

"End of life" notification data.

## Syntax


```C++
typedef struct tagMPENDOFLIFE_DATA {
  FILETIME ftSignatureExpiry;
  FILETIME ftPlatformExpiry;
  BOOL     fAdminControlled;
  BOOL     fEndOfLifeImpendingOrPast;
} MPENDOFLIFE_DATA, *PMPENDOFLIFE_DATA;
```



## Members

<dl> <dt>

**ftSignatureExpiry**
</dt> <dd>

Type: **FILETIME**

</dd> <dd>

Time when the signature expires.

</dd> <dt>

**ftPlatformExpiry**
</dt> <dd>

Type: **FILETIME**

</dd> <dd>

Time when the platform expires.

</dd> <dt>

**fAdminControlled**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

True if the administrator controlling the policy for showing the notification. If set, this tells the UI to not show the EOL notification.

</dd> <dt>

**fEndOfLifeImpendingOrPast**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

True if "End of Life" is pending or past. If false, UI and clients can clear any EOL related states.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





