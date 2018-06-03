---
title: MSFT\_MTMemorySummary class
description: The memory data object. Statistic data is calculated based on current interval seconds setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 65951f9c-81b1-4b39-acfd-04cc926db184
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTMemorySummary class
- MSFT_MTMemorySummary class, described
topic_type:
- apiref
api_name:
- MSFT_MTMemorySummary
- MSFT_MTMemorySummary.InstanceID
- MSFT_MTMemorySummary.Caption
- MSFT_MTMemorySummary.Description
- MSFT_MTMemorySummary.ElementName
- MSFT_MTMemorySummary.Name
- MSFT_MTMemorySummary.Total
- MSFT_MTMemorySummary.InUse
- MSFT_MTMemorySummary.Modified
- MSFT_MTMemorySummary.Standby
- MSFT_MTMemorySummary.Free
- MSFT_MTMemorySummary.Installed
- MSFT_MTMemorySummary.PageSize
- MSFT_MTMemorySummary.DynamicMemoryMax
- MSFT_MTMemorySummary.DynamicMemoryEnabled
- MSFT_MTMemorySummary.PagedPool
- MSFT_MTMemorySummary.NonPagedPool
- MSFT_MTMemorySummary.Committed
- MSFT_MTMemorySummary.CommitLimit
- MSFT_MTMemorySummary.Available
- MSFT_MTMemorySummary.Cached
- MSFT_MTMemorySummary.Speed
- MSFT_MTMemorySummary.Type
- MSFT_MTMemorySummary.FormFactor
- MSFT_MTMemorySummary.HardwareReserved
- MSFT_MTMemorySummary.Capacity
- MSFT_MTMemorySummary.UsedSlots
- MSFT_MTMemorySummary.TotalSlots
- MSFT_MTMemorySummary.IntervalSeconds
- MSFT_MTMemorySummary.CurrentIndex
- MSFT_MTMemorySummary.Utilization
api_location:
- MtTmProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_MTMemorySummary class

The memory data object. Statistic data is calculated based on current interval seconds setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("mttmprov"), AMENDMENT]
class MSFT_MTMemorySummary : CIM_ManagedElement
{
  string  InstanceID;
  string  Caption;
  string  Description;
  string  ElementName;
  string  Name;
  uint64  Total;
  uint64  InUse;
  uint64  Modified;
  uint64  Standby;
  uint64  Free;
  uint64  Installed;
  uint32  PageSize;
  uint64  DynamicMemoryMax;
  boolean DynamicMemoryEnabled;
  uint64  PagedPool;
  uint64  NonPagedPool;
  uint64  Committed;
  uint64  CommitLimit;
  uint64  Available;
  uint64  Cached;
  uint32  Speed;
  uint16  Type;
  uint16  FormFactor;
  uint64  HardwareReserved;
  uint64  Capacity;
  uint16  UsedSlots;
  uint16  TotalSlots;
  uint16  IntervalSeconds;
  uint16  CurrentIndex;
  real32  Utilization[];
};
```

## Members

The **MSFT\_MTMemorySummary** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MTMemorySummary** class has these properties.

<dl> <dt>

**Available**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of memory (including Standby and Free memory) that is immediately available for use by processes, drivers, or the operating system.

</dd> <dt>

**Cached**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of memory (including Standby and Modified memory) containing cached data and code for rapid access by processes, drivers, and the operating system.

</dd> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the memory capacity on the computer system.

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

**CommitLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the limit of committed memory on the computer system.

</dd> <dt>

**Committed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of committed memory on the computer system.

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

**DynamicMemoryEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

returns **true** if dynamic memory is configured on the virtual machine; otherwise, **false**.

</dd> <dt>

**DynamicMemoryMax**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the maximum amount of memory allowed as dynamic memory on the virtual machine.

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

**FormFactor**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the form factor of memory installed on the computer system. This map is defined in Table 72 in section 7.18.1 (SMBIOS Reference Specification V2.7.0)

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="SIMM"></span><span id="simm"></span>

**SIMM** (3)


</dt> <dd></dd> <dt>

<span id="SIP"></span><span id="sip"></span>

**SIP** (4)


</dt> <dd></dd> <dt>

<span id="Chip"></span><span id="chip"></span><span id="CHIP"></span>

**Chip** (5)


</dt> <dd></dd> <dt>

<span id="DIP"></span><span id="dip"></span>

**DIP** (6)


</dt> <dd></dd> <dt>

<span id="ZIP"></span><span id="zip"></span>

**ZIP** (7)


</dt> <dd></dd> <dt>

<span id="Proprietary_Card"></span><span id="proprietary_card"></span><span id="PROPRIETARY_CARD"></span>

**Proprietary Card** (8)


</dt> <dd></dd> <dt>

<span id="DIMM"></span><span id="dimm"></span>

**DIMM** (9)


</dt> <dd></dd> <dt>

<span id="TSOP"></span><span id="tsop"></span>

**TSOP** (10)


</dt> <dd></dd> <dt>

<span id="Row_of_chips"></span><span id="row_of_chips"></span><span id="ROW_OF_CHIPS"></span>

**Row of chips** (11)


</dt> <dd></dd> <dt>

<span id="RIMM"></span><span id="rimm"></span>

**RIMM** (12)


</dt> <dd></dd> <dt>

<span id="SODIMM"></span><span id="sodimm"></span>

**SODIMM** (13)


</dt> <dd></dd> <dt>

<span id="SRIMM"></span><span id="srimm"></span>

**SRIMM** (14)


</dt> <dd></dd> <dt>

<span id="FB-DIMM"></span><span id="fb-dimm"></span>

**FB-DIMM** (15)


</dt> <dd></dd> </dl>

</dd> <dt>

**Free**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the free memory that does not contain any valuable data, and that will be used first when processes, drivers or the operating system need more memory.

</dd> <dt>

**HardwareReserved**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the memory that is reserved for use by the BIOS and some drivers for other peripherals.

</dd> <dt>

**Installed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the memory physically installed on the computer system.

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

**InUse**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the memory used by processes, drivers, or the operating system.

</dd> <dt>

**Modified**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the memory whose contents must be written to disk before it can be used for another purpose.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the name of memory object.

</dd> <dt>

**NonPagedPool**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of non-paged pool used on the computer system.

</dd> <dt>

**PagedPool**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of paged pool used on the computer system.

</dd> <dt>

**PageSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the page size of the operating system.

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the speed of memory operating on the computer system, in MHz.

</dd> <dt>

**Standby**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the memory that contains cached data and code that is not actively in use.

</dd> <dt>

**Total**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total amount of physical memory available to the operating system, device drivers, and processes.

</dd> <dt>

**TotalSlots**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of memory slots available on the computer system.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the type of memory installed on the computer system. This map is defined in Table 73 in section 7.18.2 (SMBIOS Reference Specification V2.7.0)

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="DRAM"></span><span id="dram"></span>

**DRAM** (3)


</dt> <dd></dd> <dt>

<span id="EDRAM"></span><span id="edram"></span>

**EDRAM** (4)


</dt> <dd></dd> <dt>

<span id="VRAM"></span><span id="vram"></span>

**VRAM** (5)


</dt> <dd></dd> <dt>

<span id="SRAM"></span><span id="sram"></span>

**SRAM** (6)


</dt> <dd></dd> <dt>

<span id="RAM"></span><span id="ram"></span>

**RAM** (7)


</dt> <dd></dd> <dt>

<span id="ROM"></span><span id="rom"></span>

**ROM** (8)


</dt> <dd></dd> <dt>

<span id="FLASH"></span><span id="flash"></span>

**FLASH** (9)


</dt> <dd></dd> <dt>

<span id="EEPROM"></span><span id="eeprom"></span>

**EEPROM** (10)


</dt> <dd></dd> <dt>

<span id="FEPROM"></span><span id="feprom"></span>

**FEPROM** (11)


</dt> <dd></dd> <dt>

<span id="EPROM"></span><span id="eprom"></span>

**EPROM** (12)


</dt> <dd></dd> <dt>

<span id="CDRAM"></span><span id="cdram"></span>

**CDRAM** (13)


</dt> <dd></dd> <dt>

<span id="ThreeDRAM"></span><span id="threedram"></span><span id="THREEDRAM"></span>

**ThreeDRAM** (14)


</dt> <dd></dd> <dt>

<span id="SDRAM"></span><span id="sdram"></span>

**SDRAM** (15)


</dt> <dd></dd> <dt>

<span id="SGRAM"></span><span id="sgram"></span>

**SGRAM** (16)


</dt> <dd></dd> <dt>

<span id="RDRAM"></span><span id="rdram"></span>

**RDRAM** (17)


</dt> <dd></dd> <dt>

<span id="DDR"></span><span id="ddr"></span>

**DDR** (18)


</dt> <dd></dd> <dt>

<span id="DDR2"></span><span id="ddr2"></span>

**DDR2** (19)


</dt> <dd></dd> <dt>

<span id="DDR2_FB_DIMM"></span><span id="ddr2_fb_dimm"></span>

**DDR2\_FB\_DIMM** (20)


</dt> <dd></dd> <dt>

<span id="Reserved1"></span><span id="reserved1"></span><span id="RESERVED1"></span>

**Reserved1** (21)


</dt> <dd></dd> <dt>

<span id="Reserved2"></span><span id="reserved2"></span><span id="RESERVED2"></span>

**Reserved2** (22)


</dt> <dd></dd> <dt>

<span id="Reserved3"></span><span id="reserved3"></span><span id="RESERVED3"></span>

**Reserved3** (23)


</dt> <dd></dd> <dt>

<span id="DDR3"></span><span id="ddr3"></span>

**DDR3** (24)


</dt> <dd></dd> <dt>

<span id="FBD2"></span><span id="fbd2"></span>

**FBD2** (25)


</dt> <dd></dd> </dl>

</dd> <dt>

**UsedSlots**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of memory slots used on the computer system.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of historical statistics of percentage of memory utilization on the computer system. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

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

 

 





