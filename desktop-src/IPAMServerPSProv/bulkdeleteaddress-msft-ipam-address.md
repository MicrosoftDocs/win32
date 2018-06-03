---
Description: Deletes a set of IP addresses from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cf78d381-46b2-4a59-a7ab-0e65857c7870
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: BulkDeleteAddress method of the MSFT\_IPAM\_Address class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BulkDeleteAddress method of the MSFT\_IPAM\_Address class

Deletes a set of IP addresses from IPAM.

## Syntax


```mof
uint32 BulkDeleteAddress(
  [in]  MSFT_IPAM_Address         Address[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

An that contains the IP addresses to delete.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the status of each delete operation.

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

 

 




