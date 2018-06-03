---
title: NewByThirdParty method of the PS\_VpnConnection class
description: Adds a Third Party VPN connection to the Connection Manager phone book.
audience: developer
ms.assetid: A77A3C2A-EFD7-4E87-92D4-2711C0D55BC4
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewByThirdParty method
- NewByThirdParty method, PS_VpnConnection class
- PS_VpnConnection class, NewByThirdParty method
topic_type:
- apiref
api_name:
- PS_VpnConnection.NewByThirdParty
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewByThirdParty method of the PS\_VpnConnection class

Adds a Third Party VPN connection to the Connection Manager phone book.

## Syntax


```mof
uint32 NewByThirdParty(
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
  [out] ThirdPartyVpnConnection cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the third-party VPN connection profile to be created.

</dd> <dt>

*ServerAddress* \[in\]
</dt> <dd>

The address of the remote VPN server that the client connects to. This address is a URL, a friendly name, an IPv4 address, or an IPv6 address. This should be one of the elements of **ServerList**.

</dd> <dt>

*RememberCredential* \[in\]
</dt> <dd>

**True** to store in the cache the credentials that are supplied for the first successful connection; otherwise, **false**.

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

**True** to force supplying the preshared key value over an insecure channel if L2TP is used; otherwise, **false**.

</dd> <dt>

*ServerList* \[in\]
</dt> <dd>

The list of VPN servers that the VPN client can connect to.

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

 

 





