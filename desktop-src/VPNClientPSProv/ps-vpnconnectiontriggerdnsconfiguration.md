---
title: PS\_VpnConnectionTriggerDnsConfiguration class
description: The PS\_VpnConnectionTriggerDnsConfiguration class provides methods to manage the DNS trigger configuration of the VPN profile.
audience: developer
ms.assetid: 16D080E3-8069-431A-8A05-3FF487122CB6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnConnectionTriggerDnsConfiguration class
- PS_VpnConnectionTriggerDnsConfiguration class, described
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerDnsConfiguration
- PS_VpnConnectionTriggerDnsConfiguration.DnsSuffix
- PS_VpnConnectionTriggerDnsConfiguration.DnsIPAddress
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_VpnConnectionTriggerDnsConfiguration class

The **PS\_VpnConnectionTriggerDnsConfiguration** class provides methods to manage the DNS trigger configuration of the VPN profile.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnectionTriggerDnsConfiguration
{
  string DnsSuffix;
  string DnsIPAddress[];
};
```

## Members

The **PS\_VpnConnectionTriggerDnsConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **PS\_VpnConnectionTriggerDnsConfiguration** class has these methods.



| Method                                                        | Description                                                                               |
|:--------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Add**](add-ps-vpnconnectiontriggerdnsconfiguration.md)    | Adds a DNS suffix and the corresponding DNS servers to the configuration.<br/>      |
| [**Remove**](add-ps-vpnconnectiontriggerdnsconfiguration.md) | Removes DNS suffixes and the corresponding DNS servers from the configuration.<br/> |
| [**Set**](set-ps-vpnconnectiontriggerdnsconfiguration.md)    | Sets the DNS servers for a DNS suffix in the configuration.<br/>                    |



 

### Properties

The **PS\_VpnConnectionTriggerDnsConfiguration** class has these properties.

<dl> <dt>

**DnsIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv4/IPv6 addresses of the DNS servers that should be used for the DNS suffix.

</dd> <dt>

**DnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The DNS suffix for auto triggering a VPN connection.

</dd> </dl>

## Remarks

The DNS configuration contains a list of DNS suffixes and, for each suffix, a list of DNS servers. Whenever a client tries to access a resource that matches the DNS suffix, a VPN connection is auto-triggered.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





