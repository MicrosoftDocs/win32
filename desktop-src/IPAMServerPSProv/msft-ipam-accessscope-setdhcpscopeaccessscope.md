---
Description: Set access scope on an array of DHCP scopes from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5a16be06-3279-48ff-8a93-260682d14110
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetDhcpScopeAccessScope method of the MSFT\_IPAM\_AccessScope class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetDhcpScopeAccessScope method of the MSFT\_IPAM\_AccessScope class

Set access scope on an array of DHCP scopes from IPAM.

## Syntax


```mof
uint32 SetDhcpScopeAccessScope(
  [in]  boolean             IpamDhcpScope,
  [in]  string              AccessScopePath,
  [in]  boolean             IsInheritedAccessScope,
  [in]  MSFT_IPAM_DhcpScope InputObject[],
  [out] MSFT_IPAM_DhcpScope Output[]
);
```



## Parameters

<dl> <dt>

*IpamDhcpScope* \[in\]
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

An array of [**MSFT\_IPAM\_DhcpScope**](msft-ipam-dhcpscope.md) embedded instances.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the scope as an array of [**MSFT\_IPAM\_DhcpScope**](msft-ipam-dhcpscope.md) embedded instances.

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

 

 




