---
title: MSCluster\_Network class
description: A dynamic WMI class that represents cluster networks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0467bd96-9bc5-4167-a1f4-6b8b8b5de99c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_Network class", "MSCluster_Network class, described"]
topic_type:
- apiref
api_name:
- MSCluster_Network
- MSCluster_Network.Caption
- MSCluster_Network.InstallDate
- MSCluster_Network.Status
- MSCluster_Network.Flags
- MSCluster_Network.Characteristics
- MSCluster_Network.Name
- MSCluster_Network.ID
- MSCluster_Network.Description
- MSCluster_Network.Address
- MSCluster_Network.AddressMask
- MSCluster_Network.Role
- MSCluster_Network.State
- MSCluster_Network.IPv6Addresses
- MSCluster_Network.IPv6PrefixLengths
- MSCluster_Network.IPv4Addresses
- MSCluster_Network.IPv4PrefixLengths
- MSCluster_Network.Metric
- MSCluster_Network.AutoMetric
- MSCluster_Network.PrivateProperties
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_Network class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents cluster [networks](https://msdn.microsoft.com/library/aa371501).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{F541DA2A-174C-4000-9066-B755095C7E7A}"), AMENDMENT]
class MSCluster_Network : MSCluster_LogicalElement
{
  string             Caption;
  datetime           InstallDate;
  string             Status;
  uint32             Flags;
  uint32             Characteristics;
  string             Name;
  string             ID;
  string             Description;
  string             Address;
  string             AddressMask;
  uint32             Role;
  uint32             State;
  string             IPv6Addresses[];
  string             IPv6PrefixLengths[];
  string             IPv4Addresses[];
  string             IPv4PrefixLengths[];
  uint32             Metric;
  boolean            AutoMetric;
  MSCluster_Property PrivateProperties;
};
```

## Members

The **MSCluster\_Network** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_Network** class has these methods.



| Method                                                                   | Description                                        |
|:-------------------------------------------------------------------------|:---------------------------------------------------|
| [**ExecuteNetworkControl**](mscluster-network-executenetworkcontrol.md) | Executes a control code on the network.<br/> |
| [**Rename**](mscluster-network-rename.md)                               | Renames the network<br/>                     |



 

### Properties

The **MSCluster\_Network** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the address for the entire network or subnet.

</dd> <dt>

**AddressMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the mask that distinguishes the network and host portions of an address.

</dd> <dt>

**AutoMetric**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines whether the metric is to be set by the user or determined automatically.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the network.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the network. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Description)
</dt> </dl>

Provides comments about the network.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the flags set for the network. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Id of the network.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the network was installed. A lack of a value does not indicate that the network is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**IPv4Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the IPv4 addresses currently assigned to this network.

</dd> <dt>

**IPv4PrefixLengths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the prefix lengths of the IPv4 addresses currently assigned to this network.

</dd> <dt>

**IPv6Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the IPv6 addresses currently assigned to this network.

</dd> <dt>

**IPv6PrefixLengths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the prefix lengths of the IPv6 addresses currently assigned to this network.

</dd> <dt>

**Metric**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The metric of a cluster network (networks with lower values are used first). If this value is set, then the **AutoMetric** property is set to **false**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Name), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Provides the name of the network.

</dd> <dt>

**PrivateProperties**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Property**](mscluster-property.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides private properties of the network.

</dd> <dt>

**Role**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the network's [**Role**](https://msdn.microsoft.com/library/aa371516) property.

The [**Role**](https://msdn.microsoft.com/library/aa371516) property describes the role of the network in the cluster. The following are the possible values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

The network is not used by the cluster.

</dd> <dt>

<span id="Cluster"></span><span id="cluster"></span><span id="CLUSTER"></span>

<span id="Cluster"></span><span id="cluster"></span><span id="CLUSTER"></span>**Cluster** (1)


</dt> <dd>

The network is used to carry internal cluster communication.

</dd> <dt>

<span id="Client"></span><span id="client"></span><span id="CLIENT"></span>

<span id="Client"></span><span id="client"></span><span id="CLIENT"></span>**Client** (2)


</dt> <dd>

Not supported.

</dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (3)


</dt> <dd>

The network is used to connect client systems and to carry internal cluster communication.

</dd> </dl>

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the current state of the network. For a listing of state descriptors, see the [**GetClusterNetworkState**](https://msdn.microsoft.com/library/aa369619) function or the [**CLUSTER\_NETWORK\_STATE**](https://msdn.microsoft.com/library/bb309155) enumeration.

The following are the possible values.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (-1)


</dt> <dd>

The operation was not successful.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **StateUnknown** before Windows Server 2012 R2 .

</dd> <dt>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>**Unavailable** (0)


</dt> <dd>

All of the network interfaces on the network are unavailable, which means that the nodes that own the network interfaces are down.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **StateUnavailable** before Windows Server 2012 R2 .

</dd> <dt>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>**Down** (1)


</dt> <dd>

The network is not operational; none of the [nodes](https://msdn.microsoft.com/library/aa371745) on the network can communicate.

</dd> <dt>

<span id="Paritioned"></span><span id="paritioned"></span><span id="PARITIONED"></span>

<span id="Paritioned"></span><span id="paritioned"></span><span id="PARITIONED"></span>**Paritioned** (2)


</dt> <dd>

The network is operational, but two or more nodes on the network cannot communicate. Typically a path-specific problem has occurred.

> [!Note]  
> This value is **Paritioned**, and not **Partitioned.**

 

</dd> <dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>

<span id="Up"></span><span id="up"></span><span id="UP"></span>**Up** (3)


</dt> <dd>

The network is operational; all of the nodes in the cluster can communicate.

</dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the network.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **MSCluster\_Network** class is derived from the [**MSCluster\_LogicalElement**](mscluster-logicalelement.md) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_LogicalElement**](mscluster-logicalelement.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





