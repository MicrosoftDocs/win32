---
description: An actual frame from the driver.
ms.assetid: '867082c1-196a-4580-ba24-187b0752f6f8'
title: FRAME structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FRAME
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# FRAME structure

The **FRAME** structure is an actual frame from the driver.

## Syntax


```C++
typedef struct _FRAME {
  __int64 TimeStamp;
  DWORD   FrameLength;
  DWORD   nBytesAvail;
  BYTE    MacFrame[];
} FRAME, *LPFRAME, *ULPFRAME;
```



## Members

<dl> <dt>

**TimeStamp**
</dt> <dd>

Elapsed time, in microseconds, between the start of the capture and the time when the frame was captured.

</dd> <dt>

**FrameLength**
</dt> <dd>

MAC frame length.

</dd> <dt>

**nBytesAvail**
</dt> <dd>

Actual frame length copied.

</dd> <dt>

**MacFrame**
</dt> <dd>

Frame data.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




