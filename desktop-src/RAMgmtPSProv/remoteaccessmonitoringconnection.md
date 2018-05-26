---
title: RemoteAccessMonitoringConnection class
description: Remote Access Monitoring Connection Record.
audience: developer
ms.assetid: 1e2c809a-0446-40d6-afa8-fbd2fc9546c5
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessMonitoringConnection class
- RemoteAccessMonitoringConnection class, described
topic_type:
- apiref
api_name:
- RemoteAccessMonitoringConnection
- RemoteAccessMonitoringConnection.ClientIPv4Address
- RemoteAccessMonitoringConnection.ClientIPv6Address
- RemoteAccessMonitoringConnection.HostName
- RemoteAccessMonitoringConnection.ClientExternalAddress
- RemoteAccessMonitoringConnection.TunnelType
- RemoteAccessMonitoringConnection.TransitionTechnology
- RemoteAccessMonitoringConnection.ConnectionStartTime
- RemoteAccessMonitoringConnection.ConnectionDuration
- RemoteAccessMonitoringConnection.TotalBytesIn
- RemoteAccessMonitoringConnection.TotalBytesOut
- RemoteAccessMonitoringConnection.ConnectionType
- RemoteAccessMonitoringConnection.HealthStatus
- RemoteAccessMonitoringConnection.AuthMethod
- RemoteAccessMonitoringConnection.UserActivityState
- RemoteAccessMonitoringConnection.Bandwidth
- RemoteAccessMonitoringConnection.UserName
- RemoteAccessMonitoringConnection.RoutingDomain
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessMonitoringConnection class

Remote Access Monitoring Connection Record

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("2.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessMonitoringConnection : RemoteAccessConnection
{
  string   ClientIPv4Address;
  string   ClientIPv6Address;
  string   HostName;
  string   ClientExternalAddress;
  string   TunnelType;
  string   TransitionTechnology;
  datetime ConnectionStartTime;
  uint32   ConnectionDuration;
  uint64   TotalBytesIn;
  uint64   TotalBytesOut;
  string   ConnectionType;
  string   HealthStatus;
  string   AuthMethod;
  string   UserActivityState;
  uint32   Bandwidth;
  string   UserName[];
  string   RoutingDomain;
};
```

## Members

The **RemoteAccessMonitoringConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessMonitoringConnection** class has these properties.

<dl> <dt>

**AuthMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

negotiated Encryption Type

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="MSChapv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>

**MSChapv2** ("MSChapv2")


</dt> <dd></dd> <dt>

<span id="Eap_MSChapv2"></span><span id="eap_mschapv2"></span><span id="EAP_MSCHAPV2"></span>

**Eap MSChapv2** ("Eap MSChapv2")


</dt> <dd></dd> <dt>

<span id="Eap_Tls"></span><span id="eap_tls"></span><span id="EAP_TLS"></span>

**Eap Tls** ("Eap Tls")


</dt> <dd></dd> <dt>

<span id="Eap_Peap"></span><span id="eap_peap"></span><span id="EAP_PEAP"></span>

**Eap Peap** ("Eap Peap")


</dt> <dd></dd> <dt>

<span id="Eap_Unknown"></span><span id="eap_unknown"></span><span id="EAP_UNKNOWN"></span>

**Eap Unknown** ("Eap Unknown")


</dt> <dd></dd> <dt>

<span id="Machine_Certificate"></span><span id="machine_certificate"></span><span id="MACHINE_CERTIFICATE"></span>

**Machine Certificate** ("Machine Certificate")


</dt> <dd></dd> <dt>

<span id="Pap"></span><span id="pap"></span><span id="PAP"></span>

**Pap** ("Pap")


</dt> <dd></dd> <dt>

<span id="Chap"></span><span id="chap"></span><span id="CHAP"></span>

**Chap** ("Chap")


</dt> <dd></dd> <dt>

<span id="Psk_MSChapv2"></span><span id="psk_mschapv2"></span><span id="PSK_MSCHAPV2"></span>

**Psk MSChapv2** ("Psk MSChapv2")


</dt> <dd></dd> <dt>

<span id="Psk_Eap_MSChapv2"></span><span id="psk_eap_mschapv2"></span><span id="PSK_EAP_MSCHAPV2"></span>

**Psk Eap MSChapv2** ("Psk Eap MSChapv2")


</dt> <dd></dd> <dt>

<span id="Psk_Eap_Tls"></span><span id="psk_eap_tls"></span><span id="PSK_EAP_TLS"></span>

**Psk Eap Tls** ("Psk Eap Tls")


</dt> <dd></dd> <dt>

<span id="Psk_Eap_Peap"></span><span id="psk_eap_peap"></span><span id="PSK_EAP_PEAP"></span>

**Psk Eap Peap** ("Psk Eap Peap")


</dt> <dd></dd> <dt>

<span id="Psk_Pap"></span><span id="psk_pap"></span><span id="PSK_PAP"></span>

**Psk Pap** ("Psk Pap")


</dt> <dd></dd> <dt>

<span id="Psk_Chap"></span><span id="psk_chap"></span><span id="PSK_CHAP"></span>

**Psk Chap** ("Psk Chap")


</dt> <dd></dd> <dt>

<span id="Machine_Kerberos"></span><span id="machine_kerberos"></span><span id="MACHINE_KERBEROS"></span>

**Machine Kerberos** ("Machine Kerberos")


</dt> <dd></dd> <dt>

<span id="User_Kerberos"></span><span id="user_kerberos"></span><span id="USER_KERBEROS"></span>

**User Kerberos** ("User Kerberos")


</dt> <dd></dd> <dt>

<span id="User_Ntlm"></span><span id="user_ntlm"></span><span id="USER_NTLM"></span>

**User Ntlm** ("User Ntlm")


</dt> <dd></dd> <dt>

<span id="Machine_Certificate___User_Ntlm"></span><span id="machine_certificate___user_ntlm"></span><span id="MACHINE_CERTIFICATE___USER_NTLM"></span>

**Machine Certificate & User Ntlm** ("Machine Certificate & User Ntlm")


</dt> <dd></dd> <dt>

<span id="Machine_Kerberos___User_Ntlm"></span><span id="machine_kerberos___user_ntlm"></span><span id="MACHINE_KERBEROS___USER_NTLM"></span>

**Machine Kerberos & User Ntlm** ("Machine Kerberos & User Ntlm")


</dt> <dd></dd> <dt>

<span id="Machine_Certificate___User_Kerberos"></span><span id="machine_certificate___user_kerberos"></span><span id="MACHINE_CERTIFICATE___USER_KERBEROS"></span>

**Machine Certificate & User Kerberos** ("Machine Certificate & User Kerberos")


</dt> <dd></dd> <dt>




</dt> <dd></dd> <dt>




</dt> <dd></dd> <dt>

<span id="Machine_Certificate__User_Ntlm____User_Kerberos"></span><span id="machine_certificate__user_ntlm____user_kerberos"></span><span id="MACHINE_CERTIFICATE__USER_NTLM____USER_KERBEROS"></span>

**Machine Certificate, User Ntlm, & User Kerberos** ("Machine Certificate, User Ntlm, & User Kerberos")


</dt> <dd></dd> <dt>

<span id="Machine_Kerberos__User_Ntlm____User_Kerberos"></span><span id="machine_kerberos__user_ntlm____user_kerberos"></span><span id="MACHINE_KERBEROS__USER_NTLM____USER_KERBEROS"></span>

**Machine Kerberos, User Ntlm, & User Kerberos** ("Machine Kerberos, User Ntlm, & User Kerberos")


</dt> <dd></dd> </dl>

</dd> <dt>

**Bandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bandwidth

</dd> <dt>

**ClientExternalAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote Machine's IP Address

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**ClientIPv4Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Client inner IPv4 Address

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**ClientIPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Client inner IPv6 Address

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**ConnectionDuration**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Connection duration in seconds

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**ConnectionStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Connection start time

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**ConnectionType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Connection Type

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Vpn"></span><span id="vpn"></span><span id="VPN"></span>

**Vpn** ("Vpn")


</dt> <dd></dd> <dt>

<span id="DirectAccess"></span><span id="directaccess"></span><span id="DIRECTACCESS"></span>

**DirectAccess** ("DirectAccess")


</dt> <dd></dd> </dl>

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported starting with Windows Server 2016.

**Windows Server 2012 R2 and Windows Server 2012:** Indicates the health status.

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

The possible values are.

<dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("-")


</dt> <dd></dd> <dt>



 ("Healthy")


</dt> <dd></dd> <dt>



 ("Limited Access")


</dt> <dd></dd> <dt>



 ("Probation")


</dt> <dd></dd> </dl>

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote client Hostname

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The routing domain of the connection record

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

</dd> <dt>

**TotalBytesIn**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total incoming bytes for this connection

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**TotalBytesOut**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total outgoing bytes for this connection

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

</dd> <dt>

**TransitionTechnology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Transition technology used for direct access connection

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** ("Other")


</dt> <dd></dd> <dt>

<span id="Native_IPv6"></span><span id="native_ipv6"></span><span id="NATIVE_IPV6"></span>

**Native IPv6** ("Native IPv6")


</dt> <dd></dd> <dt>

<span id="6to4"></span><span id="6TO4"></span>

**6to4** ("6to4")


</dt> <dd></dd> <dt>

<span id="Isatap"></span><span id="isatap"></span><span id="ISATAP"></span>

**Isatap** ("Isatap")


</dt> <dd></dd> <dt>

<span id="Teredo"></span><span id="teredo"></span><span id="TEREDO"></span>

**Teredo** ("Teredo")


</dt> <dd></dd> <dt>

<span id="IPHttps"></span><span id="iphttps"></span><span id="IPHTTPS"></span>

**IPHttps** ("IPHttps")


</dt> <dd></dd> </dl>

</dd> <dt>

**TunnelType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Tunnel type

This property is inherited from [**RemoteAccessConnection**](remoteaccessconnection.md).

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pptp"></span><span id="pptp"></span><span id="PPTP"></span>

**Pptp** ("Pptp")


</dt> <dd></dd> <dt>

<span id="L2tp"></span><span id="l2tp"></span><span id="L2TP"></span>

**L2tp** ("L2tp")


</dt> <dd></dd> <dt>

<span id="Sstp"></span><span id="sstp"></span><span id="SSTP"></span>

**Sstp** ("Sstp")


</dt> <dd></dd> <dt>

<span id="Ikev2"></span><span id="ikev2"></span><span id="IKEV2"></span>

**Ikev2** ("Ikev2")


</dt> <dd></dd> <dt>

<span id="Esp"></span><span id="esp"></span><span id="ESP"></span>

**Esp** ("Esp")


</dt> <dd></dd> </dl>

</dd> <dt>

**UserActivityState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User activity state

The possible values are.

<dt>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>

**Idle** ("Idle")


</dt> <dd></dd> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> </dl>

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Users in this connection

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





