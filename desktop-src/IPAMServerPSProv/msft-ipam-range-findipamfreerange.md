---
Description: 'Retrieves unassigned IP address ranges from IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '3CDA524B-05B6-4C41-AD66-E35445361481'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'FindIpamFreeRange method of the MSFT\_IPAM\_Range class'
---

# FindIpamFreeRange method of the MSFT\_IPAM\_Range class

Retrieves unassigned IP address ranges from IPAM.

## Syntax


```mof
uint32 FindIpamFreeRange(
  [in]  MSFT_IPAM_Subnet    Subnet,
  [in]  uint32              NumberOfAddresses,
  [in]  uint32              NumberofRanges,
  [out] MSFT_IPAM_FreeRange FreeIPRanges[]
);
```



## Parameters

<dl> <dt>

*Subnet* \[in\]
</dt> <dd>

The subnet that contains the ranges.

</dd> <dt>

*NumberOfAddresses* \[in\]
</dt> <dd>

The number of IP addresses to retrieve.

</dd> <dt>

*NumberofRanges* \[in\]
</dt> <dd>

The number of ranges to retrieve.

</dd> <dt>

*FreeIPRanges* \[out\]
</dt> <dd>

This method returns an array of embedded [**MSFT\_IPAM\_FreeRange**](msft-ipam-freerange.md) instances containing the retrieved ranges.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_Range**](msft-ipam-range.md)
</dt> </dl>

 

 




