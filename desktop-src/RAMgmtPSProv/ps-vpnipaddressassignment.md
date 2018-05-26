---
title: PS\_VpnIPAddressAssignment class
description: Represents IP address assignment configuration for VPN.
audience: developer
ms.assetid: fc9e6146-662f-4acf-aa51-1c3556d93980
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnIPAddressAssignment class
- PS_VpnIPAddressAssignment class, described
topic_type:
- apiref
api_name:
- PS_VpnIPAddressAssignment
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_VpnIPAddressAssignment class

Represents IP address assignment configuration for VPN

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnIPAddressAssignment
{
};
```

## Members

The **PS\_VpnIPAddressAssignment** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnIPAddressAssignment** class has these methods.



| Method                                                                                         | Description                                                                                                                                      |
|:-----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetByVpnIPAddressAssignment**](setbyvpnipaddressassignment-ps-vpnipaddressassignment.md)   | This cmdlet does the following1. Configure the IPv4 address assignment method2. Configure the IPv6 prefix for IPv6 address assignment<br/> |
| [**SetByVpnIPv6PrefixEntrypoint**](setbyvpnipv6prefixentrypoint-ps-vpnipaddressassignment.md) | This cmdlet does the following1. Configure the IPv4 address assignment method2. Configure the IPv6 prefix for IPv6 address assignment<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





