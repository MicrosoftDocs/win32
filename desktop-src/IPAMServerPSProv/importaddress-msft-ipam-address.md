---
Description: Imports a set of IP addresses from a CSV file to IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8e80c4d8-f3f3-4e61-a679-c3b536804d3a
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: ImportAddress method of the MSFT\_IPAM\_Address class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ImportAddress method of the MSFT\_IPAM\_Address class

Imports a set of IP addresses from a CSV file to IPAM.

## Syntax


```mof
uint32 ImportAddress(
  [in]  string Path,
  [in]  string ErrorPath,
  [in]  uint16 AddressFamily = 1,
  [in]  string ManagedByService,
  [in]  string ServiceInstance,
  [in]  string NetworkID,
  [in]  string StartAddress,
  [in]  string EndAddress,
  [in]  uint16 NetworkType,
  [in]  string AddressSpace,
  [out] string Output
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

The path of the error files that IPAM generates if one or more IP address records fail to import.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

The address family of the IP address records in the import file.

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

The name of the service that manages the IP addresses to import.

</dd> <dt>

*ServiceInstance* \[in\]
</dt> <dd>

The name of the service instance that manages the IP addresses to import.

</dd> <dt>

*NetworkID* \[in\]
</dt> <dd>

The network address and prefix length of the IP addresses to import.

</dd> <dt>

*StartAddress* \[in\]
</dt> <dd>

The starting IP address of the IP address range that contains the IP addresses to import.

</dd> <dt>

*EndAddress* \[in\]
</dt> <dd>

The ending IP address of the IP address range that contains the IP addresses to import.

</dd> <dt>

*NetworkType* \[in\]
</dt> <dd>

Indicates whether the IP addresses are virtual addresses.

The possible values are:

<dt>

<span id="NonVirtualized"></span><span id="nonvirtualized"></span><span id="NONVIRTUALIZED"></span>

**NonVirtualized** (1)


</dt> <dd></dd> <dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>

**Provider** (2)


</dt> <dd></dd> <dt>

<span id="Customer"></span><span id="customer"></span><span id="CUSTOMER"></span>

**Customer** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*AddressSpace* \[in\]
</dt> <dd>

The address space of the IP addresses to import.

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

[**MSFT\_IPAM\_Address**](msft-ipam-address.md)
</dt> </dl>

 

 




