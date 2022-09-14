---
description: The FRAMETABLE structure, a circular buffer of frame pointers, is handed back to applications attached to the ITRC interface of the NPP.
ms.assetid: 6e2d4f8d-46f2-4d53-bc28-7b0706663490
title: FRAMETABLE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FRAMETABLE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# FRAMETABLE structure

The **FRAMETABLE** structure, a circular buffer of frame pointers, is handed back to applications attached to the **ITRC** interface of the NPP.

## Syntax


```C++
typedef struct _FRAMETABLE {
  DWORD            FrameTableLength;
  DWORD            StartIndex;
  DWORD            EndIndex;
  DWORD            FrameCount;
  FRAME_DESCRIPTOR Frames[1];
} FRAMETABLE, *LPFRAMETABLE;
```



## Members

<dl> <dt>

**FrameTableLength**
</dt> <dd>

The total length of the table.

</dd> <dt>

**StartIndex**
</dt> <dd>

The first index within the table.

</dd> <dt>

**EndIndex**
</dt> <dd>

The last index within the table.

</dd> <dt>

**FrameCount**
</dt> <dd>

The number of frames described by this table.

</dd> <dt>

**Frames**
</dt> <dd>

The actual array of frame descriptors.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




