---
Description: 'DHCP Superscope object in IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'd8741e2a-4733-4027-bad0-43d65d022112'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_IPAM\_DhcpSuperscope class'
---

# MSFT\_IPAM\_DhcpSuperscope class

DHCP Superscope object in IPAM.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_DhcpSuperscope
{
  string  InstanceID;
  string  SuperscopeName;
  string  ServerFqdn;
  uint16  Utilization;
  real64  PercentUtilized;
  string  SuperscopeStatus;
  string  ScopeIds[];
  string  AccessScopePath;
  boolean IsInheritedAccessScope;
};
```

## Members

The **MSFT\_IPAM\_DhcpSuperscope** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_DhcpSuperscope** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for this DHCP superscope.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

TBD

</dd> <dt>

**IsInheritedAccessScope**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the access scope for this DHCP superscope is inherited from parent.

</dd> <dt>

**PercentUtilized**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percent Utilization of this DHCP superscope.

</dd> <dt>

**ScopeIds**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope Ids of all the scopes which falls under this DHCP superscope.

</dd> <dt>

**ServerFqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DHCP server fully qualified domain name to which this superscope belongs.

</dd> <dt>

**SuperscopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of this DHCP superscope.

</dd> <dt>

**SuperscopeStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Superscope status of this DHCP superscope. Possible values are Active/inactive.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DHCP superscope utilization status.

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

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




