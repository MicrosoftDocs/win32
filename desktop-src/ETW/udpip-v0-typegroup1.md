---
description: UdpIp_V0_TypeGroup1 class - This class is the event type class for UDP/IP events. The following syntax is simplified from MOF code.
ms.assetid: 834a761a-089b-4b93-9a6a-a1edf752b582
title: UdpIp_V0_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UdpIp_V0_TypeGroup1
- UdpIp_V0_TypeGroup1.context
- UdpIp_V0_TypeGroup1.saddr
- UdpIp_V0_TypeGroup1.sport
- UdpIp_V0_TypeGroup1.size
- UdpIp_V0_TypeGroup1.daddr
- UdpIp_V0_TypeGroup1.dport
- UdpIp_V0_TypeGroup1.dsize
api_type: 
- NA
api_location: 
---

# UdpIp\_V0\_TypeGroup1 class

This class is the event type class for UDP/IP events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{10, 11}, EventTypeName{"Send", "Recv"}]
class UdpIp_V0_TypeGroup1 : UdpIp_V0
{
  uint32 context;
  object saddr;
  object sport;
  uint16 size;
  object daddr;
  object dport;
  uint16 dsize;
};
```

## Members

The **UdpIp\_V0\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **UdpIp\_V0\_TypeGroup1** class has these properties.

<dl> <dt>

context
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), pointer
</dt> </dl>

Process identifier for the Address Object that made or received the request.

</dd> <dt>

daddr
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), Extension("IPAddr")
</dt> </dl>

Destination IP address.

</dd> <dt>

dport
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), Extension("Port")
</dt> </dl>

Destination port number.

</dd> <dt>

dsize
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7)
</dt> </dl>

Size of the destination packet.

</dd> <dt>

saddr
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Extension("IPAddr")
</dt> </dl>

Source IP address.

</dd> <dt>

size
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Size of the source packet.

</dd> <dt>

sport
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Extension("Port")
</dt> </dl>

Source port number.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                   |



## See also

<dl> <dt>

[**UdpIp\_V0**](udpip-v0.md)
</dt> </dl>

 

 




