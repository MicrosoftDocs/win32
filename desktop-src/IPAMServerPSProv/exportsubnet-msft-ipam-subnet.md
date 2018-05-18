---
Description: 'Exports the subnets from IPAM server to a CSV file.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '6e759790-3ce3-4e67-898c-a7563cc0fcb1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'ExportSubnet method of the MSFT\_IPAM\_Subnet class'
---

# ExportSubnet method of the MSFT\_IPAM\_Subnet class

Exports the subnets from IPAM server to a CSV file.

## Syntax


```mof
uint32 ExportSubnet(
  [in]  string           Path,
  [in]  uint16           AddressType,
  [in]  uint16           NetworkType,
  [in]  string           AddressSpace,
  [out] MSFT_IPAM_Subnet Output[]
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The path and name of the CSV file to import.

</dd> <dt>

*AddressType* \[in\]
</dt> <dd>

The format of the export IP address properties.

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

Indicates whether the subnet IP addresses are virtual addresses.

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

4
</dt> <dd>

Customer

</dd> </dl> </dd> <dt>

*AddressSpace* \[in\]
</dt> <dd>

The address space of the subnets.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array of exported subnet objects.

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

[**MSFT\_IPAM\_Subnet**](msft-ipam-subnet.md)
</dt> </dl>

 

 




