---
title: DhcpServerv6Reservation class
description: Dhcp Server v6 Reservation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '45137fbf-7657-4274-ac59-7950acf169ac'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv6Reservation class", "DhcpServerv6Reservation class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv6Reservation
- DhcpServerv6Reservation.Iaid
- DhcpServerv6Reservation.ClientDuid
- DhcpServerv6Reservation.IPAddress
- DhcpServerv6Reservation.Prefix
- DhcpServerv6Reservation.Name
- DhcpServerv6Reservation.Description
- DhcpServerv6Reservation.AddressState
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv6Reservation class

Dhcp Server v6 Reservation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6Reservation
{
  uint32 Iaid;
  string ClientDuid;
  string IPAddress;
  string Prefix;
  string Name;
  string Description;
  string AddressState;
};
```

## Members

The **DhcpServerv6Reservation** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6Reservation** class has these properties.

<dl> <dt>

**AddressState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Address state of client.

<dt>

<span id="ActiveReservation"></span><span id="activereservation"></span><span id="ACTIVERESERVATION"></span>

**ActiveReservation** ("ActiveReservation")


</dt> <dd></dd> <dt>

<span id="InactiveReservation"></span><span id="inactivereservation"></span><span id="INACTIVERESERVATION"></span>

**InactiveReservation** ("InactiveReservation")


</dt> <dd></dd> </dl>

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**ClientDuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client DUID for the reservation.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description of the reservation.

</dd> <dt>

**Iaid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The interface identifier of the DHCPv6 client interface.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IPAddress of given reservation

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the reservation.

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope identifier(unique) for the scope to which reservation belongs on Dhcp server

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





