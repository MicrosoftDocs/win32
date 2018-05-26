---
title: VpnServerAddress class
description: The VpnServerAddress class represents a VPN server.
audience: developer
ms.assetid: 360571EC-7178-4544-9E6C-346D6F073996
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnServerAddress class
- VpnServerAddress class, described
topic_type:
- apiref
api_name:
- VpnServerAddress
- VpnServerAddress.ServerAddress
- VpnServerAddress.FriendlyName
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnServerAddress class

The **VpnServerAddress** class represents a VPN server.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class VpnServerAddress
{
  string ServerAddress;
  string FriendlyName;
};
```

## Members

The **VpnServerAddress** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnServerAddress** class has these properties.

<dl> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The friendly name of the remote VPN server.

</dd> <dt>

**ServerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The address of the remote VPN server that the client connects to. This address is a URL, a friendly name, an IPv4 address, or an IPv6 address.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





