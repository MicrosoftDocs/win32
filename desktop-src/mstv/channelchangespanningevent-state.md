---
title: ChannelChangeSpanningEvent\_State enumeration
description: Specifies the current state of a channel-change event in an MPEG-2 stream.
ms.assetid: '21ed5fdf-1e48-4020-8bff-6f7f9ed0ac12'
keywords: ["ChannelChangeSpanningEvent_State enumeration Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- ChannelChangeSpanningEvent_State
api_location:
- bdamedia.h
api_type:
- HeaderDef
---

# ChannelChangeSpanningEvent\_State enumeration

Specifies the current state of a channel-change event in an MPEG-2 stream.

## Syntax


```C++
typedef enum  { 
  ChannelChangeSpanningEvent_Start  = 0,
  ChannelChangeSpanningEvent_End    = 2
} ChannelChangeSpanningEvent_State;
```



## Constants

<dl> <dt>

<span id="ChannelChangeSpanningEvent_Start"></span><span id="channelchangespanningevent_start"></span><span id="CHANNELCHANGESPANNINGEVENT_START"></span>**ChannelChangeSpanningEvent\_Start**
</dt> <dd>

Start of the channel change.

</dd> <dt>

<span id="ChannelChangeSpanningEvent_End"></span><span id="channelchangespanningevent_end"></span><span id="CHANNELCHANGESPANNINGEVENT_END"></span>**ChannelChangeSpanningEvent\_End**
</dt> <dd>

End of the channel change.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





