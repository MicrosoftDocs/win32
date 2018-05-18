---
Description: 'Represents a subnet that contains IP protocol endpoints.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '9e45250e-2486-4791-8d61-53f3c46edba3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'CIM\_IPConnectivitySubnet class'
---

# CIM\_IPConnectivitySubnet class

Represents a subnet that contains IP protocol endpoints.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Collections"), Version("2.7.0"), AMENDMENT]
class CIM_IPConnectivitySubnet : CIM_ConnectivityCollection
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  uint16 ConnectivityStatus;
  string SubnetNumber;
  string SubnetMask;
  uint8  PrefixLength;
  uint16 AddressType;
};
```

## Members

The **CIM\_IPConnectivitySubnet** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_IPConnectivitySubnet** class has these properties.

<dl> <dt>

**AddressType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration that describes the format of the address properties in the subnet.

The possible values are:

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

The possible values are:

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

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following \\'preferred\\' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon \\':\\', and where &lt;OrgID&gt; must include a unique name. It can be a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID. Or, it could be a registered ID that is assigned to the business entity by a recognized global authority.(This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; must not contain a colon (\\':\\'). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be re-used to identify different underlying (real-world) elements. If the above \\'preferred\\' algorithm is not used, the defining entity must ensure that the resulting InstanceID is not re-used as any of InstanceIDs produced by this or other providers for the NameSpace of this instance.

For DMTF-defined instances, the \\'preferred\\' algorithm must be used with the &lt;OrgID&gt; set to \\'CIM\\'.

This property is inherited from [**CIM\_SystemSpecificCollection**](cim-systemspecificcollection.md).

</dd> <dt>

**PrefixLength**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The prefix length for IPv6 addresses in the subnet.

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The mask for the starting IPv4 address of the subnet.

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

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




