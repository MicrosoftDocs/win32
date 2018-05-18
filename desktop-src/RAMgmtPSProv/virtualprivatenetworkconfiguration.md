---
title: VirtualPrivateNetworkConfiguration class
description: Virtual Private Network Configuration.
audience: developer
ms.assetid: 'eb5b58c4-fa52-43b8-9a93-225861765721'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VirtualPrivateNetworkConfiguration class", "VirtualPrivateNetworkConfiguration class, described"]
topic_type:
- apiref
api_name:
- VirtualPrivateNetworkConfiguration
- VirtualPrivateNetworkConfiguration.IPAddressAssignmentPolicy
- VirtualPrivateNetworkConfiguration.AuthenticationPolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VirtualPrivateNetworkConfiguration class

Virtual Private Network Configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VirtualPrivateNetworkConfiguration
{
  VpnIPAddressAssignment IPAddressAssignmentPolicy;
  VpnAuth                AuthenticationPolicy;
};
```

## Members

The **VirtualPrivateNetworkConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **VirtualPrivateNetworkConfiguration** class has these properties.

<dl> <dt>

**AuthenticationPolicy**
</dt> <dd> <dl> <dt>

Data type: **VpnAuth**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnAuth**](vpnauth.md)")
</dt> </dl>

VPN authentication policy as a [**VpnAuth**](vpnauth.md) embedded instance

</dd> <dt>

**IPAddressAssignmentPolicy**
</dt> <dd> <dl> <dt>

Data type: **VpnIPAddressAssignment**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnIPAddressAssignment**](vpnipaddressassignment.md)")
</dt> </dl>

Address assignment policy as a [**VpnIPAddressAssignment**](vpnipaddressassignment.md) embedded instance

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





