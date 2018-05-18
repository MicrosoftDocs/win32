---
title: VpnConnectionTrigger class
description: The VpnConnectionTrigger class represents the auto-trigger properties of a VPN connection.
audience: developer
ms.assetid: '7BF92F5E-B6AD-451C-A881-CE81CA89EF1C'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnConnectionTrigger class", "VpnConnectionTrigger class, described"]
topic_type:
- apiref
api_name:
- VpnConnectionTrigger
- VpnConnectionTrigger.ConnectionName
- VpnConnectionTrigger.ApplicationID
- VpnConnectionTrigger.dnsConfig
- VpnConnectionTrigger.DnsSuffixSearchList
- VpnConnectionTrigger.TrustedNetwork
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
---

# VpnConnectionTrigger class

The **VpnConnectionTrigger** class represents the auto-trigger properties of a VPN connection.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class VpnConnectionTrigger
{
  string                               ConnectionName;
  string                               ApplicationID[];
  VpnConnectionTriggerDnsConfiguration dnsConfig[];
  string                               DnsSuffixSearchList[];
  string                               TrustedNetwork[];
};
```

## Members

The **VpnConnectionTrigger** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnConnectionTrigger** class has these properties.

<dl> <dt>

**ApplicationID**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The identifiers of applications that auto-trigger connections.

</dd> <dt>

**ConnectionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the current VPN connection profile.

</dd> <dt>

**dnsConfig**
</dt> <dd> <dl> <dt>

Data type: **VpnConnectionTriggerDnsConfiguration** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md)")
</dt> </dl>

The trigger DNS configurations.

</dd> <dt>

**DnsSuffixSearchList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS suffix search list for the auto-triggered VPN connection.

</dd> <dt>

**TrustedNetwork**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The trusted network DNS suffixes for the auto-triggered VPN connection.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





