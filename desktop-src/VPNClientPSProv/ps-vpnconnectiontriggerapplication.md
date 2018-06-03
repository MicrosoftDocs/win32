---
title: PS\_VpnConnectionTriggerApplication class
description: The PS\_VpnConnectionTriggerApplication class provides methods to configure an application, which when launched will trigger a VPN connection.
audience: developer
ms.assetid: 47794659-6EC9-4375-A86F-BB385DCAD561
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnConnectionTriggerApplication class
- PS_VpnConnectionTriggerApplication class, described
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerApplication
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_VpnConnectionTriggerApplication class

The **PS\_VpnConnectionTriggerApplication** class provides methods to configure an application, which when launched will trigger a VPN connection.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnectionTriggerApplication
{
};
```

## Members

The **PS\_VpnConnectionTriggerApplication** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnConnectionTriggerApplication** class has these methods.



| Method                                                      | Description                                                                                                                                 |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-vpnconnectiontriggerapplication.md)       | Adds an application to the trigger properties of a VPN connection profile that, when launched, auto-triggers the VPN connection.<br/> |
| [**Remove**](remove-ps-vpnconnectiontriggerapplication.md) | Removes applications from the trigger properties of a VPN connection profile.<br/>                                                    |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





