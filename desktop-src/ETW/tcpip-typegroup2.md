---
description: This class is the event type class for IPv4 TCP/IP connect and accept events. The following syntax is simplified from MOF code.
ms.assetid: a9b33ceb-7d50-4cd7-8224-0b2cf895b3b4
title: TcpIp_TypeGroup2 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TcpIp_TypeGroup2
- TcpIp_TypeGroup2.PID
- TcpIp_TypeGroup2.size
- TcpIp_TypeGroup2.daddr
- TcpIp_TypeGroup2.saddr
- TcpIp_TypeGroup2.dport
- TcpIp_TypeGroup2.sport
- TcpIp_TypeGroup2.mss
- TcpIp_TypeGroup2.sackopt
- TcpIp_TypeGroup2.tsopt
- TcpIp_TypeGroup2.wsopt
- TcpIp_TypeGroup2.rcvwin
- TcpIp_TypeGroup2.rcvwinscale
- TcpIp_TypeGroup2.sndwinscale
- TcpIp_TypeGroup2.seqnum
- TcpIp_TypeGroup2.connid
api_type: 
- NA
api_location: 
---

# TcpIp\_TypeGroup2 class

This class is the event type class for IPv4 TCP/IP connect and accept events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{12, 15}, EventTypeName{"ConnectIPV4", "AcceptIPV4"}]
class TcpIp_TypeGroup2 : TcpIp
{
  uint32 PID;
  uint32 size;
  object daddr;
  object saddr;
  object dport;
  object sport;
  uint16 mss;
  uint16 sackopt;
  uint16 tsopt;
  uint16 wsopt;
  uint32 rcvwin;
  sint16 rcvwinscale;
  sint16 sndwinscale;
  uint32 seqnum;
  uint32 connid;
};
```

## Members

The **TcpIp\_TypeGroup2** class has these types of members:

-   [Properties](#properties)

### Properties

The **TcpIp\_TypeGroup2** class has these properties.

<dl> <dt>

**connid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(15)**, **Pointer**
</dt> </dl>

A unique connection identifier to correlate events belonging to the same connection.

</dd> <dt>

**daddr**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(3)**, **Extension("IPAddrV4")**
</dt> </dl>

Destination IP address.

</dd> <dt>

**dport**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(5)**, **Extension("Port")**
</dt> </dl>

Destination port number.

</dd> <dt>

**mss**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(7)**
</dt> </dl>

Maximum segment size.

</dd> <dt>

**PID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(1)**
</dt> </dl>

Identifier of the process associated with the request.

</dd> <dt>

**rcvwin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(11)**
</dt> </dl>

TCP Receive Window size.

</dd> <dt>

**rcvwinscale**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(12)**
</dt> </dl>

TCP Receive Window Scaling factor.

</dd> <dt>

**sackopt**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(8)**
</dt> </dl>

Selective Acknowledgment (SACK) option in TCP header.

</dd> <dt>

**saddr**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(4)**, **Extension("IPAddrV4")**
</dt> </dl>

Source IP address.

</dd> <dt>

**seqnum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(14)**
</dt> </dl>

Sequence number.

</dd> <dt>

**size**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(2)**
</dt> </dl>

Size of the packet.

</dd> <dt>

**sndwinscale**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(13)**
</dt> </dl>

TCP Send Window Scaling factor.

</dd> <dt>

**sport**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(6)**, **Extension("Port")**
</dt> </dl>

Source port number.

</dd> <dt>

**tsopt**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(9)**
</dt> </dl>

Time Stamp option in TCP header.

</dd> <dt>

**wsopt**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId(10)**
</dt> </dl>

Window Scale option in TCP header.

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

 

 




