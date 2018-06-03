---
title: SetByThirdParty method of the PS\_VpnConnection class
description: Modifies a third party virtual private network (VPN) connection profile.
audience: developer
ms.assetid: EF33F2D7-BE7D-461A-97A3-9D59B20A0462
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByThirdParty method
- SetByThirdParty method, PS_VpnConnection class
- PS_VpnConnection class, SetByThirdParty method
topic_type:
- apiref
api_name:
- PS_VpnConnection.SetByThirdParty
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByThirdParty method of the PS\_VpnConnection class

Modifies a third party virtual private network (VPN) connection profile.

## Syntax


```mof
uint32 SetByThirdParty(
  [in]  string                  Name,
  [in]  string                  ServerAddress,
  [in]  boolean                 RememberCredential,
  [in]  boolean                 SplitTunneling,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  VpnServerAddress        ServerList[],
  [in]  string                  DnsSuffix,
  [in]  uint32                  IdleDisconnectSeconds,
  [in]  string                  PlugInApplicationID,
  [in]  string                  CustomConfiguration,
  [in]  boolean                 ThirdPartyVpn,
  [out] ThirdPartyVpnConnection cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the third-party VPN connection profile to be modified.

</dd> <dt>

*ServerAddress* \[in\]
</dt> <dd>

The address of the remote VPN server that the client connects to. This address is a URL, a friendly name, an IPv4 address, or an IPv6 address. This should be one of the elements of **ServerList**.

</dd> <dt>

*RememberCredential* \[in\]
</dt> <dd>

**True** to store the credentials that are supplied upon the first successful connection; otherwise, **false**.

</dd> <dt>

*SplitTunneling* \[in\]
</dt> <dd>

**True** to enable split tunneling for the VPN connection profile; otherwise, **false**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the [**ThirdPartyVpnConnection**](thirdpartyvpnconnection.md) object that contains the VPN configuration settings; otherwise, **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the supplying of the preshared key value over an unsecure channel, if L2TP is used; otherwise, **false**.

</dd> <dt>

*ServerList* \[in\]
</dt> <dd>

The VPN servers that the client can connect to.

</dd> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

The DNS suffix of the VPN connection.

</dd> <dt>

*IdleDisconnectSeconds* \[in\]
</dt> <dd>

The amount of idle time after which a connection is terminated. A value of 0 disables the time-out.

</dd> <dt>

*PlugInApplicationID* \[in\]
</dt> <dd>

The identifier of the third party VPN application.

</dd> <dt>

*CustomConfiguration* \[in\]
</dt> <dd>

A custom configuration used by third party VPN profiles.

</dd> <dt>

*ThirdPartyVpn* \[in\]
</dt> <dd>

**True** if the cmdlet is being executed for a third party profile; otherwise, **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**ThirdPartyVpnConnection**](thirdpartyvpnconnection.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                             |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnection**](ps-vpnconnection.md)
</dt> </dl>

 

 





