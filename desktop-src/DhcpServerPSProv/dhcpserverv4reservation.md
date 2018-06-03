---
title: DhcpServerv4Reservation class
description: Dhcp Server v4 Reservation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 436be7ee-c036-4ad9-981c-8a9ab94898c1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4Reservation class
- DhcpServerv4Reservation class, described
topic_type:
- apiref
api_name:
- DhcpServerv4Reservation
- DhcpServerv4Reservation.Name
- DhcpServerv4Reservation.Description
- DhcpServerv4Reservation.Type
- DhcpServerv4Reservation.ClientId
- DhcpServerv4Reservation.IPAddress
- DhcpServerv4Reservation.ScopeId
- DhcpServerv4Reservation.AddressState
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4Reservation class

Dhcp Server v4 Reservation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Reservation
{
  string Name;
  string Description;
  string Type;
  string ClientId;
  string IPAddress;
  string ScopeId;
  string AddressState;
};
```

## Members

The **DhcpServerv4Reservation** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Reservation** class has these properties.

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

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**ClientId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client unique identifier for the reservation.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description of the reservation.

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

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope identifier(unique) for the scope to which reservation belongs on Dhcp server

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Address type of the reservation.

<dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>

**Dhcp** ("Dhcp")


</dt> <dd></dd> <dt>

<span id="Bootp"></span><span id="bootp"></span><span id="BOOTP"></span>

**Bootp** ("Bootp")


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** ("Both")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





