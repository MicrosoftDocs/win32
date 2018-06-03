---
title: IPC\_BUFFER structure
description: Represents a buffer.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 87a023ce-585f-41e8-a6a9-47e6a3044366
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_BUFFER structure Active Directory Rights Management Services SDK 2.0
- PIPC_BUFFER structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_BUFFER structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_BUFFER
api_location:
- Ipcbase.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_BUFFER structure

Represents a buffer.

## Syntax


```C++
typedef struct _IPC_BUFFER {
  LPVOID pvBuffer;
  DWORD  cbBuffer;
} IPC_BUFFER, *PIPC_BUFFER;typedef const IPC_BUFFER *PCIPC_BUFFER;
```



## Members

<dl> <dt>

**pvBuffer**
</dt> <dd>

The pointer to the buffer.

</dd> <dt>

**cbBuffer**
</dt> <dd>

The size of the buffer, in bytes.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



 

 





