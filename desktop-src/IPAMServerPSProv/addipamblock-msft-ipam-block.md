---
Description: Adds a new IP address block to IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 512614f8-20d9-450f-8cd2-ec0c31ea51c1
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AddIpamBlock method of the MSFT\_IPAM\_Block class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddIpamBlock method of the MSFT\_IPAM\_Block class

Adds a new IP address block to IPAM.

## Syntax


```mof
uint32 AddIpamBlock(
  [in]  string          NetworkId,
  [in]  string          StartAddress,
  [in]  string          EndAddress,
  [in]  string          Rir,
  [in]  datetime        RirReceivedDate,
  [in]  string          Description,
  [in]  datetime        LastAssignedDate,
  [in]  string          Owner,
  [out] MSFT_IPAM_Block output
);
```



## Parameters

<dl> <dt>

*NetworkId* \[in\]
</dt> <dd>

The network address and prefix length of the address block. The value is formatted as: *NetworkId*/*Prefix*.

</dd> <dt>

*StartAddress* \[in\]
</dt> <dd>

The starting IP address of the address block.

</dd> <dt>

*EndAddress* \[in\]
</dt> <dd>

The ending IP address of the address block.

</dd> <dt>

*Rir* \[in\]
</dt> <dd>

The Regional Internet Registries (RIR) for public IP addresses.

> [!Note]  
> This property is required for a public address block.

 

The possible values are:

<dt>

AFRINIC
</dt> <dd>

African Network Information Centre (AfriNIC)

</dd> <dt>

APNIC
</dt> <dd>

Asia-Pacific Network Information Centre (APNIC)

</dd> <dt>

ARIN
</dt> <dd>

American Registry for Internet Numbers (ARIN)

</dd> <dt>

LACNIC
</dt> <dd>

Latin America and Caribbean Network Information Centre (LACNIC)

</dd> <dt>

RIPE
</dt> <dd>

R seaux IP Europ ens Network Coordination Centre (RIPE NCC)

</dd> </dl> </dd> <dt>

*RirReceivedDate* \[in\]
</dt> <dd>

The data and time when the public address block was obtained from the RIR.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A description of the address block.

</dd> <dt>

*LastAssignedDate* \[in\]
</dt> <dd>

The last date and time when the block was assigned to a device on a network.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

The owner of the address block.

</dd> <dt>

*output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the added address block object.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

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

[**MSFT\_IPAM\_Block**](msft-ipam-block.md)
</dt> </dl>

 

 




