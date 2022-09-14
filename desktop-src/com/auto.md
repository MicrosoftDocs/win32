---
title: Auto
description: Determines if the debugger is automatically launched when a COM RPC notification is sent.
ms.assetid: e05ae7cb-79d1-4543-aef3-9397548c2030
ms.topic: article
ms.date: 05/31/2018
---

# Auto

Determines if the debugger is automatically launched when a COM RPC notification is sent.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\DebugObjectRPCEnabled\AeDebug
   Auto = value
```

## Remarks

This is a **REG\_WORD** value.



| Value | Description                    |
|-------|--------------------------------|
| 1     | Automatically launch debugger. |



 

## Related topics

<dl> <dt>

[**DllDebugObjectRPCHook**](dlldebugobjectrpchook.md)
</dt> <dt>

[**IOrpcDebugNotify**](iorpcdebugnotify.md)
</dt> <dt>

[**ORPC\_DBG\_ALL**](orpc-dbg-all.md)
</dt> </dl>

 

 




