---
title: PS\_VpnServerIPsecConfiguration class
description: Represents an Internet Protocol Security (IPsec) VPN server configuration.
audience: developer
ms.assetid: '3cee426d-87f3-4ac9-88d7-f94bc375825b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnServerIPsecConfiguration class", "PS_VpnServerIPsecConfiguration class, described"]
topic_type:
- apiref
api_name:
- PS_VpnServerIPsecConfiguration
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnServerIPsecConfiguration class

Represents an Internet Protocol Security (IPsec) VPN server configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnServerIPsecConfiguration
{
};
```

## Members

The **PS\_VpnServerIPsecConfiguration** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnServerIPsecConfiguration** class has these methods.



| Method                                                                              | Description                                                                             |
|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**Get**](get-ps-vpnserveripsecconfiguration.md)                                   | Retrieves an IPsec VPN server configuration.<br/>                                 |
| [**SetByCustomPolicy**](setbycustompolicy-ps-vpnserveripsecconfiguration.md)       | Updates an IPsec VPN server configuration for custom policies.<br/>               |
| [**SetByEncryptionType**](setbyencryptiontype-ps-vpnserveripsecconfiguration.md)   | Updates an IPsec VPN server configuration for the specified encryption type.<br/> |
| [**SetByRevertToDefault**](setbyreverttodefault-ps-vpnserveripsecconfiguration.md) | Updates an IPsec VPN server configuration with default values.<br/>               |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





