---
description: This class is the event type class for network interface card configuration events.
ms.assetid: 1cae611b-fb6a-4416-8fd4-0c882e8aa5e6
title: SystemConfig_V0_NIC class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_V0_NIC
- SystemConfig_V0_NIC.NICName
- SystemConfig_V0_NIC.Index
- SystemConfig_V0_NIC.PhysicalAddrLen
- SystemConfig_V0_NIC.PhysicalAddr
- SystemConfig_V0_NIC.Size
- SystemConfig_V0_NIC.IpAddress
- SystemConfig_V0_NIC.SubnetMask
- SystemConfig_V0_NIC.DhcpServer
- SystemConfig_V0_NIC.Gateway
- SystemConfig_V0_NIC.PrimaryWinsServer
- SystemConfig_V0_NIC.SecondaryWinsServer
- SystemConfig_V0_NIC.DnsServer1
- SystemConfig_V0_NIC.DnsServer2
- SystemConfig_V0_NIC.DnsServer3
- SystemConfig_V0_NIC.DnsServer4
- SystemConfig_V0_NIC.Data
api_type: 
- NA
api_location: 
---

# SystemConfig\_V0\_NIC class

This class is the event type class for network interface card configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(13), EventTypeName("NIC")]
class SystemConfig_V0_NIC : SystemConfig_V0
{
  char16 NICName[];
  uint32 Index;
  uint32 PhysicalAddrLen;
  char16 PhysicalAddr;
  uint32 Size;
  sint32 IpAddress;
  sint32 SubnetMask;
  sint32 DhcpServer;
  sint32 Gateway;
  sint32 PrimaryWinsServer;
  sint32 SecondaryWinsServer;
  sint32 DnsServer1;
  sint32 DnsServer2;
  sint32 DnsServer3;
  sint32 DnsServer4;
  uint32 Data;
};
```

## Members

The **SystemConfig\_V0\_NIC** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_V0\_NIC** class has these properties.

<dl> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (16)
</dt> </dl>

Data field.

</dd> <dt>

**DhcpServer**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8)
</dt> </dl>

IP address of the dynamic host configuration protocol (DHCP) server. A value of 255.255.255.255 indicates the DHCP server could not be reached, or is in the process of being reached. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**DnsServer1**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (12)
</dt> </dl>

First server IP addresses to be used in querying for DNS servers. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**DnsServer2**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (13)
</dt> </dl>

Second server IP addresses to be used in querying for DNS servers. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**DnsServer3**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (14)
</dt> </dl>

Third server IP addresses to be used in querying for DNS servers. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**DnsServer4**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (15)
</dt> </dl>

Fourth server IP addresses to be used in querying for DNS servers. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**Gateway**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9)
</dt> </dl>

IP address of default gateway that the computer system uses. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**Index**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2)
</dt> </dl>

Adapter index. The adapter index may change when an adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

</dd> <dt>

**IpAddress**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6)
</dt> </dl>

IP addresses associated with the network interface card. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**NICName**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1), **Max** (256)
</dt> </dl>

Name of the network interface card.

</dd> <dt>

**PhysicalAddr**
</dt> <dd> <dl> <dt>

Data type: **char16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4), **Max** (8)
</dt> </dl>

Hardware address for the adapter.

</dd> <dt>

**PhysicalAddrLen**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Length of the hardware address for the adapter.

</dd> <dt>

**PrimaryWinsServer**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10)
</dt> </dl>

IP address for the primary WINS server. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**SecondaryWinsServer**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11)
</dt> </dl>

IP address for the secondary WINS server. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Size, in bytes, of the Data property.

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7)
</dt> </dl>

Subnet mask associated with the network interface card. Each byte of the sint32 represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SystemConfig\_V0**](systemconfig-v0.md)
</dt> </dl>

 

 




