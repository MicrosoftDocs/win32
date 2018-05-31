---
title: DVBScramblingControlSpanningEvent structure
description: Specifies whether a DVB program stream is scrambled.
ms.assetid: e54e8ab2-fc90-4540-aed1-c6dedc2f5d88
keywords:
- DVBScramblingControlSpanningEvent structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- DVBScramblingControlSpanningEvent
api_location:
- bdamedia.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DVBScramblingControlSpanningEvent structure

Specifies whether a DVB program stream is scrambled.

## Syntax


```C++
typedef struct _DVBScramblingControlSpanningEvent {
  ULONG ulPID;
  BOOL  fScrambled;
} DVBScramblingControlSpanningEvent;
```



## Members

<dl> <dt>

**ulPID**
</dt> <dd>

The packet identifier (PID) associated with the stream.

</dd> <dt>

**fScrambled**
</dt> <dd>

If **TRUE**, the program stream is scrambled. Otherwise, it is not scrambled.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





