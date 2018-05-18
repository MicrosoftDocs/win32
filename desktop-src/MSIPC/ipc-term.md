---
title: IPC\_TERM structure
description: Describes a period of time based on a start time and duration.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '43c78a2f-f446-4b58-9634-3a36c3eae17f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_TERM structure Active Directory Rights Management Services SDK 2.0", "PIPC_TERM structure pointer Active Directory Rights Management Services SDK 2.0", "PCIPC_TERM structure pointer Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_TERM
api_location:
- Ipcprot.h
api_type:
- HeaderDef
---

# IPC\_TERM structure

Describes a period of time based on a start time and duration.

## Syntax


```C++
typedef struct _IPC_TERM {
  FILETIME ftStart;
  DWORD64  qwDuration;
} IPC_TERM, *PIPC_TERM;typedef const IPC_TERM *PCIPC_TERM;
```



## Members

<dl> <dt>

**ftStart**
</dt> <dd>

The beginning of the time period specified in the number of 100-nanosecond intervals since January 1, 1601 (UTC). For more information, see the [FILETIME](https://msdn.microsoft.com/library/windows/desktop/ms724284.aspx) structure.

</dd> <dt>

**qwDuration**
</dt> <dd>

The duration of the time period in 100-nanosecond intervals.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[FILETIME](https://msdn.microsoft.com/library/windows/desktop/ms724284.aspx)
</dt> </dl>

 

 





