---
description: The EXPERTFRAMEDESCRIPTOR structure contains information about a frame. When the expert calls the ExpertGetFrame function successfully, Network Monitor passes the EXPERTFRAMEDESCRIPTOR structure back to the expert.
ms.assetid: 6cf99498-3cf9-46da-b6a0-3012229f6908
title: EXPERTFRAMEDESCRIPTOR structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXPERTFRAMEDESCRIPTOR
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# EXPERTFRAMEDESCRIPTOR structure

The **EXPERTFRAMEDESCRIPTOR** structure contains information about a frame. When the expert calls the [**ExpertGetFrame**](expertgetframe.md) function successfully, Network Monitor passes the **EXPERTFRAMEDESCRIPTOR** structure back to the expert.

## Syntax


```C++
typedef struct {
  DWORD                FrameNumber;
  HFRAME               hFrame;
  ULPFRAME             pFrame;
  LPRECOGNIZEDATATABLE lpRecognizeDataTable;
  LPPROPERTYTABLE      lpPropertyTable;
} EXPERTFRAMEDESCRIPTOR, *LPEXPERTFRAMEDESCRIPTOR;
```



## Members

<dl> <dt>

**FrameNumber**
</dt> <dd>

Number of a specified frame.

</dd> <dt>

**hFrame**
</dt> <dd>

Handle to a frame.

</dd> <dt>

**pFrame**
</dt> <dd>

Pointer to a raw frame.

</dd> <dt>

**lpRecognizeDataTable**
</dt> <dd>

Table that indicates where each parser identifies the start of the data.

</dd> <dt>

**lpPropertyTable**
</dt> <dd>

Table of frame properties that the parser identifies.

</dd> </dl>

## Remarks

If the expert specifies FLAGS\_ATTACH\_PROPERTIES when calling [**ExpertGetFrame**](expertgetframe.md), then the **szPropertyText** member in each [**PROPERTYINST**](propertyinst.md) structure is **NULL**.

If the expert does not specify FLAGS\_ATTACH\_PROPERTIES when calling the [**ExpertGetFrame**](expertgetframe.md) function, then the **lpPropertyTable** member is **NULL** on return.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




