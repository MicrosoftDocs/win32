---
title: MPCLEAN_DATA structure (MpClient.h)
description: Notification data passed to clean callback function.
ms.assetid: 475A6525-5BD8-4B29-A684-53EE2758C790
keywords:
- MPCLEAN_DATA structure Legacy Windows Environment Features
- PMPCLEAN_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPCLEAN_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPCLEAN\_DATA structure

Notification data passed to clean callback function.

## Syntax


```C++
typedef struct tagMPCLEAN_DATA {
  MPTHREAT_ID      ThreatID;
  MPTHREAT_ACTION  ThreatAction;
  DWORD            dwStatus;
  PMPRESOURCE_INFO ResourceInfo;
} MPCLEAN_DATA, *PMPCLEAN_DATA;
```



## Members

<dl> <dt>

**ThreatID**
</dt> <dd>

Type: **MPTHREAT\_ID**

</dd> <dd>

Threat identifier for the **MPNOTIFY\_CLEAN\_THREAT\_START**/**MPNOTIFY\_CLEAN\_THREAT\_SUCCEEDED**/**MPNOTIFY\_CLEAN\_THREAT\_FAILED** events. Upper bit is set to identify antivirus-related threats.

</dd> <dt>

**ThreatAction**
</dt> <dd>

Type: **[**MPTHREAT\_ACTION**](mpthreat-action.md)**

</dd> <dd>

Threat action for the **MPNOTIFY\_CLEAN\_THREAT\_START**/**MPNOTIFY\_CLEAN\_THREAT\_SUCCEEDED**/**MPNOTIFY\_CLEAN\_THREAT\_FAILED** events. See [**MPTHREAT\_ACTION**](mpthreat-action.md).

</dd> <dt>

**dwStatus**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Additional status or actions associated with the action taken. This is a combination of bit flags from [**MPSTATUS\_FLAG**](mpstatus-flag.md).

</dd> <dt>

**ResourceInfo**
</dt> <dd>

Type: **PMPRESOURCE\_INFO**

</dd> <dd>

Resource information for the **MPNOTIFY\_CLEAN\_THREAT\_START**/**MPNOTIFY\_CLEAN\_THREAT\_SUCCEEDED**/**MPNOTIFY\_CLEAN\_THREAT\_FAILED** events. See [**MPRESOURCE\_INFO**](mpresource-info.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPRESOURCE\_INFO**](mpresource-info.md)
</dt> <dt>

[**MPSTATUS\_FLAG**](mpstatus-flag.md)
</dt> <dt>

[**MPTHREAT\_ACTION**](mpthreat-action.md)
</dt> </dl>

 

 





