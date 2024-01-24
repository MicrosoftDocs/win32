---
description: The FRAME\_DESCRIPTOR structure provides descriptive information about raw frames.
ms.assetid: f2fc256e-8e64-49c1-b2ad-ef656762d5c7
title: FRAME_DESCRIPTOR structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FRAME_DESCRIPTOR
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# FRAME\_DESCRIPTOR structure

The **FRAME\_DESCRIPTOR** structure provides descriptive information about raw frames.

## Syntax


```C++
typedef struct _FRAME_DESCRIPTOR {
  LPBYTE       FramePointer;
  __int64      TimeStamp;
  DWORD        FrameLength;
  DWORD        nBytesAvail;
  WORD         Etype;
  BYTE         Sap;
  BYTE         LowProtocol;
  WORD         LowProtocolOffset;
  GENERIC_PORT HighPort;
  WORD         HighProtocolOffset;
} FRAME_DESCRIPTOR, *LPFRAME_DESCRIPTOR;
```



## Members

<dl> <dt>

**FramePointer**
</dt> <dd>

Pointer to frame data.

</dd> <dt>

**TimeStamp**
</dt> <dd>

System time, in microseconds, when the frame was captured. This time is typically used to determine the interval between the times two frames were captured.

</dd> <dt>

**FrameLength**
</dt> <dd>

Length of the frame.

</dd> <dt>

**nBytesAvail**
</dt> <dd>

Actual frame length copied.

</dd> <dt>

**Etype**
</dt> <dd>

Etype name.

</dd> <dt>

**Sap**
</dt> <dd>

SAP value.

</dd> <dt>

**LowProtocol**
</dt> <dd>

Index of protocol found.

</dd> <dt>

**LowProtocolOffset**
</dt> <dd>

Offset to protocol data obtained from **LowProtocol**.

</dd> <dt>

**HighPort**
</dt> <dd>

Port of high protocol identified in **LowProtocol**.

</dd> <dt>

**HighProtocolOffset**
</dt> <dd>

Offset to protocol data obtained from **HighPort**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




