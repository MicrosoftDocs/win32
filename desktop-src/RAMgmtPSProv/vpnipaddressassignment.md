---
title: VpnIPAddressAssignment class
description: Virtual Private Network (VPN) IP address assignment policy.
audience: developer
ms.assetid: fc9e6146-662f-4acf-aa51-1c3556d93980
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnIPAddressAssignment class
- VpnIPAddressAssignment class, described
topic_type:
- apiref
api_name:
- VpnIPAddressAssignment
- VpnIPAddressAssignment.IPAssignmentMethod
- VpnIPAddressAssignment.IPAddressRange
- VpnIPAddressAssignment.IPv6Prefix
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnIPAddressAssignment class

Virtual Private Network (VPN) IP address assignment policy

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnIPAddressAssignment
{
  string            IPAssignmentMethod;
  VpnIPAddressRange IPAddressRange[];
  string            IPv6Prefix;
};
```

## Members

The **VpnIPAddressAssignment** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnIPAddressAssignment** class has these properties.

<dl> <dt>

**IPAddressRange**
</dt> <dd> <dl> <dt>

Data type: **VpnIPAddressRange** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnIPAddressRange**](vpnipaddressrange.md)")
</dt> </dl>

Array of [**VpnIPAddressRange**](vpnipaddressrange.md) embedded instances

</dd> <dt>

**IPAssignmentMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Type of IP address assignment

The possible values are.

<dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>

**Dhcp** ("Dhcp")


</dt> <dd></dd> <dt>

<span id="StaticPool"></span><span id="staticpool"></span><span id="STATICPOOL"></span>

**StaticPool** ("StaticPool")


</dt> <dd></dd> </dl>

</dd> <dt>

**IPv6Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IPv6 Prefix used for address assignment

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





