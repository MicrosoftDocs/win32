---
title: ORPC_INIT_ARGS structure
description: The ORPC\_INIT\_ARGS structure contains information used to initialize remote debugging using the IOrpcDebugNotify interface.
ms.assetid: be7646c7-3394-45ae-ae8f-9cee68bbc789
keywords:
- ORPC_INIT_ARGS structure COM
- LPORPC_INIT_ARGS structure pointer COM
topic_type:
- apiref
api_name:
- ORPC_INIT_ARGS
api_location:
- N/A
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ORPC\_INIT\_ARGS structure

The **ORPC\_INIT\_ARGS** structure contains information used to initialize remote debugging using the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface.

## Syntax


```C++
typedef struct ORPC_INIT_ARGS {
  IOrpcDebugNotify *lpIntfOrpcDebug;
  void             *pvPSN;
  DWORD            *dwReserved1;
  DWORD            *dwReserved2;
} ORPC_INIT_ARGS, *LPORPC_INIT_ARGS;
```



## Members

<dl> <dt>

**lpIntfOrpcDebug**
</dt> <dd>

A pointer to the [**IOrpcDebugNotify**](iorpcdebugnotify.md) interface for use by in-process debuggers. If the debugger is not in-process or is a Macintosh system, this field must be **NULL**.

</dd> <dt>

**pvPSN**
</dt> <dd>

A pointer to the Macintosh process serial number of the debuggee's process. If the debuggee is not a Macintosh system, this field must be **NULL**.

</dd> <dt>

**dwReserved1**
</dt> <dd>

Reserved. Must be 0.

</dd> <dt>

**dwReserved2**
</dt> <dd>

Reserved. Must be 0.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>N/A</dt> </dl> |



## See also

<dl> <dt>

[**ORPC\_DBG\_ALL**](orpc-dbg-all.md)
</dt> <dt>

[**ORPC\_DBG\_BUFFER**](orpc-dbg-buffer.md)
</dt> <dt>

[**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md)
</dt> <dt>

[**IOrpcDebugNotify**](iorpcdebugnotify.md)
</dt> </dl>

 

 





