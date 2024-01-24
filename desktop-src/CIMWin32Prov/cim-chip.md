---
description: The CIM\_Chip class represents the type of integrated circuit hardware, including ASICs, processors, memory chips, and so on.
ms.assetid: 3c2b0023-5d02-49b9-90f5-d66eb8a103f0
ms.tgt_platform: multiple
title: CIM_Chip class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Chip
- CIM_Chip.Caption
- CIM_Chip.Description
- CIM_Chip.InstallDate
- CIM_Chip.Name
- CIM_Chip.Status
- CIM_Chip.CreationClassName
- CIM_Chip.Manufacturer
- CIM_Chip.Model
- CIM_Chip.OtherIdentifyingInfo
- CIM_Chip.PartNumber
- CIM_Chip.PoweredOn
- CIM_Chip.SerialNumber
- CIM_Chip.SKU
- CIM_Chip.Tag
- CIM_Chip.Version
- CIM_Chip.HotSwappable
- CIM_Chip.Removable
- CIM_Chip.Replaceable
- CIM_Chip.FormFactor
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_Chip class

The **CIM\_Chip** class represents the type of integrated circuit hardware, including ASICs, processors, memory chips, and so on.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, UUID("{FAF76B7A-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_Chip : CIM_PhysicalComponent
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   CreationClassName;
  string   Manufacturer;
  string   Model;
  string   OtherIdentifyingInfo;
  string   PartNumber;
  boolean  PoweredOn;
  string   SerialNumber;
  string   SKU;
  string   Tag;
  string   Version;
  boolean  HotSwappable;
  boolean  Removable;
  boolean  Replaceable;
  uint16   FormFactor;
};
```

## Members

The **CIM\_Chip** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Chip** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**FormFactor**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Implementation form factor for the chip. The following values can be specified.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="SIP"></span><span id="sip"></span>

**SIP** (2)


</dt> <dd></dd> <dt>

<span id="DIP"></span><span id="dip"></span>

**DIP** (3)


</dt> <dd></dd> <dt>

<span id="ZIP"></span><span id="zip"></span>

**ZIP** (4)


</dt> <dd></dd> <dt>

<span id="SOJ"></span><span id="soj"></span>

**SOJ** (5)


</dt> <dd></dd> <dt>

<span id="Proprietary"></span><span id="proprietary"></span><span id="PROPRIETARY"></span>

**Proprietary** (6)


</dt> <dd></dd> <dt>

<span id="SIMM"></span><span id="simm"></span>

**SIMM** (7)


</dt> <dd></dd> <dt>

<span id="DIMM"></span><span id="dimm"></span>

**DIMM** (8)


</dt> <dd></dd> <dt>

<span id="TSOP"></span><span id="tsop"></span>

**TSOP** (9)


</dt> <dd></dd> <dt>

<span id="PGA"></span><span id="pga"></span>

**PGA** (10)


</dt> <dd></dd> <dt>

<span id="RIMM"></span><span id="rimm"></span>

**RIMM** (11)


</dt> <dd></dd> <dt>

<span id="SODIMM"></span><span id="sodimm"></span>

**SODIMM** (12)


</dt> <dd></dd> <dt>

<span id="SRIMM"></span><span id="srimm"></span>

**SRIMM** (13)


</dt> <dd></dd> <dt>

<span id="SMD"></span><span id="smd"></span>

**SMD** (14)


</dt> <dd></dd> <dt>

<span id="SSMP"></span><span id="ssmp"></span>

**SSMP** (15)


</dt> <dd></dd> <dt>

<span id="QFP"></span><span id="qfp"></span>

**QFP** (16)


</dt> <dd></dd> <dt>

<span id="TQFP"></span><span id="tqfp"></span>

**TQFP** (17)


</dt> <dd></dd> <dt>

<span id="SOIC"></span><span id="soic"></span>

**SOIC** (18)


</dt> <dd></dd> <dt>

<span id="LCC"></span><span id="lcc"></span>

**LCC** (19)


</dt> <dd></dd> <dt>

<span id="PLCC"></span><span id="plcc"></span>

**PLCC** (20)


</dt> <dd></dd> <dt>

<span id="BGA"></span><span id="bga"></span>

**BGA** (21)


</dt> <dd></dd> <dt>

<span id="FPBGA"></span><span id="fpbga"></span>

**FPBGA** (22)


</dt> <dd></dd> <dt>

<span id="LGA"></span><span id="lga"></span>

**LGA** (23)


</dt> <dd></dd> <dt>

<span id="FB-DIMM"></span><span id="fb-dimm"></span>

**FB-DIMM** (24)


</dt> <dd></dd> </dl>

</dd> <dt>

**HotSwappable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the package can be hot-swapped. A physical package can be hot-swapped if the element can be replaced by a physically different (but equivalent) one while the containing package is turned on. For example, a fan component may be designed to be hot-swapped. All components that can be hot-swapped are inherently removable and replaceable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Name of the organization responsible for producing the physical element. For more information, see the **Vendor** property of [**CIM\_Product**](cim-product.md).

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Name by which the physical element is generally known.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional data, beyond asset tag information, that can be used to identify a physical element. One example is bar-code data that is associated with an element, which also has an asset tag. Note that if only bar-code data is available, and is unique and able to be used as an element key, this property would be null and the bar-code data would be used as the class key in the **Tag** property.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Part number assigned by the organization responsible for producing or manufacturing the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PoweredOn**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the physical element is powered on. Otherwise, it is currently off.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Removable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this element is designed to be taken in and out of the physical container in which it is normally found, without impairing the function of the overall packaging. A package is considered removable even if the power must be off to perform the removal. If the power can be on and the package removed, then the element is removable and can be hot-swapped. For example, an upgradeable processor chip is removable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**Replaceable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, it is possible to replace the element with a physically different one. For example, some computer systems allow the main processor chip to be upgraded to one of a higher clock rating. In this case, the processor is said to be replaceable. All removable components are inherently replaceable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Manufacturer-allocated number used to identify the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**SKU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Stock-keeping unit number for this physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**Tag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Uniquely identifies the physical element and serves as the element's key. This property can contain information, such as asset tag or serial number data. The key for [**CIM\_PhysicalElement**](cim-physicalelement.md) is placed very high in the object hierarchy to independently identify the hardware or entity, regardless of physical placement in (or on) cabinets, adapters, and so on. For example, a removable component that can be hot-swapped can be taken from its containing (scoping) package and be temporarily unused. The object still continues to exist and can even be inserted into a different scoping container. The key for a physical element is an arbitrary string that is defined independently of placement or location-oriented hierarchy.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Indicates the version of the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> </dl>

## Remarks

The **CIM\_Chip** class is derived from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

WMI does not implement this class. For more information about classes derived from **CIM\_Chip**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PhysicalComponent**](cim-physicalcomponent.md)
</dt> </dl>

 

