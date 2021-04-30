---
description: This class is the event type class for UDP/IP IPv4 send and receive events. The following syntax is simplified from MOF code.
ms.assetid: f04e0b4c-6a2b-4452-9bdf-38c08b487863
title: UdpIp_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UdpIp_TypeGroup1
- UdpIp_TypeGroup1.PID
- UdpIp_TypeGroup1.size
- UdpIp_TypeGroup1.daddr
- UdpIp_TypeGroup1.saddr
- UdpIp_TypeGroup1.dport
- UdpIp_TypeGroup1.sport
- UdpIp_TypeGroup1.seqnum
- UdpIp_TypeGroup1.connid
api_type: 
- NA
api_location: 
---

# UdpIp\_TypeGroup1 class

This class is the event type class for UDP/IP IPv4 send and receive events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{10, 11}, EventTypeName{"SendIPV4", "RecvIPV4"}]
class UdpIp_TypeGroup1 : UdpIp
{
  uint32 PID;
  uint32 size;
  object daddr;
  object saddr;
  object dport;
  object sport;
  uint32 seqnum;
  uint32 connid;
};
```

## Members

The **UdpIp\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **UdpIp\_TypeGroup1** class has these properties.

<dl> <dt>

connid
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8), Pointer
</dt> </dl>

A unique connection identifier to correlate events belonging to the same connection.

</dd> <dt>

daddr
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Extension("IPAddrV4")
</dt> </dl>

Destination IP address.

</dd> <dt>

dport
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), Extension("Port")
</dt> </dl>

Destination port number.

</dd> <dt>

PID
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

Identifier of the process associated with the request.

</dd> <dt>

saddr
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Extension("IPAddrV4")
</dt> </dl>

Source IP address.

</dd> <dt>

seqnum
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7)
</dt> </dl>

Sequence number.

</dd> <dt>

size
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Size of the packet.

</dd> <dt>

sport
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), Extension("Port")
</dt> </dl>

Source port number.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**UdpIp**](udpip.md)
</dt> </dl>

 

 




