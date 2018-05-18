---
title: PS\_VpnConnectionTrigger class
description: The PS\_VpnConnectionTrigger class has a method to retrieve the trigger properties of the VPN profile.
audience: developer
ms.assetid: '7BF92F5E-B6AD-451C-A881-CE81CA89EF1C'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnConnectionTrigger class", "PS_VpnConnectionTrigger class, described"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionTrigger
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnConnectionTrigger class

The **PS\_VpnConnectionTrigger** class has a method to retrieve the trigger properties of the VPN profile.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnectionTrigger
{
};
```

## Members

The **PS\_VpnConnectionTrigger** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnConnectionTrigger** class has these methods.



| Method                                     | Description                                                    |
|:-------------------------------------------|:---------------------------------------------------------------|
| [**Get**](get-ps-vpnconnectiontrigger.md) | Returns the trigger properties of a VPN connection.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





