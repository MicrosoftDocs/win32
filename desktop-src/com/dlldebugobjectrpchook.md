---
title: DllDebugObjectRPCHook function
description: Exported by COM DLLs to enable remote debugging.
ms.assetid: a0f8bf12-0889-452d-84d0-255c5c143bc1
keywords:
- DllDebugObjectRPCHook function COM
topic_type:
- apiref
api_name:
- DllDebugObjectRPCHook
api_location:
- ole32.dll
- API-MS-Win-Core-Com-private-l1-1-0.dll
- ComBase.dll
- API-MS-Win-Core-COM-Private-l1-1-1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DllDebugObjectRPCHook function

Exported by COM DLLs to enable remote debugging.

## Syntax


```C++
BOOL WINAPI DllDebugObjectRPCHook(
   BOOL             fTrace,
   LPORPC_INIT_ARGS lpOrpcInitArgs
);
```



## Parameters

<dl> <dt>

*fTrace* 
</dt> <dd>

If **TRUE**, remote debugging is enabled. If **FALSE**, remote debugging is not enabled.

</dd> <dt>

*lpOrpcInitArgs* 
</dt> <dd>

A pointer to an [**ORPC\_INIT\_ARGS**](orpc-init-args.md) structure.

</dd> </dl>

## Return value

**TRUE** if successful, **FALSE** otherwise

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>N/A</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Ole32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ole32.dll</dt> </dl> |



## See also

<dl> <dt>

[**ORPC\_DBG\_ALL**](orpc-dbg-all.md)
</dt> <dt>

[**ORPC\_DBG\_BUFFER**](orpc-dbg-buffer.md)
</dt> <dt>

[**ORPC\_INIT\_ARGS**](orpc-init-args.md)
</dt> <dt>

[**IOrpcDebugNotify**](iorpcdebugnotify.md)
</dt> </dl>

 

 





