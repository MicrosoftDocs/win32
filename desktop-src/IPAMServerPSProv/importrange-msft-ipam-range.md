---
Description: Imports a set of IP address ranges into IPAM from a CSV file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 19441620-1f4b-46da-98ce-a7dd9ba2c33c
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: ImportRange method of the MSFT\_IPAM\_Range class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ImportRange method of the MSFT\_IPAM\_Range class

Imports a set of IP address ranges into IPAM from a CSV file.

## Syntax


```mof
uint32 ImportRange(
  [in]  string  Path,
  [in]  string  ErrorPath,
  [in]  uint16  AddressFamily,
  [in]  string  ManagedByService,
  [in]  string  ServiceInstance,
  [in]  boolean AddManagedByService,
  [in]  boolean AddServiceInstance,
  [in]  boolean DeleteMappedAddresses,
  [in]  boolean CreateSubnetIfNotFound,
  [out] string  Output
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The literal path and filename of the CSV file.

</dd> <dt>

*ErrorPath* \[in\]
</dt> <dd>

The path of the error files that IPAM generates if one or more IP address ranges fails to import.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

The address family of the IP addresses in the import file.

The possible values are:

<dt>

0
</dt> <dd>

Other

</dd> <dt>

1
</dt> <dd>

IPv4

</dd> <dt>

2
</dt> <dd>

IPv6

</dd> </dl> </dd> <dt>

*ManagedByService* \[in\]
</dt> <dd>

The name of the service that manages the address ranges to import.

> [!Note]  
> The import of MS DHCP ranges is not supported by IPAM.

 

</dd> <dt>

*ServiceInstance* \[in\]
</dt> <dd>

An array of service instances that manage the address ranges to import.

</dd> <dt>

*AddManagedByService* \[in\]
</dt> <dd>

**True** to manage the imported address ranges with the service that manage the address ranges in the CSV file; otherwise, **false**.

</dd> <dt>

*AddServiceInstance* \[in\]
</dt> <dd>

**True** to manage the imported address ranges with the service instance that manage the address ranges in the CSV file; otherwise, **false**.

</dd> <dt>

*DeleteMappedAddresses* \[in\]
</dt> <dd>

**True** delete mapped IP addresses from the imported address ranges; otherwise, **false**.

</dd> <dt>

*CreateSubnetIfNotFound* \[in\]
</dt> <dd>

**True** to create a parent subnet for the imported address ranges when no parent subnet exists; otherwise, **false**.

</dd> <dt>

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_Range**](msft-ipam-range.md)
</dt> </dl>

 

 




