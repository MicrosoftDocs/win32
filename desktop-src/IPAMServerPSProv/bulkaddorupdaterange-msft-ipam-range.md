---
Description: Adds or updates a set of IP address ranges in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b3ff21f0-0662-4871-afe6-24d016d533a9
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: BulkAddOrUpdateRange method of the MSFT\_IPAM\_Range class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BulkAddOrUpdateRange method of the MSFT\_IPAM\_Range class

Adds or updates a set of IP address ranges in IPAM.

## Syntax


```mof
uint32 BulkAddOrUpdateRange(
  [in]  MSFT_IPAM_Range           Range[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*Range* \[in\]
</dt> <dd>

An array that contains the IP address object to add.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the operational status for each add operation.

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

 

 




