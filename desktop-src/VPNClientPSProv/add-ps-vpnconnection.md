---
title: Add method of the PS\_VpnConnection class
description: Adds a virtual private network (VPN) connection to the Connection Manager phone book.
audience: developer
ms.assetid: 2ac4741d-87bc-4a81-a8c8-f6e0806ebafc
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_VpnConnection class
- PS_VpnConnection class, Add method
topic_type:
- apiref
api_name:
- PS_VpnConnection.Add
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_VpnConnection class

Adds a virtual private network (VPN) connection to the Connection Manager phone book.

## Syntax


```mof
static uint32 Add(
  [in]  string           Name,
  [in]  string           ServerAddress,
  [in]  string           TunnelType,
  [in]  boolean          AllUserConnection,
  [in]  boolean          RememberCredential,
  [in]  uint32           IdleDisconnectSeconds,
  [in]  string           DnsSuffix,
  [in]  boolean          SplitTunneling,
  [in]  boolean          Force,
  [in]  boolean          PassThru,
  [in]  string           L2tpPsk,
  [in]  boolean          UseWinlogonCredential,
  [in]  string           EapConfigXmlStream,
  [in]  string           AuthenticationMethod[],
  [in]  string           EncryptionLevel,
  [in]  uint8            MachineCertificateIssuerFilter[],
  [in]  string           MachineCertificateEKUFilter[],
  [in]  VpnServerAddress ServerList[],
  [out] VpnConnection    cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the VPN connection profile to create.

</dd> <dt>

*ServerAddress* \[in\]
</dt> <dd>

The address of the remote VPN server that the client connects to. This address is a URL, a friendly name, an IPv4 address, or an IPv6 address. This should be one of the elements of **ServerList**.

</dd> <dt>

*TunnelType* \[in\]
</dt> <dd>

The tunnel type that is used in the RAS configuration. The tunnel type is decided after the first successful connection.

<dt>

<span id="Ikev2"></span><span id="ikev2"></span><span id="IKEV2"></span>

<span id="Ikev2"></span><span id="ikev2"></span><span id="IKEV2"></span>**Ikev2** ("Ikev2")


</dt> <dd>

Internet Key Exchange version 2 (IKEv2).

</dd> <dt>

<span id="L2tp"></span><span id="l2tp"></span><span id="L2TP"></span>

<span id="L2tp"></span><span id="l2tp"></span><span id="L2TP"></span>**L2tp** ("L2tp")


</dt> <dd>

Layer 2 Tunneling Protocol (L2TP).

</dd> <dt>

<span id="Pptp"></span><span id="pptp"></span><span id="PPTP"></span>

<span id="Pptp"></span><span id="pptp"></span><span id="PPTP"></span>**Pptp** ("Pptp")


</dt> <dd>

Point to Point Tunneling Protocol (PPTP).

</dd> <dt>

<span id="Sstp"></span><span id="sstp"></span><span id="SSTP"></span>

<span id="Sstp"></span><span id="sstp"></span><span id="SSTP"></span>**Sstp** ("Sstp")


</dt> <dd>

Secure Socket Tunneling Protocol (SSTP).

</dd> </dl> </dd> <dt>

*AllUserConnection* \[in\]
</dt> <dd>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

*RememberCredential* \[in\]
</dt> <dd>

**True** to store the credentials used for the first successful connection; otherwise, **false**.

</dd> <dt>

*IdleDisconnectSeconds* \[in\]
</dt> <dd>

The amount of idle time after which a connection is terminated. A value of 0 disables the time-out.

</dd> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

The DNS suffix of the VPN connection.

</dd> <dt>

*SplitTunneling* \[in\]
</dt> <dd>

**True** to enable split tunneling for the VPN connection profile; otherwise, **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the supplying of the preshared key value over an unsecure channel, if L2TP is used; otherwise, **false**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the [**VpnConnection**](vpnconnection.md) object that contains the VPN configuration settings; otherwise, **false**.

</dd> <dt>

*L2tpPsk* \[in\]
</dt> <dd>

The value of the preshared key to be used for L2TP authentication. If this parameter is not specified, a certificate is used for L2TP.

</dd> <dt>

*UseWinlogonCredential* \[in\]
</dt> <dd>

**True** if the Windows logon credentials for the user are automatically used for connection with the current VPN connection profile; otherwise, **false**.

This flag is only used for authentication protocols that involve MSCHAPv2.

</dd> <dt>

*EapConfigXmlStream* \[in\]
</dt> <dd>

The contents of the EAP XML configuration file, which includes the EAP method identifier.

</dd> <dt>

*AuthenticationMethod* \[in\]
</dt> <dd>

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

<span id="MsChapv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>

<span id="MsChapv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>**MsChapv2** ("MsChapv2")


</dt> <dd>

Microsoft Challenge Handshake Authentication Protocol version 2 (MSCHAPv2).

</dd> <dt>

<span id="Pap"></span><span id="pap"></span><span id="PAP"></span>

<span id="Pap"></span><span id="pap"></span><span id="PAP"></span>**Pap** ("Pap")


</dt> <dd>

Password Authentication Protocol (PAP).

</dd> </dl> </dd> <dt>

*EncryptionLevel* \[in\]
</dt> <dd>

The encryption level for the VPN connection.

<dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>**Maximum** ("Maximum")


</dt> <dd>

Maximum encryption.

</dd> <dt>

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

</dd> </dl> </dd> <dt>

*MachineCertificateIssuerFilter* \[in\]
</dt> <dd>

A filter based on the root certificate issuer to select the Machine Certificate for authentication. This property applies when IKEv2 tunnel type along with Machine Certificate authentication method is used.

</dd> <dt>

*MachineCertificateEKUFilter* \[in\]
</dt> <dd>

A filter based on the Certificate EKU Name or OID to select the Machine Certificate for authentication. This property applies when IKEv2 tunnel type along with Machine Certificate authentication method is used.

</dd> <dt>

*ServerList* \[in\]
</dt> <dd>

The VPN servers that the client can connect to.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnection**](vpnconnection.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnection**](ps-vpnconnection.md)
</dt> </dl>

 

 





