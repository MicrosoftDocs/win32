---
title: MPSTATUS_DATA structure (MpClient.h)
description: Contains data about the current status of a component of the product.
ms.assetid: 6AEF485C-30D1-47DB-92B6-048B8CAA7833
keywords:
- MPSTATUS_DATA structure Legacy Windows Environment Features
- PMPSTATUS_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSTATUS_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSTATUS\_DATA structure

Contains data about the current status of a component of the product.

## Syntax


```C++
typedef struct tagMPSTATUS_DATA {
  MPCOMPONENT_ID ComponentID;
  BOOL           fEnable;
  union {
    PMPSTATUS_DATAEX_UNUSED p1;
    PMPSTATUS_DATAEX_UNUSED p2;
    PMPSTATUS_DATAEX_UNUSED p3;
    PMPSTATUS_DATAEX_UNUSED p4;
    PMPSTATUS_DATAEX_UNUSED p5;
    PMPSTATUS_DATAEX_UNUSED p6;
    PMPSTATUS_DATAEX_UNUSED p7;
    PMPSTATUS_DATAEX_UNUSED p8;
    PMPSTATUS_DATAEX_UNUSED p9;
    PMPSTATUS_DATAEX_UNUSED pa;
    PMPSTATUS_DATAEX_UNUSED pb;
  } ComponentStatus;
} MPSTATUS_DATA, *PMPSTATUS_DATA;
```



## Members

<dl> <dt>

**ComponentID**
</dt> <dd>

Type: **[**MPCOMPONENT\_ID**](mpcomponent-id.md)**

</dd> <dd>

Specific component ID for which status is reported.

</dd> <dt>

**fEnable**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Status requested for the component. **hResult** in the callback data signifies success or failure for the request.

</dd> <dt>

**ComponentStatus**
</dt> <dd>

Extra status data depending on value of **ComponentID**.

> [!Note]  
> Currently results in a pointer to a dummy structure for all possible values of **ComponentID**.

 

<dl> <dt>

**p1**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_AS\_SIGNATURE**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p2**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_AV\_SIGNATURE**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p3**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_REALTIME\_MONITOR**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p4**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_ONACCESS\_PROTECTION**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p5**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_IOAV\_PROTECTION**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p6**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_BEHAVIOR\_MONITOR**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p7**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_AUTO\_SCAN**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p8**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_AUTO\_SIGUPDATE**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**p9**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_IPC**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**pa**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_NIS**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> <dt>

**pb**
</dt> <dd>

Type: **PMPSTATUS\_DATAEX\_UNUSED**

</dd> <dd>

When **ComponentID** == **MPCOMPONENT\_ELAM**. See [**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md).

</dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPCOMPONENT\_ID**](mpcomponent-id.md)
</dt> <dt>

[**MPSTATUS\_DATAEX\_UNUSED**](mpstatus-dataex-unused.md)
</dt> </dl>

 

 





