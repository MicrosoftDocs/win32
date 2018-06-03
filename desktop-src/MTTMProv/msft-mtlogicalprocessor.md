---
title: MSFT\_MTLogicalProcessor class
description: The Logical Processor data object. Statistic data is calculated based on current interval seconds setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6700cd4-19d2-444f-a4b7-d5055087531f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTLogicalProcessor class
- MSFT_MTLogicalProcessor class, described
topic_type:
- apiref
api_name:
- MSFT_MTLogicalProcessor
- MSFT_MTLogicalProcessor.InstanceID
- MSFT_MTLogicalProcessor.Caption
- MSFT_MTLogicalProcessor.Description
- MSFT_MTLogicalProcessor.ElementName
- MSFT_MTLogicalProcessor.NodeId
- MSFT_MTLogicalProcessor.CpuId
- MSFT_MTLogicalProcessor.Parking
- MSFT_MTLogicalProcessor.IntervalSeconds
- MSFT_MTLogicalProcessor.CurrentIndex
- MSFT_MTLogicalProcessor.Utilization
- MSFT_MTLogicalProcessor.Privileged
api_location:
- MtTmProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_MTLogicalProcessor class

The Logical Processor data object. Statistic data is calculated based on current interval seconds setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("mttmprov"), AMENDMENT]
class MSFT_MTLogicalProcessor : CIM_ManagedElement
{
  string  InstanceID;
  string  Caption;
  string  Description;
  string  ElementName;
  uint16  NodeId;
  uint16  CpuId;
  boolean Parking;
  uint16  IntervalSeconds;
  uint16  CurrentIndex;
  real32  Utilization[];
  real32  Privileged[];
};
```

## Members

The **MSFT\_MTLogicalProcessor** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MTLogicalProcessor** class has these properties.

<dl> <dt>

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

**CpuId**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the identification number of logical processor.

</dd> <dt>

**CurrentIndex**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current data sample index. The increment at every data sample.

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

Gets a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the **Name** property of [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where **Name** exists and is not a Key (such as for instances of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)), the same information can be present in both the **Name** and **ElementName** properties. Note that if there is an associated instance of **CIM\_EnabledLogicalElementCapabilities**, restrictions on this properties may exist as defined in **ElementNameMask** and **MaxElementNameLen** properties defined in that class.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**InstanceID** is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below. To ensure uniqueness within the NameSpace, the value of **InstanceID** should be constructed using the following "preferred" algorithm: "*OrgID*:*LocalID*" Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the **InstanceID** or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in **InstanceID** must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting **InstanceID** is not reused across any **InstanceID**s produced by this or other providers for the NameSpace of this instance. If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to "CIM".

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**IntervalSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current data collection interval in seconds.

</dd> <dt>

**NodeId**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the identification number of the NUMA node or processor socket. If empty, it presents an aggregated NUMA, or the Socket itself.

</dd> <dt>

**Parking**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that is **true** if the processor is in a parked state; otherwise, **false**.

</dd> <dt>

**Privileged**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of historical statistics of percentage of privileged kernel utilization on the logical processor. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of historical statistics of percentage of utilization on the logical processor. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dt>

[Management Tools Task Manager WMI Provider](management-tools-task-manager-wmi-provider-portal.md)
</dt> </dl>

 

 





