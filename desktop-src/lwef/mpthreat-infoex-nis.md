---
title: MPTHREAT_INFOEX_NIS structure (MpClient.h)
description: Contains NIS-specific information.
ms.assetid: 3887C5BF-B1F6-4420-B40A-9585E44BE7A9
keywords:
- MPTHREAT_INFOEX_NIS structure Legacy Windows Environment Features
- PMPTHREAT_INFOEX_NIS structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_INFOEX_NIS
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_INFOEX\_NIS structure

Contains NIS-specific information.

## Syntax


```C++
typedef struct tagMPTHREAT_INFOEX_NIS {
  MP_MIDL_STRING LPWSTR SourceIP;
  MP_MIDL_STRING LPWSTR DestinationIP;
  DWORD                 dwSourceport;
  DWORD                 dwDestinationport;
  MP_MIDL_STRING LPWSTR Protocol;
  MP_MIDL_STRING LPWSTR Link;
} MPTHREAT_INFOEX_NIS, *PMPTHREAT_INFOEX_NIS;
```



## Members

<dl> <dt>

**SourceIP**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd></dd> <dt>

**DestinationIP**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd></dd> <dt>

**dwSourceport**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> <dt>

**dwDestinationport**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> <dt>

**Protocol**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd></dd> <dt>

**Link**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





