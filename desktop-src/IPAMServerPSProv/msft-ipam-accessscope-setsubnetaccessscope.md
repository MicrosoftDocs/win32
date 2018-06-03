---
Description: Set access scope on an array of IP Subnets from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6bf6547-f0bc-483d-9581-3d4ac8a0d2fe
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetSubnetAccessScope method of the MSFT\_IPAM\_AccessScope class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetSubnetAccessScope method of the MSFT\_IPAM\_AccessScope class

Set access scope on an array of IP Subnets from IPAM.

## Syntax


```mof
uint32 SetSubnetAccessScope(
  [in]  boolean          IpamSubnet,
  [in]  string           AccessScopePath,
  [in]  boolean          IsInheritedAccessScope,
  [in]  MSFT_IPAM_Subnet InputObject[],
  [out] MSFT_IPAM_Subnet Output[]
);
```



## Parameters

<dl> <dt>

*IpamSubnet* \[in\]
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

An array of [**MSFT\_IPAM\_Subnet**](msft-ipam-subnet.md) embedded instances.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the scope as an array of [**MSFT\_IPAM\_Subnet**](msft-ipam-subnet.md) embedded instances.

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

 

 




