---
description: This class is the event type class for IPv4 TCP/IP send events. The following syntax is simplified from MOF code.
ms.assetid: 51a61257-fcbf-4724-80e4-12bdf45b359e
title: TcpIp_SendIPV4 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TcpIp_SendIPV4
- TcpIp_SendIPV4.PID
- TcpIp_SendIPV4.size
- TcpIp_SendIPV4.daddr
- TcpIp_SendIPV4.saddr
- TcpIp_SendIPV4.dport
- TcpIp_SendIPV4.sport
- TcpIp_SendIPV4.startime
- TcpIp_SendIPV4.endtime
- TcpIp_SendIPV4.seqnum
- TcpIp_SendIPV4.connid
api_type: 
- NA
api_location: 
---

# TcpIp\_SendIPV4 class

This class is the event type class for IPv4 TCP/IP send events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{10}, EventTypeName{"SendIPV4"}]
class TcpIp_SendIPV4 : TcpIp
{
  uint32 PID;
  uint32 size;
  object daddr;
  object saddr;
  object dport;
  object sport;
  uint32 startime;
  uint32 endtime;
  uint32 seqnum;
  uint32 connid;
};
```

## Members

The **TcpIp\_SendIPV4** class has these types of members:

-   [Properties](#properties)

### Properties

The **TcpIp\_SendIPV4** class has these properties.

<dl> <dt>

connid
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(10), Pointer
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

**endtime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8)
</dt> </dl>

End send request time.

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

Qualifiers: WmiDataId(9)
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

</dd> <dt>

**startime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7)
</dt> </dl>

Start send request time.

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

 

 




