---
Description: 'Exports a set of IP address ranges from IPAM to a CSV file.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'b4fdd9ed-c4e8-443a-b076-3167e3ae46df'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'ExportRange method of the MSFT\_IPAM\_Range class'
---

# ExportRange method of the MSFT\_IPAM\_Range class

Exports a set of IP address ranges from IPAM to a CSV file.

## Syntax


```mof
uint32 ExportRange(
  [in]  string          Path,
  [in]  uint16          AddressType,
  [in]  uint16          NetworkType,
  [in]  string          AddressSpace,
  [out] MSFT_IPAM_Range Output[]
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The literal path and filename of the CSV file.

</dd> <dt>

*AddressType* \[in\]
</dt> <dd>

Indicates the format of the IP addresses and masks within the range.

The possible values are:

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

IPv4

</dd> <dt>

2
</dt> <dd>

IPv6

</dd> </dl> </dd> <dt>

*NetworkType* \[in\]
</dt> <dd>

The network type of the address range.

The possible values are:

<dt>

1
</dt> <dd>

NonVirtualized

</dd> <dt>

2
</dt> <dd>

Provider

</dd> <dt>

3
</dt> <dd>

Customer

</dd> </dl> </dd> <dt>

*AddressSpace* \[in\]
</dt> <dd>

The name of the address space associated with the address range.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array of the exported address range objects.

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

[**MSFT\_IPAM\_Range**](msft-ipam-range.md)
</dt> </dl>

 

 




