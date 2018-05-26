---
Description: Represents and IP address block in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0daf03c8-1abd-421d-aa01-e7ecd00e83b9
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_Block class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_IPAM\_Block class

Represents and IP address block in IPAM.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Collections"), ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_Block : CIM_RangeOfIPAddresses
{
  string   Caption;
  string   Description;
  string   ElementName;
  string   StartAddress;
  string   EndAddress;
  uint16   AddressType;
  string   InstanceID;
  uint16   AddressCategory;
  string   Rir;
  string   NetworkId;
  datetime RirReceivedDate;
  datetime LastAssignedDate;
  datetime LastModifiedTime;
  string   Owner;
  uint16   Utilization;
  uint64   TotalAddresses;
  uint64   AssignedAddresses;
  uint64   UtilizedAddresses;
  real32   PercentageUtilized;
  real32   PercentageAssigned;
  string   AccessScopePath;
  boolean  IsInheritedAccessScope;
};
```

## Members

The **MSFT\_IPAM\_Block** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_IPAM\_Block** class has these methods.



| Method                                               | Description                                     |
|:-----------------------------------------------------|:------------------------------------------------|
| [**AddIpamBlock**](addipamblock-msft-ipam-block.md) | Adds a new IP address block to IPAM.<br/> |



 

### Properties

The **MSFT\_IPAM\_Block** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for this block.

**Windows Server 2012 R2:** This property is unavailable prior to Windows Server 2016.

</dd> <dt>

**AddressCategory**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the IP address block is public or private.

The possible values are.

<dt>

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

**AddressType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the format of the IP addresses and masks within the range.

This property is inherited from [**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md).

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

The number of IP addresses assigned to child ranges.

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

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **Description** property provides a textual description of the object.

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

**EndAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md).**AddressType**")
</dt> </dl>

The ending IP address of the address range.

This property is inherited from [**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (InstanceID), [**key**](https://msdn.microsoft.com/library/aa392157)
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

Whether the access scope for this block is inherited from parent.

**Windows Server 2012 R2:** This property is unavailable prior to Windows Server 2016.

</dd> <dt>

**LastAssignedDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date when the address block was assigned to the IPAM server.

</dd> <dt>

**LastModifiedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The latest date and time when any property of the address block was modified.

</dd> <dt>

**NetworkId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network address and prefix length of the address block. The value is formatted as: *NetworkId*/*Prefix*.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The owner of the address block.

</dd> <dt>

**PercentageAssigned**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of assigned IP addresses in the address block.

</dd> <dt>

**PercentageUtilized**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of used IP addresses in the address block.

</dd> <dt>

**Rir**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Regional Internet Registries (RIR) for public IP addresses.

> [!Note]  
> This property is required for a public address block.

 

The possible values are.

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

</dd> </dl>

</dd> <dt>

**RirReceivedDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date when a public address block was obtained from an RIR.

</dd> <dt>

**StartAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md).**AddressType**")
</dt> </dl>

The starting IP address of the address range.

This property is inherited from [**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md).

</dd> <dt>

**TotalAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of IP addresses in the address block.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the IP address utilization of the block, as a threshold.

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

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of used IP addresses in the address block.

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

[**CIM\_RangeOfIPAddresses**](cim-rangeofipaddresses.md)
</dt> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




