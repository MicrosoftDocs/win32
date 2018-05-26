---
title: VpnConnectionTriggerDnsConfiguration class
description: The VpnConnectionTriggerDnsConfiguration class represents the DNS configuration for an auto-triggered VPN connection.
audience: developer
ms.assetid: 16D080E3-8069-431A-8A05-3FF487122CB6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnConnectionTriggerDnsConfiguration class
- VpnConnectionTriggerDnsConfiguration class, described
topic_type:
- apiref
api_name:
- VpnConnectionTriggerDnsConfiguration
- VpnConnectionTriggerDnsConfiguration.ConnectionName
- VpnConnectionTriggerDnsConfiguration.DnsSuffix
- VpnConnectionTriggerDnsConfiguration.DnsIPAddress
- VpnConnectionTriggerDnsConfiguration.DnsSuffixSearchList
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnConnectionTriggerDnsConfiguration class

The **VpnConnectionTriggerDnsConfiguration** class represents the DNS configuration for an auto-triggered VPN connection.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class VpnConnectionTriggerDnsConfiguration
{
  string ConnectionName;
  string DnsSuffix;
  string DnsIPAddress[];
  string DnsSuffixSearchList[];
};
```

## Members

The **VpnConnectionTriggerDnsConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnConnectionTriggerDnsConfiguration** class has these properties.

<dl> <dt>

**ConnectionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the current VPN connection profile.

</dd> <dt>

**DnsIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv4/IPv6 addresses of the DNS servers to use for the DNS suffix.

</dd> <dt>

**DnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS suffix for auto triggering a VPN connection.

</dd> <dt>

**DnsSuffixSearchList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS suffix search list for the auto-triggered VPN connection.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





