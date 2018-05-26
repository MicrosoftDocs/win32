---
Description: Represents a subnet that contains IP protocol endpoints in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0f4fdeee-33f9-4495-b6a9-8d5037fce02c
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_Subnet class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_IPAM\_Subnet class

Represents a subnet that contains IP protocol endpoints in IPAM.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Collections"), ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_Subnet : CIM_IPConnectivitySubnet
{
  string   Caption;
  string   Description;
  string   ElementName;
  uint16   ConnectivityStatus;
  string   SubnetNumber;
  string   SubnetMask;
  uint8    PrefixLength;
  uint16   AddressType;
  string   InstanceID;
  string   Name;
  string   NetworkId;
  uint16   NetworkType;
  boolean  Overlapping;
  string   NetworkSite;
  string   VmmLogicalNetwork;
  string   AddressSpace;
  uint64   AddressSpaceId;
  string   ProviderAddressSpace;
  string   CustomerAddressSpace;
  string   Owner;
  datetime LastModifiedTime;
  real64   PercentageUtilized;
  real64   TotalAddresses;
  real64   AssignedAddresses;
  real64   UtilizedAddresses;
  uint16   Utilization;
  uint16   VlanId[];
  uint32   VirtualSubnetId;
  string   CustomConfiguration;
  string   AccessScopePath;
  boolean  IsInheritedAccessScope;
};
```

## Members

The **MSFT\_IPAM\_Subnet** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_IPAM\_Subnet** class has these methods.



| Method                                                                  | Description                                                                                                                                          |
|:------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddIpamSubnet**](addipamsubnet-msft-ipam-subnet.md)                 | Adds a new subnet object to IPAM.<br/>                                                                                                         |
| [**BulkAddOrUpdateSubnet**](bulkaddorupdatesubnet-msft-ipam-subnet.md) | Adds or updates a set of subnets in IPAM.<br/>                                                                                                 |
| [**BulkDeleteSubnet**](bulkdeletesubnet-msft-ipam-subnet.md)           | Deletes a set of IP address objects from IPAM.<br/>                                                                                            |
| [**ExportSubnet**](exportsubnet-msft-ipam-subnet.md)                   | Exports the subnets from IPAM server to a CSV file.<br/>                                                                                       |
| [**FindIpamFreeSubnet**](msft-ipam-subnet-findipamfreesubnet.md)       | Retrieves unassigned IP subnets from IPAM.<br/> **Windows Server 2012 R2:** This method is not available until Windows Server 2016.<br/> |
| [**ImportSubnet**](importsubnet-msft-ipam-subnet.md)                   | Imports subnets into IPAM from a CSV file.<br/>                                                                                                |



 

### Properties

The **MSFT\_IPAM\_Subnet** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for this subnet.

**Windows Server 2012 R2:** This property is unavailable prior to Windows Server 2016.

</dd> <dt>

**AddressSpace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address space of the subnet.

</dd> <dt>

**AddressSpaceId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the address space of the subnet.

</dd> <dt>

**AddressType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration that describes the format of the address properties in the subnet.

This property is inherited from [**CIM\_IPConnectivitySubnet**](cim-ipconnectivitysubnet.md).

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

**IPv4** (1)


</dt> <dd></dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

**IPv6** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**AssignedAddresses**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of IP addresses in the subnet, that map to an address range in IPAM.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ConnectivityStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration that describes the connectivity between the endpoints in the collection.

This property is inherited from [**CIM\_ConnectivityCollection**](cim-connectivitycollection.md).

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The system couldn't retrieve the state of the connection.

</dd> <dt>

<span id="Connectivity_Up"></span><span id="connectivity_up"></span><span id="CONNECTIVITY_UP"></span>

<span id="Connectivity_Up"></span><span id="connectivity_up"></span><span id="CONNECTIVITY_UP"></span>**Connectivity/Up** (2)


</dt> <dd>

The connection is up.

</dd> <dt>

<span id="No_Connectivity_Down"></span><span id="no_connectivity_down"></span><span id="NO_CONNECTIVITY_DOWN"></span>

<span id="No_Connectivity_Down"></span><span id="no_connectivity_down"></span><span id="NO_CONNECTIVITY_DOWN"></span>**No Connectivity/Down** (3)


</dt> <dd>

The connection is down.

</dd> <dt>

<span id="Partitioned"></span><span id="partitioned"></span><span id="PARTITIONED"></span>

<span id="Partitioned"></span><span id="partitioned"></span><span id="PARTITIONED"></span>**Partitioned** (4)


</dt> <dd>

The connection is partitioned.

</dd> </dl>

</dd> <dt>

**CustomConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A set of custom metadata associated with the subnet address. This is specified as a semi-colon separated  name=value  pairs.

> [!Note]  
> This property is formatted with semi-colon separated *name*=*value* pairs.

 

</dd> <dt>

**CustomerAddressSpace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The customer address space associated with the subnet.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

</dd> <dt>

**IsInheritedAccessScope**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the access scope for this subnet is inherited from parent.

**Windows Server 2012 R2:** This property is unavailable prior to Windows Server 2016.

</dd> <dt>

**LastModifiedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The latest date and time when a property of the subnet was modified.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user specified name of the subnet.

</dd> <dt>

**NetworkId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network ID of the subnet.

> [!Note]  
> The **NetworkID** property uses the format: *NetworkId* / *Prefix Length*.

 

</dd> <dt>

**NetworkSite**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of a network site in the physical network.

</dd> <dt>

**NetworkType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the IP address is a virtual address.

The possible values are.

<dt>

<span id="NonVirtualized"></span><span id="nonvirtualized"></span><span id="NONVIRTUALIZED"></span>

**NonVirtualized** (1)


</dt> <dd></dd> <dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>

**Provider** (2)


</dt> <dd></dd> <dt>

<span id="Customer"></span><span id="customer"></span><span id="CUSTOMER"></span>

**Customer** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Overlapping**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if this subnet overlaps with another subnet in IPAM; otherwise, **false**.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The owner of the subnet.

</dd> <dt>

**PercentageUtilized**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of IP addresses in the subnet that are in use.

</dd> <dt>

**PrefixLength**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The prefix length for IPv6 addresses in the subnet.

This property is inherited from [**CIM\_IPConnectivitySubnet**](cim-ipconnectivitysubnet.md).

</dd> <dt>

**ProviderAddressSpace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The provider address space associated with the subnet.

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The mask for the starting IPv4 address of the subnet.

This property is inherited from [**CIM\_IPConnectivitySubnet**](cim-ipconnectivitysubnet.md).

</dd> <dt>

**SubnetNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_IPConnectivitySubnet.AddressType")
</dt> </dl>

The IP address of the subnet.

This property is inherited from [**CIM\_IPConnectivitySubnet**](cim-ipconnectivitysubnet.md).

</dd> <dt>

**TotalAddresses**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of IP addresses in the subnet.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The usage level of the subnet.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Under"></span><span id="under"></span><span id="UNDER"></span>

**Under** (1)


</dt> <dd></dd> <dt>

<span id="Optimal"></span><span id="optimal"></span><span id="OPTIMAL"></span>

**Optimal** (2)


</dt> <dd></dd> <dt>

<span id="Over"></span><span id="over"></span><span id="OVER"></span>

**Over** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**UtilizedAddresses**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of IP addresses in the subnet that are in use.

</dd> <dt>

**VirtualSubnetId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The virtual subnet ID to use for network virtualization.

</dd> <dt>

**VlanId**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the IDs of VLANs that contain the subnet.

</dd> <dt>

**VmmLogicalNetwork**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of an abstraction of a physical network that describes a particular function in an environment. A logical network can contain multiple network sites.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | RootMicrosoftIPAM<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_IPConnectivitySubnet**](cim-ipconnectivitysubnet.md)
</dt> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




