---
title: DhcpServerv6Scope class
description: Dhcp Server v6 Scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c33810fa-b8c1-4a8a-9069-6080cfd8a6b5
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6Scope class
- DhcpServerv6Scope class, described
topic_type:
- apiref
api_name:
- DhcpServerv6Scope
- DhcpServerv6Scope.Prefix
- DhcpServerv6Scope.Name
- DhcpServerv6Scope.Description
- DhcpServerv6Scope.Preference
- DhcpServerv6Scope.PreferredLifetime
- DhcpServerv6Scope.PrefixLength
- DhcpServerv6Scope.State
- DhcpServerv6Scope.T1
- DhcpServerv6Scope.T2
- DhcpServerv6Scope.ValidLifetime
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv6Scope class

Dhcp Server v6 Scope.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6Scope
{
  string   Prefix;
  string   Name;
  string   Description;
  uint16   Preference;
  DateTime PreferredLifetime;
  uint32   PrefixLength;
  string   State;
  DateTime T1;
  DateTime T2;
  DateTime ValidLifetime;
};
```

## Members

The **DhcpServerv6Scope** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6Scope** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description of the given scope on Dhcp server

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the given scope on Dhcp server

</dd> <dt>

**Preference**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Preference of the given scope on Dhcp server

</dd> <dt>

**PreferredLifetime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

it specifies the preferred lifetime for IANA addresses for given scope on Dhcp server

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope identifier(unique) for the given scope on Dhcp server

</dd> <dt>

**PrefixLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the Prefix Length for given scope on Dhcp server

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

State of given scope on Dhcp server, whether its functional(active).

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="InActive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**InActive** ("InActive")


</dt> <dd></dd> </dl>

</dd> <dt>

**T1**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the lease renewal time for given scope on Dhcp server.

</dd> <dt>

**T2**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the lease rebind time for given scope on Dhcp server.

</dd> <dt>

**ValidLifetime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the valid lifetime for IANA addresses for given scope on Dhcp server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





