---
title: RemoteAccessAccountingConnectionLocal class
description: Remote Access Accounting Connection Record.
audience: developer
ms.assetid: ba01c95b-fde3-4e6d-96cc-39ad3e1035dd
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessAccountingConnectionLocal class
- RemoteAccessAccountingConnectionLocal class, described
topic_type:
- apiref
api_name:
- RemoteAccessAccountingConnectionLocal
- RemoteAccessAccountingConnectionLocal.ClientIPv4Address
- RemoteAccessAccountingConnectionLocal.ClientIPv6Address
- RemoteAccessAccountingConnectionLocal.HostName
- RemoteAccessAccountingConnectionLocal.ClientExternalAddress
- RemoteAccessAccountingConnectionLocal.TunnelType
- RemoteAccessAccountingConnectionLocal.TransitionTechnology
- RemoteAccessAccountingConnectionLocal.ConnectionStartTime
- RemoteAccessAccountingConnectionLocal.ConnectionDuration
- RemoteAccessAccountingConnectionLocal.TotalBytesIn
- RemoteAccessAccountingConnectionLocal.TotalBytesOut
- RemoteAccessAccountingConnectionLocal.ConnectionType
- RemoteAccessAccountingConnectionLocal.HealthStatus
- RemoteAccessAccountingConnectionLocal.AuthMethod
- RemoteAccessAccountingConnectionLocal.UserName
- RemoteAccessAccountingConnectionLocal.SessionId
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessAccountingConnectionLocal class

Remote Access Accounting Connection Record.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessAccountingConnectionLocal : RemoteAccessConnectionLocal
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
  string   UserName;
  uint64   SessionId;
};
```

## Members

The **RemoteAccessAccountingConnectionLocal** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessAccountingConnectionLocal** class has these properties.

<dl> <dt>

**AuthMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

negotiated Encryption Type

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

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

<span id="Machine_Kerberos___User_Kerberos"></span><span id="machine_kerberos___user_kerberos"></span><span id="MACHINE_KERBEROS___USER_KERBEROS"></span>

**Machine Kerberos & User Kerberos** ("Machine Kerberos & User Kerberos")


</dt> <dd></dd> <dt>

<span id="Machine_Kerberos___User_Kerberos"></span><span id="machine_kerberos___user_kerberos"></span><span id="MACHINE_KERBEROS___USER_KERBEROS"></span>

**Machine Kerberos & User Kerberos** ("Machine Kerberos & User Kerberos")


</dt> <dd></dd> <dt>

<span id="Machine_Certificate__User_Ntlm____User_Kerberos"></span><span id="machine_certificate__user_ntlm____user_kerberos"></span><span id="MACHINE_CERTIFICATE__USER_NTLM____USER_KERBEROS"></span>

**Machine Certificate, User Ntlm, & User Kerberos** ("Machine Certificate, User Ntlm, & User Kerberos")


</dt> <dd></dd> <dt>

<span id="Machine_Kerberos__User_Ntlm____User_Kerberos"></span><span id="machine_kerberos__user_ntlm____user_kerberos"></span><span id="MACHINE_KERBEROS__USER_NTLM____USER_KERBEROS"></span>

**Machine Kerberos, User Ntlm, & User Kerberos** ("Machine Kerberos, User Ntlm, & User Kerberos")


</dt> <dd></dd> </dl>

</dd> <dt>

**ClientExternalAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote Machine's IP Address

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**ClientIPv4Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Client inner IPv4 Address

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**ClientIPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Client inner IPv6 Address

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**ConnectionDuration**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Connection duration in seconds

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**ConnectionStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Connection start time

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**ConnectionType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Connection Type

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

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

health status

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="-"></span>

**-** ("-")


</dt> <dd></dd> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** ("Healthy")


</dt> <dd></dd> <dt>

<span id="Limited_Access"></span><span id="limited_access"></span><span id="LIMITED_ACCESS"></span>

**Limited Access** ("Limited Access")


</dt> <dd></dd> <dt>

<span id="Probation"></span><span id="probation"></span><span id="PROBATION"></span>

**Probation** ("Probation")


</dt> <dd></dd> </dl>

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote client Hostname

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**SessionId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The session identifier corresponding to this connection.

</dd> <dt>

**TotalBytesIn**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TotalBytes in for this connection

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**TotalBytesOut**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TotalBytes out for this connection

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

</dd> <dt>

**TransitionTechnology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Transition technology used for DA connection

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

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

This property is inherited from [**RemoteAccessConnectionLocal**](remoteaccessconnectionlocal.md).

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

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User Name

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





