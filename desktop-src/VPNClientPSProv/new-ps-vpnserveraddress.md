---
title: New method of the PS\_VpnServerAddress class
description: Creates a VPN server object.
audience: developer
ms.assetid: '360571EC-7178-4544-9E6C-346D6F073996'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["New method", "New method, PS_VpnServerAddress class", "PS_VpnServerAddress class, New method"]
topic_type:
- apiref
api_name:
- PS_VpnServerAddress.New
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# New method of the PS\_VpnServerAddress class

Creates a VPN server object.

## Syntax


```mof
uint32 New(
  [in]  string           ServerAddress,
  [in]  string           FriendlyName,
  [in]  boolean          PassThru,
  [out] VpnServerAddress cmdletOutput
);
```



## Parameters

<dl> <dt>

*ServerAddress* \[in\]
</dt> <dd>

The address of the remote VPN server that the client connects to. This address is a URL, a friendly name, an IPv4 address, or an IPv6 address.

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The friendly name of the VPN server.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnServerAddress**](vpnserveraddress.md) object; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnServerAddress**](vpnserveraddress.md) object (if *PassThru* is **true**). The **ServerAddress** and **FriendlyName** fields are populated.

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

[**PS\_VpnServerAddress**](ps-vpnserveraddress.md)
</dt> </dl>

 

 





