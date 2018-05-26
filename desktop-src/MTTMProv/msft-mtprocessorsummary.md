---
title: MSFT\_MTProcessorSummary class
description: The Processor data object. Statistic data is calculated based on current interval seconds setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b001150-5b56-4592-81fb-52ba3948d16f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTProcessorSummary class
- MSFT_MTProcessorSummary class, described
topic_type:
- apiref
api_name:
- MSFT_MTProcessorSummary
- MSFT_MTProcessorSummary.InstanceID
- MSFT_MTProcessorSummary.Caption
- MSFT_MTProcessorSummary.Description
- MSFT_MTProcessorSummary.ElementName
- MSFT_MTProcessorSummary.Name
- MSFT_MTProcessorSummary.Virtualization
- MSFT_MTProcessorSummary.AverageSpeed
- MSFT_MTProcessorSummary.MaximumSpeed
- MSFT_MTProcessorSummary.Sockets
- MSFT_MTProcessorSummary.Cores
- MSFT_MTProcessorSummary.LogicalProcessors
- MSFT_MTProcessorSummary.L1Cache
- MSFT_MTProcessorSummary.L2Cache
- MSFT_MTProcessorSummary.L3Cache
- MSFT_MTProcessorSummary.Processes
- MSFT_MTProcessorSummary.Threads
- MSFT_MTProcessorSummary.Handles
- MSFT_MTProcessorSummary.Uptime
- MSFT_MTProcessorSummary.NumaNodes
- MSFT_MTProcessorSummary.IntervalSeconds
- MSFT_MTProcessorSummary.CurrentIndex
- MSFT_MTProcessorSummary.Utilization
- MSFT_MTProcessorSummary.Privileged
api_location:
- MtTmProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_MTProcessorSummary class

The Processor data object. Statistic data is calculated based on current interval seconds setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("mttmprov"), AMENDMENT]
class MSFT_MTProcessorSummary : CIM_ManagedElement
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  string Name;
  uint16 Virtualization;
  real32 AverageSpeed;
  real32 MaximumSpeed;
  uint32 Sockets;
  uint32 Cores;
  uint32 LogicalProcessors;
  uint32 L1Cache;
  uint32 L2Cache;
  uint32 L3Cache;
  uint32 Processes;
  uint32 Threads;
  uint32 Handles;
  uint64 Uptime;
  uint16 NumaNodes;
  uint16 IntervalSeconds;
  uint16 CurrentIndex;
  real32 Utilization[];
  real32 Privileged[];
};
```

## Members

The **MSFT\_MTProcessorSummary** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MTProcessorSummary** class has these properties.

<dl> <dt>

**AverageSpeed**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the Current average speed of the processors on the computer system, in MHz.

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

**Cores**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of processor cores on the computer system.

</dd> <dt>

**CurrentIndex**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current data sample index. Increment at every data sample.

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

**Handles**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of current active handles on the computer system.

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

**L1Cache**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total size, in kilobytes, of the L1 cache on the computer system.

</dd> <dt>

**L2Cache**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total size, in kilobytes, of the L2 cache on the computer system.

</dd> <dt>

**L3Cache**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total size, in kilobytes, of the L3 cache on the computer system.

</dd> <dt>

**LogicalProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of logical processors on the computer system.

</dd> <dt>

**MaximumSpeed**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the maximum speed of the processors on the computer system, in MHz.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the Name of processor.

</dd> <dt>

**NumaNodes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of NUMA nodes on the computer system.

</dd> <dt>

**Privileged**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the historical statistics of percentage of privileged kernel utilization on the computer system. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**Processes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of current active processes on the computer system.

</dd> <dt>

**Sockets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of processor sockets on the computer system.

</dd> <dt>

**Threads**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of current active threads on the computer system.

</dd> <dt>

**Uptime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the time the computer system has been working and available, in the number of 100-nanosecond intervals.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the Historical statistics of percentage of processor total utilization on the computer system. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**Virtualization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of Hyper-V virtual machine on the computer system.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

None - unknown state

</dd> <dt>

<span id="VM"></span><span id="vm"></span>

<span id="VM"></span><span id="vm"></span>**VM** (1)


</dt> <dd>

VM - Virtual Machine

</dd> <dt>

<span id="VMHost"></span><span id="vmhost"></span><span id="VMHOST"></span>

<span id="VMHost"></span><span id="vmhost"></span><span id="VMHOST"></span>**VMHost** (2)


</dt> <dd>

VMHost - Hosting Virtual Machines

</dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (3)


</dt> <dd>

Enabled - Hosting is enabled

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (4)


</dt> <dd>

Disabled - Hosting is disabled

</dd> <dt>

<span id="HyperVCapable"></span><span id="hypervcapable"></span><span id="HYPERVCAPABLE"></span>

<span id="HyperVCapable"></span><span id="hypervcapable"></span><span id="HYPERVCAPABLE"></span>**HyperVCapable** (5)


</dt> <dd>

HyperVCapable - Hyper-V capable

</dd> <dt>

<span id="HyperVIncapable"></span><span id="hypervincapable"></span><span id="HYPERVINCAPABLE"></span>

<span id="HyperVIncapable"></span><span id="hypervincapable"></span><span id="HYPERVINCAPABLE"></span>**HyperVIncapable** (6)


</dt> <dd>

HyperVIncapable - Hyper-V incapable

</dd> </dl>

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

 

 





