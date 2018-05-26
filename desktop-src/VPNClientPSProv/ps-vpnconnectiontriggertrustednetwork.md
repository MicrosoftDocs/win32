---
title: PS\_VpnConnectionTriggerTrustedNetwork class
description: The PS\_VpnConnectionTriggerTrustedNetwork class provides methods to configure the trusted network configuration for VPN triggering.
audience: developer
ms.assetid: 71B4F04D-1B88-433D-BBB1-870D4781F70D
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnConnectionTriggerTrustedNetwork class
- PS_VpnConnectionTriggerTrustedNetwork class, described
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerTrustedNetwork
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_VpnConnectionTriggerTrustedNetwork class

The **PS\_VpnConnectionTriggerTrustedNetwork** class provides methods to configure the trusted network configuration for VPN triggering.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnectionTriggerTrustedNetwork
{
};
```

## Members

The **PS\_VpnConnectionTriggerTrustedNetwork** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnConnectionTriggerTrustedNetwork** class has these methods.



| Method                                                         | Description                                                                                                                                                                                            |
|:---------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-vpnconnectiontriggertrustednetwork.md)       | Adds DNS suffixes to the trusted network list of the VPN connection profile.<br/>                                                                                                                |
| [**Remove**](remove-ps-vpnconnectiontriggertrustednetwork.md) | Removes DNS suffixes from the trusted network list of the VPN connection profile.<br/>                                                                                                           |
| [**Set**](set-ps-vpnconnectiontriggertrustednetwork.md)       | Sets the trusted network list with the Name Resolution Policy Table (NRPT) DNS suffixes that have been configured as part of triggering properties. The NRPT exemption entries are ignored.<br/> |



 

## Remarks

When a trusted suffix is present on the client's physical interface, VPN auto-trigger is suppressed.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





