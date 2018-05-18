---
title: ThirdPartyVpnConnection class
description: The ThirdPartyVpnConnection class represents third party VPN profiles.
audience: developer
ms.assetid: '26A926C2-C218-4362-A090-9E4D3F5BB38F'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ThirdPartyVpnConnection class", "ThirdPartyVpnConnection class, described"]
topic_type:
- apiref
api_name:
- ThirdPartyVpnConnection
- ThirdPartyVpnConnection.ServerAddress
- ThirdPartyVpnConnection.ProvisioningAuthority
- ThirdPartyVpnConnection.RememberCredential
- ThirdPartyVpnConnection.SplitTunneling
- ThirdPartyVpnConnection.IsAutoTriggerEnabled
- ThirdPartyVpnConnection.Name
- ThirdPartyVpnConnection.ProfileType
- ThirdPartyVpnConnection.Guid
- ThirdPartyVpnConnection.ConnectionStatus
- ThirdPartyVpnConnection.IdleDisconnectSeconds
- ThirdPartyVpnConnection.ServerList
- ThirdPartyVpnConnection.Routes
- ThirdPartyVpnConnection.VpnTrigger
- ThirdPartyVpnConnection.DnsSuffix
- ThirdPartyVpnConnection.Proxy
- ThirdPartyVpnConnection.VpnConfigurationXml
- ThirdPartyVpnConnection.PlugInApplicationID
- ThirdPartyVpnConnection.CustomConfiguration
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
---

# ThirdPartyVpnConnection class

The **ThirdPartyVpnConnection** class represents third party VPN profiles.**ThirdPartyVpnConnection** is derived from [**VpnCommonConfig**](vpncommonconfig.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class ThirdPartyVpnConnection : VpnCommonConfig
{
  string  ServerAddress;
  string  ProvisioningAuthority;
  boolean RememberCredential;
  boolean SplitTunneling;
  boolean IsAutoTriggerEnabled;
  string  Name;
  string  ProfileType;
  string  Guid;
  string  ConnectionStatus;
  uint32  IdleDisconnectSeconds;
  string  ServerList[];
  string  Routes[];
  string  VpnTrigger;
  string  DnsSuffix;
  string  Proxy;
  string  VpnConfigurationXml;
  string  PlugInApplicationID;
  string  CustomConfiguration;
};
```

## Members

The **ThirdPartyVpnConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **ThirdPartyVpnConnection** class has these properties.

<dl> <dt>

**ConnectionStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The connection status of the VPN connection.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

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

**CustomConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A custom configuration used by third party VPN profiles.

</dd> <dt>

**DnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS suffix of the connection.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of this VPN profile.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**IdleDisconnectSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The amount of idle time after which a connection is terminated. A value of 0 disables the time-out.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**IsAutoTriggerEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the VPN connection is enabled for auto-trigger; **false** if it is not.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

**Windows 8 and Windows Server 2012:** The property is not available before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the current VPN connection profile.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**PlugInApplicationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The identifier of the third party VPN application.

</dd> <dt>

**ProfileType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The profile type.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

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

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

**Windows 8 and Windows Server 2012:** The property is not available before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**Proxy**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnConnectionProxy**](ps-vpnconnectionproxy.md)")
</dt> </dl>

The proxy settings of the VPN connection.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**RememberCredential**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to store the credentials used for the first successful connection; otherwise, **false**.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**Routes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_NetRoute**](msft-netroute.md)")
</dt> </dl>

The list of routes to plumb on the VPN interface when the VPN profile is connected.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**ServerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The address of the remote VPN server that the client connects to. This address is a URL, a friendly name, an IPv4 address, or an IPv6 address. This should be one of the elements of **ServerList**.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**ServerList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnServerAddress**](vpnserveraddress.md)")
</dt> </dl>

The VPN server list.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**SplitTunneling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable split tunneling; **false** to disable it.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> <dt>

**VpnConfigurationXml**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An XML representation of this instance, which can be used as input for [**MSFT\_VpnConnection::Set**](set-msft-vpnconnection.md).

</dd> <dt>

**VpnTrigger**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnConnectionTrigger**](vpnconnectiontrigger.md)")
</dt> </dl>

The trigger properties of the VPN connection.

This property is inherited from [**VpnCommonConfig**](vpncommonconfig.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**VpnCommonConfig**](vpncommonconfig.md)
</dt> </dl>

 

 





