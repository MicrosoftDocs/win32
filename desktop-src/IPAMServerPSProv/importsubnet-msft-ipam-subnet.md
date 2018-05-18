---
Description: 'Imports subnets into IPAM from a CSV file.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '736c447d-5b0f-40c0-a600-4acc3ea83eba'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'ImportSubnet method of the MSFT\_IPAM\_Subnet class'
---

# ImportSubnet method of the MSFT\_IPAM\_Subnet class

Imports subnets into IPAM from a CSV file.

## Syntax


```mof
uint32 ImportSubnet(
  [in]  string Path,
  [in]  string ErrorPath,
  [in]  uint16 AddressFamily,
  [out] string Output
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The path and name of the CSV file to import.

</dd> <dt>

*ErrorPath* \[in\]
</dt> <dd>

The path to the error files that IPAM generates if IPAM fails to import one or more IP addresses.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

The address family of the IP address records in the CSV file.

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

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the status of the import operation.

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

 

 




