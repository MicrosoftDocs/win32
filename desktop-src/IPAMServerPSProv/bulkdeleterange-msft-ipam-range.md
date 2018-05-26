---
Description: Deletes a set of IP address range from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa8eaba6-5a4e-4871-b794-ddda544f3ee3
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: BulkDeleteRange method of the MSFT\_IPAM\_Range class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BulkDeleteRange method of the MSFT\_IPAM\_Range class

Deletes a set of IP address range from IPAM.

## Syntax


```mof
uint32 BulkDeleteRange(
  [in]  MSFT_IPAM_Range           Range[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*Range* \[in\]
</dt> <dd>

An array that contains the IP address object to delete.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the operational status for each delete operation.

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

[**MSFT\_IPAM\_Range**](msft-ipam-range.md)
</dt> </dl>

 

 




