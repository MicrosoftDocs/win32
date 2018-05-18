---
title: CIM\_Cluster class
description: A class derived from CIM\_ComputerSystem that 'is made up of' two or more computer systems which operate together as an atomic, functional whole to increase the performance, resources and/or RAS (Reliability, Availability and Serviceability) of the component computer systems, related to some aspects of these computer systems.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '10191d43-0c39-43a5-9fcd-4c538ee6eb44'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_Cluster class", "CIM_Cluster class, described"]
topic_type:
- apiref
api_name:
- CIM_Cluster
- CIM_Cluster.Caption
- CIM_Cluster.Description
- CIM_Cluster.InstallDate
- CIM_Cluster.Status
- CIM_Cluster.CreationClassName
- CIM_Cluster.Name
- CIM_Cluster.PrimaryOwnerContact
- CIM_Cluster.PrimaryOwnerName
- CIM_Cluster.Roles
- CIM_Cluster.NameFormat
- CIM_Cluster.Interconnect
- CIM_Cluster.InterconnectAddress
- CIM_Cluster.Types
- CIM_Cluster.MaxNumberOfNodes
- CIM_Cluster.ClusterState
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# CIM\_Cluster class

A class derived from [**CIM\_ComputerSystem**](cim-computersystem.md) that 'is made up of' two or more computer systems which operate together as an atomic, functional whole to increase the performance, resources and/or RAS (Reliability, Availability and Serviceability) of the component computer systems, related to some aspects of these computer systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class CIM_Cluster : CIM_ComputerSystem
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Status;
  string   CreationClassName;
  string   Name;
  string   PrimaryOwnerContact;
  string   PrimaryOwnerName;
  string   Roles[];
  string   NameFormat;
  string   Interconnect;
  string   InterconnectAddress;
  uint16   Types[];
  uint32   MaxNumberOfNodes;
  uint16   ClusterState;
};
```

## Members

The **CIM\_Cluster** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Cluster** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ClusterState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the state of the cluster. The cluster can be defined to be on-line (value=2), off-line (3), in a degraded mode of operation (4) or unavailable (5).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="On-line"></span><span id="on-line"></span><span id="ON-LINE"></span>

**On-line** (2)


</dt> <dd></dd> <dt>

<span id="Off-line"></span><span id="off-line"></span><span id="OFF-LINE"></span>

**Off-line** (3)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (4)


</dt> <dd></dd> <dt>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>

**Unavailable** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The CreationClassName property indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The InstallDate property is a datetime value indicating when the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Interconnect**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Interconnect is a free form string that describes the interconnection mechanism for the cluster.

</dd> <dt>

**InterconnectAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

InterconnectAddress indicates the address of the cluster system, which is dependent on the interconnection scheme. If no address is available or applicable, a null string should be used.

</dd> <dt>

**MaxNumberOfNodes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the maximum number of nodes that may participate in the cluster. If unlimited, enter 0.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The inherited Name property serves as key of a CIM\_System instance in an enterprise environment.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("NameFormat")
</dt> </dl>

The CIM\_ComputerSystem object and its derivatives are Top Level Objects of CIM. They provide the scope for numerous components. Having unique CIM\_System keys is required. A heuristic is defined to create the CIM\_ComputerSystem name to attempt to always generate the same name, independent of discovery protocol. This prevents inventory and management problems where the same asset or entity is discovered multiple times, but can not be resolved to a single object. Use of the heuristic is optional, but recommended.

The NameFormat property identifies how the computer system name is generated, using a heuristic. The heuristic is outlined, in detail, in the CIM V2 Common Model specification. It assumes that the documented rules are traversed in order, to determine and assign a name. The NameFormat values list defines the precedence order for assigning the computer system name. Several rules do map to the same Value.

Note that the CIM\_ComputerSystem Name calculated using the heuristic is the system's key value. Other names can be assigned and used for the CIM\_ComputerSystem, that better suit the business, using Aliases.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

<dt>



 ("Other")


</dt> <dd></dd> <dt>



 ("IP")


</dt> <dd></dd> <dt>



 ("Dial")


</dt> <dd></dd> <dt>



 ("HID")


</dt> <dd></dd> <dt>



 ("NWA")


</dt> <dd></dd> <dt>



 ("HWA")


</dt> <dd></dd> <dt>



 ("X25")


</dt> <dd></dd> <dt>



 ("ISDN")


</dt> <dd></dd> <dt>



 ("IPX")


</dt> <dd></dd> <dt>



 ("DCC")


</dt> <dd></dd> <dt>



 ("ICD")


</dt> <dd></dd> <dt>



 ("E.164")


</dt> <dd></dd> <dt>



 ("SNA")


</dt> <dd></dd> <dt>



 ("OID/OSI")


</dt> <dd></dd> </dl>

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

A string that provides information on how the primary system owner can be reached (e.g. phone number, email address, ...).

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

The name of the primary system owner.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**Roles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A collection of strings that specify the roles this system plays in the IT-environment.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

The Status property is a string indicating the current status of the object. Various operational and non-operational statuses can be defined. Operational statuses are "OK", "Degraded" and "Pred Fail". "Pred Fail" indicates that an element may be functioning properly but predicting a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses can also be specified. These are "Error", "Starting", "Stopping" and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither "OK" nor in one of the other states.

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


</dt> <dd></dd> </dl>

</dd> <dt>

**Types**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This displays the cluster types. This specifies whether the cluster is for failover (value=2), performance (3), etc. The values which can be specified are not mutually exclusive. Thus, Types is an array.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>

**Failover** (2)


</dt> <dd></dd> <dt>

<span id="Performance"></span><span id="performance"></span><span id="PERFORMANCE"></span>

**Performance** (3)


</dt> <dd></dd> <dt>

<span id="Distributed_OS"></span><span id="distributed_os"></span><span id="DISTRIBUTED_OS"></span>

**Distributed OS** (4)


</dt> <dd></dd> <dt>

<span id="Node_Grouping"></span><span id="node_grouping"></span><span id="NODE_GROUPING"></span>

**Node Grouping** (5)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> </dl>

 

 





