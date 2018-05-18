---
Description: 'Adds a subnet to IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '05e4c244-a79e-4c97-a81b-7ebe540b99ec'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'AddIpamSubnet method of the MSFT\_IPAM\_Subnet class'
---

# AddIpamSubnet method of the MSFT\_IPAM\_Subnet class

Adds a subnet to IPAM.

## Syntax


```mof
uint32 AddIpamSubnet(
  [in]  string           Name,
  [in]  string           NetworkId,
  [in]  uint16           NetworkType,
  [in]  string           AddressSpace,
  [in]  string           Owner,
  [in]  string           Description,
  [in]  uint16           VlanId[],
  [in]  string           CustomConfiguration,
  [in]  string           VmmLogicalNetwork,
  [in]  string           NetworkSite,
  [in]  uint32           VirtualSubnetId,
  [out] MSFT_IPAM_Subnet output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The user specified name of the subnet.

</dd> <dt>

*NetworkId* \[in\]
</dt> <dd>

The network ID of the subnet.

> [!Note]  
> The **NetworkID** property uses the format: *NetworkId* / *Prefix Length*.

 

</dd> <dt>

*NetworkType* \[in\]
</dt> <dd>

Indicates whether the IP address is a virtual address.

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

The address space of the subnet.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

The owner of the subnet.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The Description property provides a textual description of the object.

</dd> <dt>

*VlanId* \[in\]
</dt> <dd>

An array that contains the IDs of VLANs that contain the subnet.

</dd> <dt>

*CustomConfiguration* \[in\]
</dt> <dd>

A set of custom metadata associated with the subnet address. This is specified as a semi-colon separated ‘name=value’ pairs.

> [!Note]  
> This property is formatted with semi-colon separated *name*=*value* pairs.

 

</dd> <dt>

*VmmLogicalNetwork* \[in\]
</dt> <dd>

The name of an abstraction of a physical network that describes a particular function in an environment. A logical network can contain multiple network sites.

</dd> <dt>

*NetworkSite* \[in\]
</dt> <dd>

The name of a network site in the physical network.

</dd> <dt>

*VirtualSubnetId* \[in\]
</dt> <dd>

The virtual subnet ID to use for network virtualization.

</dd> <dt>

*output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the new subnet object.

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

 

 




