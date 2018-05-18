---
title: DhcpServerv4Scope class
description: Dhcp Server v4 Scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '64325de3-0a3e-4955-825e-2baec0c4ddd1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4Scope class", "DhcpServerv4Scope class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4Scope
- DhcpServerv4Scope.ScopeId
- DhcpServerv4Scope.Name
- DhcpServerv4Scope.Description
- DhcpServerv4Scope.SubnetMask
- DhcpServerv4Scope.StartRange
- DhcpServerv4Scope.EndRange
- DhcpServerv4Scope.SuperscopeName
- DhcpServerv4Scope.LeaseDuration
- DhcpServerv4Scope.NapProfile
- DhcpServerv4Scope.NapEnable
- DhcpServerv4Scope.Delay
- DhcpServerv4Scope.State
- DhcpServerv4Scope.Type
- DhcpServerv4Scope.MaxBootpClients
- DhcpServerv4Scope.ActivatePolicies
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4Scope class

Dhcp Server v4 Scope.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Scope
{
  string   ScopeId;
  string   Name;
  string   Description;
  string   SubnetMask;
  string   StartRange;
  string   EndRange;
  string   SuperscopeName;
  DateTime LeaseDuration;
  string   NapProfile;
  boolean  NapEnable;
  uint16   Delay;
  string   State;
  string   Type;
  uint32   MaxBootpClients;
  boolean  ActivatePolicies;
};
```

## Members

The **DhcpServerv4Scope** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Scope** class has these properties.

<dl> <dt>

**ActivatePolicies**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if policy enforcement is enabled/disabled for the scope

</dd> <dt>

**Delay**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Delay (in ms) with which server leases addresses from this scope

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description of the given scope on Dhcp server

</dd> <dt>

**EndRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

End point or last address of IPRange available from where scope can lease out ipaddress

</dd> <dt>

**LeaseDuration**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Duration for which each Dhcp Lease is leased out by the Dhcp server

</dd> <dt>

**MaxBootpClients**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum number of bootp clients to which address can be leased out by given scope of Dhcp server

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the given scope on Dhcp server

</dd> <dt>

**NapEnable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if Nap setting is enabled for given scope on Dhcp server

</dd> <dt>

**NapProfile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Nap profile for given scope on Dhcp server

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope identifier(unique) for the given scope on Dhcp server

</dd> <dt>

**StartRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Starting point or first address of IPRange available from where scope can lease out ipaddress

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

State of given scope on Dhcp server, whether its functional(active) or not

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** ("Inactive")


</dt> <dd></dd> </dl>

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Subnet Mask for the given scope on Dhcp server

</dd> <dt>

**SuperscopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of Superscope to which given scope belongs

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of clients to which given scope of Dhcp server leases out ipaddress

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





