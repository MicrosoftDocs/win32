---
Description: Adds or updates a set of IP addresses in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 453d2252-adbc-4d85-8b60-091e5cf6c5ad
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: BulkAddOrUpdateAddress method of the MSFT\_IPAM\_Address class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BulkAddOrUpdateAddress method of the MSFT\_IPAM\_Address class

Adds or updates a set of IP addresses in IPAM.

## Syntax


```mof
uint32 BulkAddOrUpdateAddress(
  [in]  MSFT_IPAM_Address         Address[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

The array of IP addresses to add or update.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the status of each add or update operation.

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

[**MSFT\_IPAM\_Address**](msft-ipam-address.md)
</dt> </dl>

 

 




