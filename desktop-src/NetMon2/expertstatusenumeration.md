---
description: The EXPERTSTATUSENUMERATION enumeration contains status values. It is used by the Status member of EXPERTSTATUS structure and the Status parameter in ExpertIndicateStatus.
ms.assetid: 217dce5a-3698-45a9-bb13-8379bcbdd762
title: EXPERTSTATUSENUMERATION enumeration (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXPERT_STATUS_ENUMERATION
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# EXPERTSTATUSENUMERATION enumeration

The **EXPERTSTATUSENUMERATION** enumeration contains status values. It is used by the **Status** member of [EXPERTSTATUS](expertstatus.md) structure and the *Status* parameter in [ExpertIndicateStatus](expertindicatestatus.md).

## Syntax


```C++
typedef enum  { 
  EXPERTSTATUS_INACTIVE  = 0,
  EXPERTSTATUS_STARTING,
  EXPERTSTATUS_RUNNING,
  EXPERTSTATUS_PROBLEM,
  EXPERTSTATUS_ABORTED,
  EXPERTSTATUS_DONE
} EXPERT_STATUS_ENUMERATION;
```



## Constants

<dl> <dt>

<span id="EXPERTSTATUS_INACTIVE"></span><span id="expertstatus_inactive"></span>**EXPERTSTATUS\_INACTIVE**
</dt> <dd>

The expert never started.

</dd> <dt>

<span id="EXPERTSTATUS_STARTING"></span><span id="expertstatus_starting"></span>**EXPERTSTATUS\_STARTING**
</dt> <dd>

The expert is starting.

</dd> <dt>

<span id="EXPERTSTATUS_RUNNING"></span><span id="expertstatus_running"></span>**EXPERTSTATUS\_RUNNING**
</dt> <dd>

The expert is running normally.

</dd> <dt>

<span id="EXPERTSTATUS_PROBLEM"></span><span id="expertstatus_problem"></span>**EXPERTSTATUS\_PROBLEM**
</dt> <dd>

A problem specified in *SubStatus* stopped the expert.

</dd> <dt>

<span id="EXPERTSTATUS_ABORTED"></span><span id="expertstatus_aborted"></span>**EXPERTSTATUS\_ABORTED**
</dt> <dd>

Network Monitor stopped the expert.

</dd> <dt>

<span id="EXPERTSTATUS_DONE"></span><span id="expertstatus_done"></span>**EXPERTSTATUS\_DONE**
</dt> <dd>

The expert finished successfully.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




