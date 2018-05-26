---
title: DhcpServerv4MulticastLease class
description: Dhcp Server v4 Multicast Lease.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 34c6a660-454d-4861-b652-cb4c47439d82
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4MulticastLease class
- DhcpServerv4MulticastLease class, described
topic_type:
- apiref
api_name:
- DhcpServerv4MulticastLease
- DhcpServerv4MulticastLease.AddressState
- DhcpServerv4MulticastLease.IPAddress
- DhcpServerv4MulticastLease.Name
- DhcpServerv4MulticastLease.ClientId
- DhcpServerv4MulticastLease.HostName
- DhcpServerv4MulticastLease.LeaseExpiryTime
- DhcpServerv4MulticastLease.LeaseStartTime
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv4MulticastLease class

Dhcp Server v4 Multicast Lease

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4MulticastLease
{
  string   AddressState;
  string   IPAddress;
  string   Name;
  string   ClientId;
  string   HostName;
  DateTime LeaseExpiryTime;
  DateTime LeaseStartTime;
};
```

## Members

The **DhcpServerv4MulticastLease** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4MulticastLease** class has these properties.

<dl> <dt>

**AddressState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Address state.

<dl><span id="Offered"></span><span id="offered"></span><span id="OFFERED"></span><dt>

**Offered**
</dt><span id="Active"></span><span id="active"></span><span id="ACTIVE"></span><dt>

**Active**
</dt><span id="Declined"></span><span id="declined"></span><span id="DECLINED"></span><dt>

**Declined**
</dt><span id="Expired"></span><span id="expired"></span><span id="EXPIRED"></span><dt>

**Expired**
</dt><span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span><dt>

**Inactive**
</dt> </dl>

</dd> <dt>

**ClientId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client unique identifier for Address Lease. Format is hex string with hyphen separation.

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client name.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client IP address.

</dd> <dt>

**LeaseExpiryTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lease expiry time. Outputformat will be as per the time zone of the user and the culture setting.

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** (Active)


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** (Inactive)


</dt> <dd></dd> </dl>

</dd> <dt>

**LeaseStartTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lease start time. Outputformat will be as per the time zone of the user and the culture setting.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the multicast scope.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





