---
description: The NETWORKSTATUS structure describes the current status of the NPP.
ms.assetid: e5e07480-cfc3-408f-9ca2-48a697e4b875
title: NETWORKSTATUS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NETWORKSTATUS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# NETWORKSTATUS structure

The **NETWORKSTATUS** structure describes the current status of the NPP.

## Syntax


```C++
typedef struct _NETWORKSTATUS {
  DWORD State;
  DWORD Flags;
} NETWORKSTATUS, *LPNETWORKSTATUS;
```



## Members

<dl> <dt>

**State**
</dt> <dd>

Indicates the current state of the NPP.



| Value                                                                                                                                                                                                          | Meaning                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span id="NETWORKSTATUS_STATE_VOID"></span><span id="networkstatus_state_void"></span><dl> <dt>**NETWORKSTATUS\_STATE\_VOID**</dt> </dl>                | The NPP is not connected, or it is connected and the capture is not started.<br/> |
| <span id="NETWORKSTATUS_STATE_CAPTURING"></span><span id="networkstatus_state_capturing"></span><dl> <dt>**NETWORKSTATUS\_STATE\_CAPTURING**</dt> </dl> | The NPP is capturing data.<br/>                                                   |
| <span id="NETWORKSTATUS_STATE_PAUSED"></span><span id="networkstatus_state_paused"></span><dl> <dt>**NETWORKSTATUS\_STATE\_PAUSED**</dt> </dl>          | The NPP has paused while capturing data.<br/>                                     |



 

</dd> <dt>

**Flags**
</dt> <dd>

Flags that describe the current state of the NPP.



| Value                                                                                                                                                                                                                             | Meaning                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <span id="NETWORKSTATUS_FLAGS_TRIGGER_PENDING"></span><span id="networkstatus_flags_trigger_pending"></span><dl> <dt>**NETWORKSTATUS\_FLAGS\_TRIGGER\_PENDING**</dt> </dl> | There is a trigger pending for the NPP.<br/> |



 

</dd> </dl>

## Remarks

When using this structure, you must allocate the memory for the structure before it can be used and free the memory when the structure is no longer needed.

The See Also list at the bottom of this topic lists all the methods that use this structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[IDelaydC::QueryStatus](idelaydc-querystatus.md)
</dt> <dt>

[IESP::QueryStatus](iesp-querystatus.md)
</dt> <dt>

[IRTC::QueryStatus](irtc-querystatus.md)
</dt> <dt>

[IStats::QueryStatus](istats-querystatus.md)
</dt> </dl>

 

 




