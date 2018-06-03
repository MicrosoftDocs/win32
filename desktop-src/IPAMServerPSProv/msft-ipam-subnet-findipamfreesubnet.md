---
Description: Retrieves unassigned IP subnets from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1B893A84-6C50-4C61-8F10-F0A60E94E6B6
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: FindIpamFreeSubnet method of the MSFT\_IPAM\_Subnet class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FindIpamFreeSubnet method of the MSFT\_IPAM\_Subnet class

Retrieves unassigned IP subnets from IPAM.

## Syntax


```mof
uint32 FindIpamFreeSubnet(
  [in]  MSFT_IPAM_Block      Block,
  [in]  uint32               SubnetPrefix,
  [in]  uint32               NumberOfSubnets,
  [out] MSFT_IPAM_FreeSubnet FreeIPSubnets[]
);
```



## Parameters

<dl> <dt>

*Block* \[in\]
</dt> <dd>

The block that contains the subnets.

</dd> <dt>

*SubnetPrefix* \[in\]
</dt> <dd>

The prefix of the subnets to retrieve.

</dd> <dt>

*NumberOfSubnets* \[in\]
</dt> <dd>

The number of subnets to retrieve.

</dd> <dt>

*FreeIPSubnets* \[out\]
</dt> <dd>

When this method returns, this parameter contains an instance of [**MSFT\_IPAM\_FreeSubnet**](msft-ipam-freesubnet.md) that contains the retrieved subnets.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

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

[**MSFT\_IPAM\_Subnet**](msft-ipam-subnet.md)
</dt> </dl>

 

 




