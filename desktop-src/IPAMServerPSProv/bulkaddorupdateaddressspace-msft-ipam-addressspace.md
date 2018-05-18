---
Description: 'Adds or updates a set of address spaces in IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'f59df028-0115-4d76-8aee-885068215541'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'BulkAddOrUpdateAddressSpace method of the MSFT\_IPAM\_AddressSpace class'
---

# BulkAddOrUpdateAddressSpace method of the MSFT\_IPAM\_AddressSpace class

Adds or updates a set of address spaces in IPAM.

## Syntax


```mof
uint32 BulkAddOrUpdateAddressSpace(
  [in]  MSFT_IPAM_AddressSpace    AddressSpace[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*AddressSpace* \[in\]
</dt> <dd>

An array that contains the address space objects to add.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array of that contains the status for each add operation.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_AddressSpace**](msft-ipam-addressspace.md)
</dt> </dl>

 

 




