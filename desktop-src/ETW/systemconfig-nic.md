---
description: This class is the event type class for network interface card configuration events. The following syntax is simplified from MOF code.
ms.assetid: 66b2c116-810e-489d-ad5e-f9c09902005b
title: SystemConfig_NIC class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_NIC
- SystemConfig_NIC.PhysicalAddr
- SystemConfig_NIC.PhysicalAddrLen
- SystemConfig_NIC.Ipv4Index
- SystemConfig_NIC.Ipv6Index
- SystemConfig_NIC.NICDescription
- SystemConfig_NIC.IpAddresses
- SystemConfig_NIC.DnsServerAddresses
api_type: 
- NA
api_location: 
---

# SystemConfig\_NIC class

This class is the event type class for network interface card configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(13), EventTypeName("NIC")]
class SystemConfig_NIC : SystemConfig
{
  uint64 PhysicalAddr;
  uint32 PhysicalAddrLen;
  uint32 Ipv4Index;
  uint32 Ipv6Index;
  string NICDescription;
  string IpAddresses;
  string DnsServerAddresses;
};
```

## Members

The **SystemConfig\_NIC** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_NIC** class has these properties.

<dl> <dt>

DnsServerAddresses
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

IP addresses to be used in querying for DNS servers. The list of addresses is comma-delimited.

</dd> <dt>

IpAddresses
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

IP addresses associated with the network interface card. The list of addresses is comma-delimited.

</dd> <dt>

Ipv4Index
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Adapter index for IPv4 NIC. The adapter index may change when an adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

</dd> <dt>

Ipv6Index
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Adapter index for IPv6 NIC. The adapter index may change when an adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

</dd> <dt>

NICDescription
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Description of the adapter.

</dd> <dt>

PhysicalAddr
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

Hardware address for the adapter.

</dd> <dt>

PhysicalAddrLen
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Length of the hardware address for the adapter.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SystemConfig**](systemconfig.md)
</dt> </dl>

 

 




