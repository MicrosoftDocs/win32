---
Description: Exports a set of IP addresses from IPAM to a CSV file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c20ea491-fdd4-4af8-8ce5-b19a358678d9
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: ExportAddress method of the MSFT\_IPAM\_Address class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExportAddress method of the MSFT\_IPAM\_Address class

Exports a set of IP addresses from IPAM to a CSV file.

## Syntax


```mof
uint32 ExportAddress(
  [in]  string            Path,
  [in]  uint16            AddressType = 1,
  [in]  uint16            NetworkType,
  [in]  string            AddressSpace,
  [out] MSFT_IPAM_Address Output[]
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The path and name of the CSV file.

</dd> <dt>

*AddressType* \[in\]
</dt> <dd>

The format of the IP addresses.

The possible values are:

<dt>

1
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

The address space of the IP addresses to export.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the exported IP addresses.

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

 

 




