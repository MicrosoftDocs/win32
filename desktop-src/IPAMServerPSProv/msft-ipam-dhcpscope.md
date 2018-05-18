---
Description: 'DHCP scope object in IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e514a8d3-a45a-429a-ab4f-010eed6697a7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_IPAM\_DhcpScope class'
---

# MSFT\_IPAM\_DhcpScope class

DHCP scope object in IPAM.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_DhcpScope
{
  string  InstanceID;
  string  ScopeId;
  uint16  AddressFamily;
  string  ScopeName;
  string  SubnetMask;
  string  StartRange;
  string  EndRange;
  uint16  Delay;
  string  Description;
  string  LeaseDuration;
  string  ScopeStatus;
  string  SuperscopeName;
  string  ServerFqdn;
  uint16  Utilization;
  real64  PercentUtilized;
  string  PolicyActivationStatus;
  string  AccessScopePath;
  boolean IsInheritedAccessScope;
  string  PreferredLeaseTime;
  string  ValidLeaseTime;
};
```

## Members

The **MSFT\_IPAM\_DhcpScope** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_DhcpScope** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for this DHCP scope.

</dd> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

AddressFamily.

The possible values are.

<dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

**IPv4** (1)


</dt> <dd></dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

**IPv6** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Delay**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DHCP scope subnet delay in milliseconds.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DHCP scope description.

</dd> <dt>

**EndRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

End range of this DHCP scope.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Opaquely and uniquely identifies an instance of this class within the scope of the instantiating Namespace.

</dd> <dt>

**IsInheritedAccessScope**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the access scope for this DHCP scope is inherited from parent.

</dd> <dt>

**LeaseDuration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DHCP scope lease duration.

</dd> <dt>

**PercentUtilized**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percent Utilization of this DHCP scope.

</dd> <dt>

**PolicyActivationStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Policy Activation Status of this DHCP scope. Possible values are Active/Inactive.

</dd> <dt>

**PreferredLeaseTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Preferred lease time of IPv6 DHCP scope.

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope Id of this DHCP scope.

</dd> <dt>

**ScopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of this DHCP scope.

</dd> <dt>

**ScopeStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope status of this DHCP scope. Possible values are Active/Inactive.

</dd> <dt>

**ServerFqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DHCP server fully qualified domain name to which this scope belongs.

</dd> <dt>

**StartRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Start range of this DHCP scope.

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Subnet mask of this DHCP scope.

</dd> <dt>

**SuperscopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Superscope name to which this DHCP scope belongs to.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DHCP scope utilization status.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Under"></span><span id="under"></span><span id="UNDER"></span>

**Under** (1)


</dt> <dd></dd> <dt>

<span id="Optimal"></span><span id="optimal"></span><span id="OPTIMAL"></span>

**Optimal** (2)


</dt> <dd></dd> <dt>

<span id="Over"></span><span id="over"></span><span id="OVER"></span>

**Over** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ValidLeaseTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Valid lease time of IPv6 DHCP scope.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




