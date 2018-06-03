---
title: SetByRevertToDefault method of the PS\_VpnServerIPsecConfiguration class
description: Updates an Internet Protocol Security (IPsec) VPN server configuration with default values.
audience: developer
ms.assetid: 98315dd8-8a25-4115-8250-632a03acc1f7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByRevertToDefault method
- SetByRevertToDefault method, PS_VpnServerIPsecConfiguration class
- PS_VpnServerIPsecConfiguration class, SetByRevertToDefault method
topic_type:
- apiref
api_name:
- PS_VpnServerIPsecConfiguration.SetByRevertToDefault
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByRevertToDefault method of the PS\_VpnServerIPsecConfiguration class

Updates an Internet Protocol Security (IPsec) VPN server configuration with default values.

## Syntax


```mof
uint32 SetByRevertToDefault(
  [in]  boolean                     PassThru,
  [in]  uint32                      TunnelType,
  [in]  boolean                     RevertToDefault,
  [out] VpnServerIPsecConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md) parameter returns an object.

</dd> <dt>

*TunnelType* \[in\]
</dt> <dd>

The tunnel type of the IPsec configuration.

</dd> <dt>

*RevertToDefault* \[in\]
</dt> <dd>

Indicates whether to set the IPsec configuration to the default values. **True** to get the IPsec configuration to default values; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md) object that receives the server configuration.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnServerIPsecConfiguration**](ps-vpnserveripsecconfiguration.md)
</dt> </dl>

 

 





