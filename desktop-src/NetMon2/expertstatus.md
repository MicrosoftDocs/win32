---
description: Indicates the current status of a running expert.
ms.assetid: 49107459-599c-4710-8935-4b2c789081de
title: EXPERTSTATUS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXPERTSTATUS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# EXPERTSTATUS structure

The **EXPERTSTATUS** structure indicates the current status of a running expert.

## Syntax


```C++
typedef struct {
  EXPERTSTATUSENUMERATION Status;
  DWORD                   SubStatus;
  DWORD                   PercentDone;
  DWORD                   Frame;
  char                    szStatusText[EXPERTSTRINGLENGTH];
} EXPERTSTATUS, *PEXPERTSTATUS;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

Current expert status value defined by the [**EXPERTSTATUSENUMERATION**](expertstatusenumeration.md) enumeration.

</dd> <dt>

**SubStatus**
</dt> <dd>

Sub-status value.

</dd> <dt>

**PercentDone**
</dt> <dd>

Percentage completion of the expert analysis of network data.

</dd> <dt>

**Frame**
</dt> <dd>

Frame number.

</dd> <dt>

**szStatusText**
</dt> <dd>

Text that describes the expert status.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




