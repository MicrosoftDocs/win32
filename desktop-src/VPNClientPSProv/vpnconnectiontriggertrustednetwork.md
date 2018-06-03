---
title: VpnConnectionTriggerTrustedNetwork class
description: The VpnConnectionTriggerTrustedNetwork class represents the trusted network configuration for VPN triggering.
audience: developer
ms.assetid: 71B4F04D-1B88-433D-BBB1-870D4781F70D
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnConnectionTriggerTrustedNetwork class
- VpnConnectionTriggerTrustedNetwork class, described
topic_type:
- apiref
api_name:
- VpnConnectionTriggerTrustedNetwork
- VpnConnectionTriggerTrustedNetwork.ConnectionName
- VpnConnectionTriggerTrustedNetwork.DnsSuffix
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VpnConnectionTriggerTrustedNetwork class

The **VpnConnectionTriggerTrustedNetwork** class represents the trusted network configuration for VPN triggering.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class VpnConnectionTriggerTrustedNetwork
{
  string ConnectionName;
  string DnsSuffix[];
};
```

## Members

The **VpnConnectionTriggerTrustedNetwork** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnConnectionTriggerTrustedNetwork** class has these properties.

<dl> <dt>

**ConnectionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the VPN connection profile.

</dd> <dt>

**DnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The list of DNS suffixes (the trusted network list).

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





