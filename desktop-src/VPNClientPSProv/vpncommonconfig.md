---
title: VpnCommonConfig class
description: The VpnCommonConfig class represents the common attributes of the VpnConnection and ThirdPartyVpnConnection objects.
audience: developer
ms.assetid: AB8AD9D4-9772-4532-8B47-AB3DCFDF8F6C
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnCommonConfig class
- VpnCommonConfig class, described
topic_type:
- apiref
api_name:
- VpnCommonConfig
- VpnCommonConfig.Name
- VpnCommonConfig.ProfileType
- VpnCommonConfig.ServerAddress
- VpnCommonConfig.ProvisioningAuthority
- VpnCommonConfig.RememberCredential
- VpnCommonConfig.SplitTunneling
- VpnCommonConfig.Guid
- VpnCommonConfig.ConnectionStatus
- VpnCommonConfig.IdleDisconnectSeconds
- VpnCommonConfig.ServerList
- VpnCommonConfig.Routes
- VpnCommonConfig.VpnTrigger
- VpnCommonConfig.DnsSuffix
- VpnCommonConfig.Proxy
- VpnCommonConfig.IsAutoTriggerEnabled
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnCommonConfig class

The **VpnCommonConfig** class represents the common attributes of the [**VpnConnection**](vpnconnection.md) and [**ThirdPartyVpnConnection**](thirdpartyvpnconnection.md) objects.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class VpnCommonConfig
{
  string               Name;
  string               ProfileType;
  string               ServerAddress;
  string               ProvisioningAuthority;
  boolean              RememberCredential;
  boolean              SplitTunneling;
  string               Guid;
  string               ConnectionStatus;
  uint32               IdleDisconnectSeconds;
  VpnServerAddress     ServerList[];
  MSFT_NetRoute        Routes[];
  VpnConnectionTrigger VpnTrigger;
  string               DnsSuffix;
  VpnConnectionProxy   Proxy;
  boolean              IsAutoTriggerEnabled;
};
```

## Members

The **VpnCommonConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnCommonConfig** class has these properties.

<dl> <dt>

**ConnectionStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The connection status of the VPN connection.

<dt>

<span id="Connected"></span><span id="connected"></span><span id="CONNECTED"></span>

<span id="Connected"></span><span id="connected"></span><span id="CONNECTED"></span>**Connected** ("Connected")


</dt> <dd>

Connected.

</dd> <dt>

<span id="Connecting"></span><span id="connecting"></span><span id="CONNECTING"></span>

<span id="Connecting"></span><span id="connecting"></span><span id="CONNECTING"></span>**Connecting** ("Connecting")


</dt> <dd>

In the process of connecting.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** ("Dormant")


</dt> <dd>

The connection is dormant.

</dd> <dt>

<span id="Limited"></span><span id="limited"></span><span id="LIMITED"></span>

<span id="Limited"></span><span id="limited"></span><span id="LIMITED"></span>**Limited** ("Limited")


</dt> <dd>

There connection has less than full capabilities.

</dd> <dt>

<span id="NotConnected"></span><span id="notconnected"></span><span id="NOTCONNECTED"></span>

<span id="NotConnected"></span><span id="notconnected"></span><span id="NOTCONNECTED"></span>**NotConnected** ("NotConnected")


</dt> <dd>

Not connected.

</dd> </dl>

</dd> <dt>

**DnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS suffix of the connection.

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of this VPN profile.

</dd> <dt>

**IdleDisconnectSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The amount of idle time after which a connection is terminated. A value of 0 disables the time-out.

</dd> <dt>

**IsAutoTriggerEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the VPN connection is enabled for auto-trigger; **false** if it is not.

**Windows 8 and Windows Server 2012:** The property is not available before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the current VPN connection profile.

</dd> <dt>

**ProfileType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The profile type.

<dt>

<span id="Inbox"></span><span id="inbox"></span><span id="INBOX"></span>

<span id="Inbox"></span><span id="inbox"></span><span id="INBOX"></span>**Inbox** ("Inbox")


</dt> <dd>

The profile is an inbox profile.

</dd> <dt>

<span id="ThirdParty"></span><span id="thirdparty"></span><span id="THIRDPARTY"></span>

<span id="ThirdParty"></span><span id="thirdparty"></span><span id="THIRDPARTY"></span>**ThirdParty** ("ThirdParty")


</dt> <dd>

The profile is a third party profile.

</dd> </dl>

</dd> <dt>

**ProvisioningAuthority**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The provisioning authority of the VPN profile.

**Windows 8 and Windows Server 2012:** The property is not available before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**Proxy**
</dt> <dd> <dl> <dt>

Data type: **VpnConnectionProxy**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnConnectionProxy**](vpnconnectionproxy.md)")
</dt> </dl>

The proxy settings of the VPN connection.

</dd> <dt>

**RememberCredential**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to store the credentials used for the first successful connection; otherwise, **false**.

</dd> <dt>

**Routes**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetRoute** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_NetRoute**](msft-netroute.md)")
</dt> </dl>

The list of routes to plumb on the VPN interface when the VPN profile is connected.

</dd> <dt>

**ServerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The address of the remote VPN server that the client connects to. This address is a URL, a friendly name, an IPv4 address, or an IPv6 address. This should be one of the elements of **ServerList**.

</dd> <dt>

**ServerList**
</dt> <dd> <dl> <dt>

Data type: **VpnServerAddress** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnServerAddress**](vpnserveraddress.md)")
</dt> </dl>

The VPN server list.

</dd> <dt>

**SplitTunneling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable split tunneling; **false** to disable it.

</dd> <dt>

**VpnTrigger**
</dt> <dd> <dl> <dt>

Data type: **VpnConnectionTrigger**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnConnectionTrigger**](vpnconnectiontrigger.md)")
</dt> </dl>

The trigger properties of the VPN connection.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





