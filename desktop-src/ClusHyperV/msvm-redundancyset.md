---
title: Msvm\_RedundancySet class
description: Represents a collection of managed elements that provide redundancy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9c6173a8-9dab-4759-a0f1-9f42fe24724c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msvm_RedundancySet class", "Msvm_RedundancySet class, described"]
topic_type:
- apiref
api_name:
- Msvm_RedundancySet
- Msvm_RedundancySet.Caption
- Msvm_RedundancySet.Description
- Msvm_RedundancySet.ElementName
- Msvm_RedundancySet.InstanceID
- Msvm_RedundancySet.RedundancyStatus
- Msvm_RedundancySet.TypeOfSet
- Msvm_RedundancySet.MinNumberNeeded
- Msvm_RedundancySet.MaxNumberSupported
- Msvm_RedundancySet.VendorIdentifyingInfo
- Msvm_RedundancySet.OtherTypeOfSet
- Msvm_RedundancySet.LoadBalanceAlgorithm
- Msvm_RedundancySet.OtherLoadBalanceAlgorithm
api_location:
- VMMS.exe
api_type:
- DllExport
---

# Msvm\_RedundancySet class

Represents a collection of managed elements that provide redundancy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_RedundancySet : CIM_RedundancySet
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  uint16 RedundancyStatus;
  uint16 TypeOfSet[];
  uint32 MinNumberNeeded;
  uint32 MaxNumberSupported;
  string VendorIdentifyingInfo;
  string OtherTypeOfSet[];
  uint16 LoadBalanceAlgorithm;
  string OtherLoadBalanceAlgorithm;
};
```

## Members

The **Msvm\_RedundancySet** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_RedundancySet** class has these methods.



| Method                                          | Description                                                                                                                                                 |
|:------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Failover**](msvm-redundancyset-failover.md) | Forces a failover from one managed element to another.<br/> This method is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).<br/> |



 

### Properties

The **Msvm\_RedundancySet** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following format: *OrgID*:*LocalID*

-   *OrgID* must include a copyrighted, trademarked or a unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names.
-   The first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
-   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
-   If this format is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
-   For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

This property is inherited from [**CIM\_SystemSpecificCollection**](cim-systemspecificcollection.md).

</dd> <dt>

**LoadBalanceAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_RedundancySet**](cim-redundancyset.md).**OtherLoadBalanceAlgorithm**")
</dt> </dl>

The current load balancing algorithm of the redundancy set.

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="No_Load_Balancing"></span><span id="no_load_balancing"></span><span id="NO_LOAD_BALANCING"></span>

**No Load Balancing** (2)


</dt> <dd></dd> <dt>

<span id="Round_Robin"></span><span id="round_robin"></span><span id="ROUND_ROBIN"></span>

**Round Robin** (3)


</dt> <dd></dd> <dt>

<span id="Least_Blocks"></span><span id="least_blocks"></span><span id="LEAST_BLOCKS"></span>

**Least Blocks** (4)


</dt> <dd></dd> <dt>

<span id="Least_IO"></span><span id="least_io"></span><span id="LEAST_IO"></span>

**Least IO** (5)


</dt> <dd></dd> <dt>

<span id="Address_Region"></span><span id="address_region"></span><span id="ADDRESS_REGION"></span>

**Address Region** (6)


</dt> <dd></dd> <dt>

<span id="Product_Specific"></span><span id="product_specific"></span><span id="PRODUCT_SPECIFIC"></span>

**Product Specific** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**MaxNumberSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The largest number of elements that can participate in the r edundancy set. A value of "0" indicates there is no limit on the number of elements.

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

</dd> <dt>

**MinNumberNeeded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

The minimum number of elements that must be operational for redundancy to function.

This property is not used if **TypeOfSet** is set to "5" (limited sparing).

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

</dd> <dt>

**OtherLoadBalanceAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_RedundancySet**](cim-redundancyset.md).**LoadBalanceAlgorithm**")
</dt> </dl>

An array that contains descriptions of **LoadBalanceAlgorithm** values that are set to "1" (other).

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

</dd> <dt>

**OtherTypeOfSet**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_RedundancySet**](cim-redundancyset.md).**TypeOfSet**")
</dt> </dl>

An array that contains descriptions of **TypeOfSet** values that are set to "1" (other).

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

</dd> <dt>

**RedundancyStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_RedundancySet**](cim-redundancyset.md).**MinNumberNeeded**")
</dt> </dl>

The state of the redundancy group.

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (1)


</dt> <dd></dd> <dt>

<span id="Fully_Redundant"></span><span id="fully_redundant"></span><span id="FULLY_REDUNDANT"></span>

**Fully Redundant** (2)


</dt> <dd></dd> <dt>

<span id="Degraded_Redundancy"></span><span id="degraded_redundancy"></span><span id="DEGRADED_REDUNDANCY"></span>

**Degraded Redundancy** (3)


</dt> <dd></dd> <dt>

<span id="Redundancy_Lost"></span><span id="redundancy_lost"></span><span id="REDUNDANCY_LOST"></span>

**Redundancy Lost** (4)


</dt> <dd></dd> <dt>

<span id="Overall_Failure"></span><span id="overall_failure"></span><span id="OVERALL_FAILURE"></span>

**Overall Failure** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**TypeOfSet**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_RedundancySet**](cim-redundancyset.md).**OtherTypeOfSet**")
</dt> </dl>

An array that contains information about the type of redundancy used by the collection.

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="N_1"></span><span id="n_1"></span>

**N+1** (2)


</dt> <dd></dd> <dt>

<span id="Load_Balanced"></span><span id="load_balanced"></span><span id="LOAD_BALANCED"></span>

**Load Balanced** (3)


</dt> <dd></dd> <dt>

<span id="Sparing"></span><span id="sparing"></span><span id="SPARING"></span>

**Sparing** (4)


</dt> <dd></dd> <dt>

<span id="Limited_Sparing"></span><span id="limited_sparing"></span><span id="LIMITED_SPARING"></span>

**Limited Sparing** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**VendorIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The vendor identifying data for the redundancy set. One example is the product name for a cluster.

This property is inherited from [**CIM\_RedundancySet**](cim-redundancyset.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_RedundancySet**](cim-redundancyset.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





