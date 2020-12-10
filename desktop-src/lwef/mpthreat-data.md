---
title: MPTHREAT_DATA structure (MpClient.h)
description: Notification data passed due to threat detection or modification.
ms.assetid: 07A2F88B-9D58-44EC-86D0-BDCC1DF44B94
keywords:
- MPTHREAT_DATA structure Legacy Windows Environment Features
- PMPTHREAT_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_DATA structure

Notification data passed due to threat detection or modification.

## Syntax


```C++
typedef struct tagMPTHREAT_DATA {
  MPTHREAT_ID     ThreatID;
  DWORD           dwSessionID;
  MPTHREAT_ACTION ThreatAction;
  DWORD           dwStatus;
} MPTHREAT_DATA, *PMPTHREAT_DATA;
```



## Members

<dl> <dt>

**ThreatID**
</dt> <dd>

Type: **MPTHREAT\_ID**

</dd> <dd>

Threat identifier. Upper bit is set to identify antivirus-related threats.

</dd> <dt>

**dwSessionID**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Session associated with the threat. Set to -1 if no session specific information is available.

</dd> <dt>

**ThreatAction**
</dt> <dd>

Type: **[**MPTHREAT\_ACTION**](mpthreat-action.md)**

</dd> <dd>

Threat action tried for the **MPNOTIFY\_THREAT\_CLEAN\_SUCCEEDED**/**MPNOTIFY\_THREAT\_CLEAN\_FAILED** events.

</dd> <dt>

**dwStatus**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Additional status or actions associated with the action taken. This is a combination of bit flags from [**MPSTATUS\_FLAG**](mpstatus-flag.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPSTATUS\_FLAG**](mpstatus-flag.md)
</dt> <dt>

[**MPTHREAT\_ACTION**](mpthreat-action.md)
</dt> </dl>

 

 





