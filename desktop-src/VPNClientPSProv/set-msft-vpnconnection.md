---
title: Set method of the MSFT\_VpnConnection class
description: Creates or modifies a virtual private network (VPN) connection profile.
audience: developer
ms.assetid: a6ac373f-1085-4b35-875a-d03ebdeb947a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, MSFT_VpnConnection class
- MSFT_VpnConnection class, Set method
topic_type:
- apiref
api_name:
- MSFT_VpnConnection.Set
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the MSFT\_VpnConnection class

Creates or modifies a virtual private network (VPN) connection profile.

## Syntax


```mof
static uint32 Set(
  [in] string Profile
);
```



## Parameters

<dl> <dt>

*Profile* \[in\]
</dt> <dd>

A string representation of the VPN connection profile to be modified or created. The **VpnConfigurationXml** property of the [**VpnConnection**](vpnconnection.md) class can be used as input for this parameter.

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

[**MSFT\_VpnConnection**](msft-vpnconnection.md)
</dt> </dl>

 

 





