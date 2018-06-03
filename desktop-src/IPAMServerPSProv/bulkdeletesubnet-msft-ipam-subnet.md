---
Description: Deletes a set of IP address objects from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dad2c88c-3e97-456b-beab-140a09821c15
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: BulkDeleteSubnet method of the MSFT\_IPAM\_Subnet class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BulkDeleteSubnet method of the MSFT\_IPAM\_Subnet class

Deletes a set of IP address objects from IPAM.

## Syntax


```mof
uint32 BulkDeleteSubnet(
  [in]  MSFT_IPAM_Subnet          Subnet[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*Subnet* \[in\]
</dt> <dd>

An array that contains the subnet objects to delete.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the operational status for each deleted subnet object.

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

 

 




