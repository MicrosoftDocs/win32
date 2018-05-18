---
title: PS\_VpnConnectionIPsecConfiguration class
description: The PS\_VpnConnectionIPsecConfiguration class can set or remove the IPsec custom policy configuration of a VPN connection profile.
audience: developer
ms.assetid: 'B993E97E-0E8F-42A6-8A0E-6794D1D90D88'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnConnectionIPsecConfiguration class", "PS_VpnConnectionIPsecConfiguration class, described"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionIPsecConfiguration
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnConnectionIPsecConfiguration class

The **PS\_VpnConnectionIPsecConfiguration** class can set or remove the IPsec custom policy configuration of a VPN connection profile.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnectionIPsecConfiguration
{
};
```

## Members

The **PS\_VpnConnectionIPsecConfiguration** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnConnectionIPsecConfiguration** class has these methods.



| Method                                                                            | Description                                                                                                       |
|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| [**SetByCustomPolicy**](setbycustompolicy-ps-vpnconnectionipsecconfiguration.md) | Sets the IPsec custom policy configuration of a VPN profile.<br/>                                           |
| [**SetIpSecByDefault**](setipsecbydefault-ps-vpnconnectionipsecconfiguration.md) | Removes the IPsec custom policy configuration and restores the default configuration of a VPN profile.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





