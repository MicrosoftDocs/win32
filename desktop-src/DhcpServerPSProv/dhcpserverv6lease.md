---
title: DhcpServerv6Lease class
description: Dhcp Server v6 Client Lease.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9b6769a6-78c2-4169-bca7-a0a805d3e143'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv6Lease class", "DhcpServerv6Lease class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv6Lease
- DhcpServerv6Lease.AddressType
- DhcpServerv6Lease.IPAddress
- DhcpServerv6Lease.Prefix
- DhcpServerv6Lease.Description
- DhcpServerv6Lease.ClientDuid
- DhcpServerv6Lease.HostName
- DhcpServerv6Lease.Iaid
- DhcpServerv6Lease.LeaseExpiryTime
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv6Lease class

Dhcp Server v6 Client Lease.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6Lease
{
  string   AddressType;
  string   IPAddress;
  string   Prefix;
  string   Description;
  string   ClientDuid;
  string   HostName;
  uint32   Iaid;
  DateTime LeaseExpiryTime;
};
```

## Members

The **DhcpServerv6Lease** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6Lease** class has these properties.

<dl> <dt>

**AddressType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Address Type of Client.

<dt>

<span id="IATA"></span><span id="iata"></span>

**IATA** ("IATA")


</dt> <dd></dd> <dt>

<span id="IANA"></span><span id="iana"></span>

**IANA** ("IANA")


</dt> <dd></dd> </dl>

</dd> <dt>

**ClientDuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client Duid.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description for the client.

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client Name.

</dd> <dt>

**Iaid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Interface Identifier.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client IP Address.

</dd> <dt>

**LeaseExpiryTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Valid lease expiry time.

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Prefix Address to which Client belongs.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





