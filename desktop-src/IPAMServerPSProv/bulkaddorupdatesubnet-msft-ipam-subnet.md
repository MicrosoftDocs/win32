---
Description: Adds or updates a set of subnets in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c2c09c2-a910-4efb-ba30-b0963092c7e2
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: BulkAddOrUpdateSubnet method of the MSFT\_IPAM\_Subnet class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BulkAddOrUpdateSubnet method of the MSFT\_IPAM\_Subnet class

Adds or updates a set of subnets in IPAM.

## Syntax


```mof
uint32 BulkAddOrUpdateSubnet(
  [in]  MSFT_IPAM_Subnet          Subnet[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*Subnet* \[in\]
</dt> <dd>

An array that contains the subnet objects to add or update.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the operational status for each new and updated subnet object.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_Subnet**](msft-ipam-subnet.md)
</dt> </dl>

 

 




