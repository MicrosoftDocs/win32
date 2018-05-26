---
title: Get method of the PS\_VpnServerIPsecConfiguration class
description: Retrieves an Internet Protocol Security (IPsec) VPN server configuration.
audience: developer
ms.assetid: 3cee426d-87f3-4ac9-88d7-f94bc375825b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_VpnServerIPsecConfiguration class
- PS_VpnServerIPsecConfiguration class, Get method
topic_type:
- apiref
api_name:
- PS_VpnServerIPsecConfiguration.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_VpnServerIPsecConfiguration class

Retrieves an Internet Protocol Security (IPsec) VPN server configuration.

## Syntax


```mof
uint32 Get(
  [in]  uint32                      TunnelType,
  [out] VpnServerIPsecConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*TunnelType* \[in\]
</dt> <dd>

The tunnel type of the server configuration.

**Windows Server 2012:** This parameter is not available before Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The cmdlet output.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnServerIPsecConfiguration**](ps-vpnserveripsecconfiguration.md)
</dt> </dl>

 

 





