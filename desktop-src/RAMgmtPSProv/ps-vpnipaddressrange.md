---
title: PS\_VpnIPAddressRange class
description: Represents the IP address range from which IP addresses are assigned to VPN clients.
audience: developer
ms.assetid: '4a6f4363-4b62-454b-90a2-c461ed3621fb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnIPAddressRange class", "PS_VpnIPAddressRange class, described"]
topic_type:
- apiref
api_name:
- PS_VpnIPAddressRange
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnIPAddressRange class

Represents the IP address range from which IP addresses are assigned to VPN clients

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnIPAddressRange
{
};
```

## Members

The **PS\_VpnIPAddressRange** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnIPAddressRange** class has these methods.



| Method                                        | Description                                                                                                   |
|:----------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-vpnipaddressrange.md)       | This cmdlet adds a new IPv4 address range from which IPv4 addresses can be assigned to VPN clients<br/> |
| [**Remove**](remove-ps-vpnipaddressrange.md) | This cmdlet removes an existing IPv4 address range from the pool for IP address assignment<br/>         |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





