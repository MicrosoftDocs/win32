---
Description: 'Adds a new IP address range to IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e1695eb2-0cff-457f-867c-e63b9b978b76'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'AddRange method of the MSFT\_IPAM\_Range class'
---

# AddRange method of the MSFT\_IPAM\_Range class

Adds a new IP address range to IPAM.

## Syntax


```mof
uint32 AddRange(
  [in]  string          NetworkID,
  [in]  uint16          NetworkType,
  [in]  string          AddressSpace,
  [in]  string          StartAddress,
  [in]  string          EndAddress,
  [in]  string          ManagedByService,
  [in]  string          ServiceInstance,
  [in]  uint16          UtilizationCalculation,
  [in]  real64          UtilizedAddresses,
  [in]  string          Description,
  [in]  string          Owner,
  [in]  uint16          AssignmentType,
  [in]  datetime        AssignmentDate,
  [in]  string          ReservedIPAddresses[],
  [in]  string          DnsServers[],
  [in]  string          DnsSuffixes[],
  [in]  string          ConnectionSpecificDnsSuffix,
  [in]  string          WinsServers[],
  [in]  string          VIP[],
  [in]  string          Gateway[],
  [in]  string          CustomConfiguration,
  [in]  string          AssociatedReverseLookupZone,
  [out] MSFT_IPAM_Range OutputRange
);
```



## Parameters

<dl> <dt>

*NetworkID* \[in\]
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

*StartAddress* \[in\]
</dt> <dd>

The starting IP address of the address range.

</dd> <dt>

*EndAddress* \[in\]
</dt> <dd>

The ending IP address of the address range.

</dd> <dt>

*ManagedByService* \[in\]
</dt> <dd>

The service that manages the address range.

</dd> <dt>

*ServiceInstance* \[in\]
</dt> <dd>

The instance of Managed By Service that manages the address range.

</dd> <dt>

*UtilizationCalculation* \[in\]
</dt> <dd>

Indicates whether the utilization thresholds are set by the user.

The possible values are:

<dt>

1
</dt> <dd>

Auto

</dd> <dt>

2
</dt> <dd>

Static

</dd> </dl> </dd> <dt>

*UtilizedAddresses* \[in\]
</dt> <dd>

The number of used IP addresses in the address range.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The description of the address range.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

The owner of the address range.

</dd> <dt>

*AssignmentType* \[in\]
</dt> <dd>

The format of the IP address assignment.

The possible values are:

<dt>

0
</dt> <dd>

None

</dd> <dt>

1
</dt> <dd>

Static

</dd> <dt>

2
</dt> <dd>

Dynamic

</dd> <dt>

3
</dt> <dd>

Auto

</dd> <dt>

4
</dt> <dd>

VIP

</dd> <dt>

5
</dt> <dd>

Reserved

</dd> </dl> </dd> <dt>

*AssignmentDate* \[in\]
</dt> <dd>

The date when addresses were assigned to the address range.

</dd> <dt>

*ReservedIPAddresses* \[in\]
</dt> <dd>

An array that contains the reserved IP addresses in the address range.

> [!Note]  
> These IP addresses are excluded from queries, when searching for free IP addresses.

 

</dd> <dt>

*DnsServers* \[in\]
</dt> <dd>

An array that contains the names of the DNS servers that are associated with the address range.

</dd> <dt>

*DnsSuffixes* \[in\]
</dt> <dd>

An array that contains the DNS search suffixes that are associated with the address range. These search suffixes are used to resolve a DNS query.

</dd> <dt>

*ConnectionSpecificDnsSuffix* \[in\]
</dt> <dd>

The Connection specific DNS suffix that is associated with the address range.

</dd> <dt>

*WinsServers* \[in\]
</dt> <dd>

An array that contains the WINS servers associated with the address range.

</dd> <dt>

*VIP* \[in\]
</dt> <dd>

An array that contains the virtual IP addresses in the address range.

> [!Note]  
> These IP addresses are excluded from queries, when searching for free IP addresses.

 

</dd> <dt>

*Gateway* \[in\]
</dt> <dd>

An array that contains the names of gateway servers and corresponding metrics associated with the address range.

</dd> <dt>

*CustomConfiguration* \[in\]
</dt> <dd>

The custom data associated with the address range. This is formatted as semi-colon separated *name*=*value* pairs.

</dd> <dt>

*AssociatedReverseLookupZone* \[in\]
</dt> <dd>

The associated reverse lookup zone name for this range.

**Windows Server 2012 R2:** This parameter not supported before Windows Server 2016.

</dd> <dt>

*OutputRange* \[out\]
</dt> <dd>

When this method returns, this parameter contains the new address range object.

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

 

 




