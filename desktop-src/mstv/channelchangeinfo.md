---
title: ChannelChangeInfo structure
description: Contains information about a channel-change event in an MPEG-2 stream.
ms.assetid: 61130e8e-7000-4f5a-b4c1-7ae22cfad473
keywords:
- ChannelChangeInfo structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- ChannelChangeInfo
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
api_location:
- bdamedia.h
api_type:
- HeaderDef
---

# ChannelChangeInfo structure

Contains information about a channel-change event in an MPEG-2 stream.

## Syntax


```C++
typedef struct _ChannelChangeInfo {
  ChannelChangeSpanningEvent_State state;
  ULONGLONG                        TimeStamp;
} ChannelChangeInfo;
```



## Members

<dl> <dt>

**state**
</dt> <dd>

Specifies the event state, specified as a member of the [**ChannelChangeSpanningEvent\_State**](channelchangespanningevent-state.md) enumeration.

</dd> <dt>

**TimeStamp**
</dt> <dd>

The tick count from the system timer when the event occurred.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





