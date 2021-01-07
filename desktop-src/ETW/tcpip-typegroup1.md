---
description: This class is the event type class for IPv4 TCP/IP events. The following syntax is simplified from MOF code.
ms.assetid: ed835df8-6f53-46a3-abf2-c66a1f13f987
title: TcpIp_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TcpIp_TypeGroup1
- TcpIp_TypeGroup1.PID
- TcpIp_TypeGroup1.size
- TcpIp_TypeGroup1.daddr
- TcpIp_TypeGroup1.saddr
- TcpIp_TypeGroup1.dport
- TcpIp_TypeGroup1.sport
- TcpIp_TypeGroup1.seqnum
- TcpIp_TypeGroup1.connid
api_type: 
- NA
api_location: 
---

# TcpIp\_TypeGroup1 class

This class is the event type class for IPv4 TCP/IP events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{11, 13, 14, 16, 18}, EventTypeName{"RecvIPV4", "DisconnectIPV4", "RetransmitIPV4", "ReconnectIPV4", "TCPCopyIPV4"}]
class TcpIp_TypeGroup1 : TcpIp
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

The **TcpIp\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **TcpIp\_TypeGroup1** class has these properties.

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

[**TcpIp**](tcpip.md)
</dt> </dl>

 

 




