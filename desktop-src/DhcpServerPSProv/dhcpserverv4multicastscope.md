---
title: DhcpServerv4MulticastScope class
description: Dhcp Server v4 Multicast Scope class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c5f0abc4-1160-4421-9ce7-847ea32d0a92
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4MulticastScope class
- DhcpServerv4MulticastScope class, described
topic_type:
- apiref
api_name:
- DhcpServerv4MulticastScope
- DhcpServerv4MulticastScope.Name
- DhcpServerv4MulticastScope.Description
- DhcpServerv4MulticastScope.StartRange
- DhcpServerv4MulticastScope.EndRange
- DhcpServerv4MulticastScope.LeaseDuration
- DhcpServerv4MulticastScope.ExpiryTime
- DhcpServerv4MulticastScope.State
- DhcpServerv4MulticastScope.Ttl
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4MulticastScope class

Dhcp Server v4 Multicast Scope class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4MulticastScope
{
  string   Name;
  string   Description;
  string   StartRange;
  string   EndRange;
  DateTime LeaseDuration;
  DateTime ExpiryTime;
  string   State;
  UINT32   Ttl;
};
```

## Members

The **DhcpServerv4MulticastScope** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4MulticastScope** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope description.

</dd> <dt>

**EndRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

End of scope IP range.

</dd> <dt>

**ExpiryTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time to live. After expiry of this period, the scope is deleted by the DHCP server.

</dd> <dt>

**LeaseDuration**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lease duration configured on this scope.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope name.

</dd> <dt>

**StartRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Start of scope IP range.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope state.

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** ("Inactive")


</dt> <dd></dd> </dl>

</dd> <dt>

**Ttl**
</dt> <dd> <dl> <dt>

Data type: **UINT32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of routers through which multicast traffic passes through.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





