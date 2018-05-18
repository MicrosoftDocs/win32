---
Description: 'Represents an IP address range in IPAM. An IP address range contains the IP addresses that are between the start and end address of the range.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '0b58acca-5452-4506-a8a1-4c9ae3558304'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_IPAM\_Range class'
---

# MSFT\_IPAM\_Range class

Represents an IP address range in IPAM. An IP address range contains the IP addresses that are between the start and end address of the range.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Collections"), ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_Range : CIM_RangeOfIPAddresses
{
  string   Caption;
  string   Description;
  string   ElementName;
  string   StartAddress;
  string   EndAddress;
  uint16   AddressType;
  string   InstanceID;
  uint16   NetworkType;
  uint16   AddressCategory;
  boolean  Overlapping;
  string   NetworkID;
  string   ManagedByService;
  string   ServiceInstance;
  string   AddressSpace;
  uint64   AddressSpaceId;
  string   ProviderAddressSpace;
  string   CustomerAddressSpace;
  string   Owner;
  real64   PercentageUtilized;
  string   SubnetMask;
  uint16   AssignmentType;
  datetime AssignmentDate;
  datetime LastModifiedTime;
  string   NetworkSite;
  string   VmmLogicalNetwork;
  string   DhcpServerName;
  string   DhcpScopeName;
  uint16   Utilization;
  uint16   UtilizationCalculation;
  real64   UtilizedAddresses;
  uint64   AssignedAddresses;
  string   ExclusionRanges[];
  datetime LastReclaimRunTime;
  string   DnsServers[];
  string   WinsServers[];
  string   VIP[];
  string   ReservedIPAddresses[];
  string   DnsSuffixes[];
  string   ConnectionSpecificDnsSuffix;
  string   CustomConfiguration;
  string   AssociatedReverseLookupZone;
  string   AccessScopePath;
  boolean  IsInheritedAccessScope;
  string   Gateway[];
};
```

## Members

The **MSFT\_IPAM\_Range** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_IPAM\_Range** class has these methods.



| Method                                                               | Description                                                                                                                                                 |
|:---------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddRange**](addrange-msft-ipam-range.md)                         | Adds a new IP address range to IPAM.<br/>                                                                                                             |
| [**BulkAddOrUpdateRange**](bulkaddorupdaterange-msft-ipam-range.md) | Adds or updates a set of IP address ranges in IPAM.<br/>                                                                                              |
| [**BulkDeleteRange**](bulkdeleterange-msft-ipam-range.md)           | Deletes a set of IP address range from IPAM.<br/>                                                                                                     |
| [**ExportRange**](exportrange-msft-ipam-range.md)                   | Exports a set of IP address ranges from IPAM to a CSV file.<br/>                                                                                      |
| [**FindIpamFreeRange**](msft-ipam-range-findipamfreerange.md)       | Retrieves unassigned IP address ranges from IPAM.<br/> **Windows Server 2012 R2:** This method is not available until Windows Server 2016.<br/> |
| [**ImportRange**](importrange-msft-ipam-range.md)                   | Imports a set of IP address ranges into IPAM from a CSV file.<br/>                                                                                    |



 

### Properties

The **MSFT\_IPAM\_Range** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for this range.

**Windows Server 2012 R2:** This property is unavailable prior to Windows Server 2016.

</dd> <dt>

**AddressCategory**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The privacy scope of address range, such as public or private.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Public"></span><span id="public"></span><span id="PUBLIC"></span>

**Public** (1)


</dt> <dd></dd> <dt>

<span id="Private"></span><span id="private"></span><span id="PRIVATE"></span>

**Private** (2)


</dt> <dd></dd> <dt>

<span id="Global"></span><span id="global"></span><span id="GLOBAL"></span>

**Global** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**AddressSpace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the address space associated with the address range.

</dd> <dt>

**AddressSpaceId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the address space associated with the address range.

</dd> <dt>

**AddressType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("AddressType")
</dt> </dl>

An enumeration that defines how the address and mask properties are formatted.

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

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of IP addresses in the address range.

</dd> <dt>

**AssignmentDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date when addresses were assigned to the address range.

</dd> <dt>

**AssignmentType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The format of the IP address assignment.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>

**Static** (1)


</dt> <dd></dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (2)


</dt> <dd></dd> <dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>

**Auto** (3)


</dt> <dd></dd> <dt>

<span id="VIP"></span><span id="vip"></span>

**VIP** (4)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**AssociatedReverseLookupZone**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The associated reverse lookup zone name for this range.

**Windows Server 2012 R2:** This parameter not supported before Windows Server 2016.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The **Caption** property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ConnectionSpecificDnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Connection specific DNS suffix that is associated with the address range.

</dd> <dt>

**CustomConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The custom data associated with the address range. This is formatted as semi-colon separated *name*=*value* pairs.

</dd> <dt>

**CustomerAddressSpace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The customer address space that contains the address range.

> [!Note]  
> This property is only populated when the **NetworkType** property is set to "3" (Customer).

 

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **Description** property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DhcpScopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the DHCP scope that is synchronized with the range.

</dd> <dt>

**DhcpServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the DHCP server that is synchronized with the range.

</dd> <dt>

**DnsServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the names of the DNS servers that are associated with the address range.

</dd> <dt>

**DnsSuffixes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the DNS search suffixes that are associated with the address range. These search suffixes are used to resolve a DNS query.

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

**EndAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RangeOfIPAddresses.AddressType")
</dt> </dl>

The ending IP address of the address range.

This property is inherited from [**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md).

</dd> <dt>

**ExclusionRanges**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the exclusion ranges of the DHCP scope that is synchronized with the address range.

</dd> <dt>

**Gateway**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the names of gateway servers and corresponding metrics associated with the address range.

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

Whether the access scope for this range is inherited from parent.

**Windows Server 2012 R2:** This property is unavailable prior to Windows Server 2016.

</dd> <dt>

**LastModifiedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last date and time when any property of the address was modified.

</dd> <dt>

**LastReclaimRunTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time IP addresses were reclaimed from the address range.

</dd> <dt>

**ManagedByService**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The service that manages the address range.

</dd> <dt>

**NetworkID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network address and prefix length of the address range. This property is formatted as *NetworkId* / *Prefix Length*.

</dd> <dt>

**NetworkSite**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field, along with a logical network, forms an abstraction of the physical network. A given logical network can contain many network sites. This property is inherited from the subnet to which this range maps.

</dd> <dt>

**NetworkType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network type of the address range.

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

**True** if the range overlaps with another range in IPAM; otherwise, **false**.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The owner of this address IP range.

</dd> <dt>

**PercentageUtilized**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of used IP addresses in the address range.

</dd> <dt>

**ProviderAddressSpace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The provider address space that contains the address range.

> [!Note]  
> This property is only populated when the **NetworkType** property is set to "2" (Provider).

 

</dd> <dt>

**ReservedIPAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the reserved IP addresses in the address range.

> [!Note]  
> These IP addresses are excluded from queries, when searching for free IP addresses.

 

</dd> <dt>

**ServiceInstance**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The instance of Managed By Service that manages the address range.

</dd> <dt>

**StartAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RangeOfIPAddresses.AddressType")
</dt> </dl>

The starting IP address of the address range.

This property is inherited from [**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md).

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The subnet mask associated with the address range.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the IP address utilization of the range, as a threshold.

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

**UtilizationCalculation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the utilization thresholds are set by the user.

The possible values are.

<dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>

**Auto** (1)


</dt> <dd></dd> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>

**Static** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**UtilizedAddresses**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of used IP addresses in the address range.

</dd> <dt>

**VIP**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the virtual IP addresses in the address range.

> [!Note]  
> These IP addresses are excluded from queries, when searching for free IP addresses.

 

</dd> <dt>

**VmmLogicalNetwork**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An network abstraction defined for your environment. This property is inherited from the subnet to which this range maps.

</dd> <dt>

**WinsServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the WINS servers associated with the address range.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | RootMicrosoftIPAM<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md)
</dt> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




