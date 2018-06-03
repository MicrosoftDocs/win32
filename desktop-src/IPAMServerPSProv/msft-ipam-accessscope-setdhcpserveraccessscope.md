---
Description: Set access scope on an array of DHCP servers from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dcb473c7-6e0e-4106-9a47-83e6a52eb223
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetDhcpServerAccessScope method of the MSFT\_IPAM\_AccessScope class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDhcpServerAccessScope method of the MSFT\_IPAM\_AccessScope class

Set access scope on an array of DHCP servers from IPAM.

## Syntax


```mof
uint32 SetDhcpServerAccessScope(
  [in]  boolean              IpamDhcpServer,
  [in]  string               AccessScopePath,
  [in]  boolean              IsInheritedAccessScope,
  [in]  MSFT_IPAM_DhcpServer InputObject[],
  [out] MSFT_IPAM_DhcpServer Output[]
);
```



## Parameters

<dl> <dt>

*IpamDhcpServer* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AccessScopePath* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*IsInheritedAccessScope* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

An array of [**MSFT\_IPAM\_DhcpServer**](msft-ipam-dhcpserver.md) embedded instances.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the scope as an array of [**MSFT\_IPAM\_DhcpServer**](msft-ipam-dhcpserver.md) embedded instances.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_AccessScope**](msft-ipam-accessscope.md)
</dt> </dl>

 

 




