---
title: PS\_VpnConnection class
description: The PS\_VpnConnection class contains the profile management functionality of the Get Connected wizard (GCW).
audience: developer
ms.assetid: 2ac4741d-87bc-4a81-a8c8-f6e0806ebafc
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnConnection class
- PS_VpnConnection class, described
topic_type:
- apiref
api_name:
- PS_VpnConnection
- PS_VpnConnection.Name
- PS_VpnConnection.AllUserConnection
- PS_VpnConnection.ServerAddress
- PS_VpnConnection.ProfileType
- PS_VpnConnection.ProvisioningAuthority
- PS_VpnConnection.RememberCredential
- PS_VpnConnection.SplitTunneling
- PS_VpnConnection.Guid
- PS_VpnConnection.ConnectionStatus
- PS_VpnConnection.IdleDisconnectSeconds
- PS_VpnConnection.DnsSuffix
- PS_VpnConnection.TunnelType
- PS_VpnConnection.UseWinlogonCredential
- PS_VpnConnection.AuthenticationMethod
- PS_VpnConnection.EncryptionLevel
- PS_VpnConnection.L2tpPsk
- PS_VpnConnection.L2tpIPsecAuth
- PS_VpnConnection.EapConfigXmlStream
- PS_VpnConnection.NapState
- PS_VpnConnection.VpnConfigurationXml
- PS_VpnConnection.MachineCertificateEKUFilter
- PS_VpnConnection.MachineCertificateIssuerFilter
- PS_VpnConnection.ApplicationID
- PS_VpnConnection.ServerList
- PS_VpnConnection.Routes
- PS_VpnConnection.DnsConfig
- PS_VpnConnection.DnsSuffixSearchList
- PS_VpnConnection.TrustedNetwork
- PS_VpnConnection.Proxy
- PS_VpnConnection.PlugInApplicationID
- PS_VpnConnection.CustomConfiguration
- PS_VpnConnection.IsAutoTriggerEnabled
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_VpnConnection class

The **PS\_VpnConnection** class contains the profile management functionality of the Get Connected wizard (GCW).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), InPartition("local-system", "local-user"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnection
{
  string                                  Name;
  boolean                                 AllUserConnection;
  string                                  ServerAddress;
  string                                  ProfileType;
  string                                  ProvisioningAuthority;
  boolean                                 RememberCredential;
  boolean                                 SplitTunneling;
  string                                  Guid;
  string                                  ConnectionStatus;
  uint32                                  IdleDisconnectSeconds;
  string                                  DnsSuffix;
  string                                  TunnelType;
  boolean                                 UseWinlogonCredential;
  string                                  AuthenticationMethod[];
  string                                  EncryptionLevel;
  string                                  L2tpPsk;
  string                                  L2tpIPsecAuth;
  string                                  EapConfigXmlStream;
  string                                  NapState;
  string                                  VpnConfigurationXml;
  string                                  MachineCertificateEKUFilter[];
  string                                  MachineCertificateIssuerFilter;
  string                                  ApplicationID[];
  PS_VpnServerAddress                     ServerList[];
  PS_VpnConnectionRoute                   Routes[];
  PS_VpnConnectionTriggerDnsConfiguration DnsConfig[];
  string                                  DnsSuffixSearchList[];
  string                                  TrustedNetwork[];
  PS_VpnConnectionProxy                   Proxy;
  string                                  PlugInApplicationID;
  string                                  CustomConfiguration;
  boolean                                 IsAutoTriggerEnabled;
};
```

## Members

The **PS\_VpnConnection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **PS\_VpnConnection** class has these methods.



| Method                                                      | Description                                                                                                   |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-vpnconnection.md)                         | Adds a virtual private network (VPN) connection to the Connection Manager phone book.<br/>              |
| [**Get**](get-ps-vpnconnection.md)                         | Retrieves virtual private network (VPN) connection profiles.<br/>                                       |
| [**NewByThirdParty**](newbythirdparty-ps-vpnconnection.md) | Adds a Third Party virtual private network (VPN) connection to the Connection Manager phone book.<br/>  |
| [**Remove**](remove-ps-vpnconnection.md)                   | Removes a virtual private network (VPN) connection profile from the Connection Manager phone book.<br/> |
| [**Set**](set-ps-vpnconnection.md)                         | Modifies an existing virtual private network (VPN) connection profile.<br/>                             |
| [**SetByThirdParty**](setbythirdparty-ps-vpnconnection.md) | Modifies a third party virtual private network (VPN) connection profile.<br/>                           |



 

### Properties

The **PS\_VpnConnection** class has these properties.

<dl> <dt>

**AllUserConnection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

**ApplicationID**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The identifiers of applications that auto-trigger the connection.

</dd> <dt>

**AuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The authentication protocols to use for the VPN connection.

<dt>

<span id="Chap"></span><span id="chap"></span><span id="CHAP"></span>

<span id="Chap"></span><span id="chap"></span><span id="CHAP"></span>**Chap** ("Chap")


</dt> <dd>

Challenge Handshake Authentication Protocol (CHAP).

</dd> <dt>

<span id="Eap"></span><span id="eap"></span><span id="EAP"></span>

<span id="Eap"></span><span id="eap"></span><span id="EAP"></span>**Eap** ("Eap")


</dt> <dd>

Extensible Authentication Protocol (EAP).

</dd> <dt>

<span id="MachineCertificate"></span><span id="machinecertificate"></span><span id="MACHINECERTIFICATE"></span>

<span id="MachineCertificate"></span><span id="machinecertificate"></span><span id="MACHINECERTIFICATE"></span>**MachineCertificate** ("MachineCertificate")


</dt> <dd>

A machine certificate.

</dd> <dt>

<span id="MsChapv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>

<span id="MsChapv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>**MsChapv2** ("MsChapv2")


</dt> <dd>

Microsoft Challenge Handshake Authentication Protocol version 2 (MSCHAPv2).

</dd> <dt>

<span id="Pap"></span><span id="pap"></span><span id="PAP"></span>

<span id="Pap"></span><span id="pap"></span><span id="PAP"></span>**Pap** ("Pap")


</dt> <dd>

Password Authentication Protocol (PAP).

</dd> </dl>

</dd> <dt>

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

**CustomConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A custom configuration used by third party VPN profiles.

</dd> <dt>

**DnsConfig**
</dt> <dd> <dl> <dt>

Data type: **PS\_VpnConnectionTriggerDnsConfiguration** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**PS\_VpnConnectionTriggerDnsConfiguration**](ps-vpnconnectiontriggerdnsconfiguration.md)")
</dt> </dl>

The trigger DNS configurations.

</dd> <dt>

**DnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS suffix of the VPN connection.

</dd> <dt>

**DnsSuffixSearchList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS suffix search list for the auto-triggered VPN connection.

</dd> <dt>

**EapConfigXmlStream**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An XML stream of the detailed EAP configuration for the VPN connection profile.

</dd> <dt>

**EncryptionLevel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The encryption level for the VPN connection.

<dt>

<span id="NoEncryption"></span><span id="noencryption"></span><span id="NOENCRYPTION"></span>

<span id="NoEncryption"></span><span id="noencryption"></span><span id="NOENCRYPTION"></span>**NoEncryption** ("NoEncryption")


</dt> <dd>

No encryption.

</dd> <dt>

<span id="Optional"></span><span id="optional"></span><span id="OPTIONAL"></span>

<span id="Optional"></span><span id="optional"></span><span id="OPTIONAL"></span>**Optional** ("Optional")


</dt> <dd>

Optional encryption.

</dd> <dt>

<span id="Required"></span><span id="required"></span><span id="REQUIRED"></span>

<span id="Required"></span><span id="required"></span><span id="REQUIRED"></span>**Required** ("Required")


</dt> <dd>

Required encryption.

</dd> <dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>**Maximum** ("Maximum")


</dt> <dd>

Maximum encryption.

</dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** ("Custom")


</dt> <dd>

Custom encryption.

**Windows 8 and Windows Server 2012:** This value is not available before Windows 8.1 and Windows Server 2012 R2.

</dd> </dl>

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GUID of this VPN profile.

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

**Windows 8 and Windows Server 2012:** This property is not available before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**L2tpIPsecAuth**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The authentication method of Layer Two Tunneling Protocol (L2TP) Internet Protocol security (IPSec).

<dt>

<span id="Certificate"></span><span id="certificate"></span><span id="CERTIFICATE"></span>

<span id="Certificate"></span><span id="certificate"></span><span id="CERTIFICATE"></span>**Certificate** ("Certificate")


</dt> <dd>

Machine certificate.

</dd> <dt>

<span id="Psk"></span><span id="psk"></span><span id="PSK"></span>

<span id="Psk"></span><span id="psk"></span><span id="PSK"></span>**Psk** ("Psk")


</dt> <dd>

Preshared key.

</dd> </dl>

</dd> <dt>

**L2tpPsk**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The value of the preshared key to be used for L2TP authentication. If this parameter is not specified, a certificate is used for L2TP.

</dd> <dt>

**MachineCertificateEKUFilter**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A filter based on the Certificate EKU Name or OID to select the Machine Certificate for authentication. This property applies when IKEv2 tunnel type along with Machine Certificate authentication method is used.

</dd> <dt>

**MachineCertificateIssuerFilter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A filter based on the root certificate issuer to select the Machine Certificate for authentication. This property applies when IKEv2 tunnel type along with Machine Certificate authentication method is used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the current VPN connection profile.

</dd> <dt>

**NapState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Network Access Protection (NAP) health status of the connection. This property applies when the Protected Extensible Authentication Protocol (PEAP) authentication protocol is used.

<dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** ("Error")


</dt> <dd>

An error occurred.

</dd> <dt>

<span id="NoConnection"></span><span id="noconnection"></span><span id="NOCONNECTION"></span>

<span id="NoConnection"></span><span id="noconnection"></span><span id="NOCONNECTION"></span>**NoConnection** ("NoConnection")


</dt> <dd>

No connection has been made.

</dd> <dt>

<span id="NotNapCapable"></span><span id="notnapcapable"></span><span id="NOTNAPCAPABLE"></span>

<span id="NotNapCapable"></span><span id="notnapcapable"></span><span id="NOTNAPCAPABLE"></span>**NotNapCapable** ("NotNapCapable")


</dt> <dd>

NAP is not supported.

</dd> <dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>**Success** ("Success")


</dt> <dd>

The connection is successful.

</dd> </dl>

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

The VPN connection profile type.

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

The provisioning authority of the VPN connection profile.

**Windows 8 and Windows Server 2012:** This property is not available before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**Proxy**
</dt> <dd> <dl> <dt>

Data type: **PS\_VpnConnectionProxy**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**PS\_VpnConnectionProxy**](ps-vpnconnectionproxy.md)")
</dt> </dl>

The proxy settings of the VPN connection.

</dd> <dt>

**RememberCredential**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to save the credentials for the VPN connection upon the first successful connection; otherwise, **false**.

</dd> <dt>

**Routes**
</dt> <dd> <dl> <dt>

Data type: **PS\_VpnConnectionRoute** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**PS\_VpnConnectionRoute**](ps-vpnconnectionroute.md)")
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

Data type: **PS\_VpnServerAddress** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**PS\_VpnServerAddress**](ps-vpnserveraddress.md)")
</dt> </dl>

The VPN servers that the client can connect to.

</dd> <dt>

**SplitTunneling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable split tunneling for the VPN connection profile; otherwise, **false**.

</dd> <dt>

**TrustedNetwork**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The trusted network DNS suffixes for the auto-triggered VPN connection.

</dd> <dt>

**TunnelType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The tunnel type that is used in the RAS configuration. The tunnel type is decided after the first successful connection.

<dt>

<span id="Pptp"></span><span id="pptp"></span><span id="PPTP"></span>

<span id="Pptp"></span><span id="pptp"></span><span id="PPTP"></span>**Pptp** ("Pptp")


</dt> <dd>

Point to Point Tunneling Protocol (PPTP).

</dd> <dt>

<span id="L2tp"></span><span id="l2tp"></span><span id="L2TP"></span>

<span id="L2tp"></span><span id="l2tp"></span><span id="L2TP"></span>**L2tp** ("L2tp")


</dt> <dd>

Layer 2 Tunneling Protocol (L2TP).

</dd> <dt>

<span id="Sstp"></span><span id="sstp"></span><span id="SSTP"></span>

<span id="Sstp"></span><span id="sstp"></span><span id="SSTP"></span>**Sstp** ("Sstp")


</dt> <dd>

Secure Socket Tunneling Protocol (SSTP).

</dd> <dt>

<span id="Ikev2"></span><span id="ikev2"></span><span id="IKEV2"></span>

<span id="Ikev2"></span><span id="ikev2"></span><span id="IKEV2"></span>**Ikev2** ("Ikev2")


</dt> <dd>

Internet Key Exchange version 2 (IKEv2).

</dd> <dt>

<span id="Automatic"></span><span id="automatic"></span><span id="AUTOMATIC"></span>

<span id="Automatic"></span><span id="automatic"></span><span id="AUTOMATIC"></span>**Automatic** ("Automatic")


</dt> <dd>

The tunnel types are tried in sequence.

</dd> </dl>

</dd> <dt>

**UseWinlogonCredential**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if the Winlogon credentials for the user are automatically used to connect; otherwise, **false**. This flag is only used for authentication protocols that use MSCHAPv2 or EAP-MSCHAPv2 authentication methods.

</dd> <dt>

**VpnConfigurationXml**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An XML representation of this instance, which can be used as input for [**Set**](set-msft-vpnconnection.md) method of the [**MSFT\_VpnConnection**](msft-vpnconnection.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





