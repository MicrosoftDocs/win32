---
Description: An actual frame from the driver.
ms.assetid: a4f53568-684b-48cf-835b-915cefb45a5d
title: FRAME structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




