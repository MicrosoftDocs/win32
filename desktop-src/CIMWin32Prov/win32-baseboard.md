---
description: Represents a baseboard, which is also known as a motherboard or system board.
ms.assetid: 04ac7522-8b99-4ffc-9f7d-d1225f55a862
ms.tgt_platform: multiple
title: Win32_BaseBoard class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_BaseBoard
- Win32_BaseBoard.IsCompatible
- Win32_BaseBoard.Caption
- Win32_BaseBoard.ConfigOptions
- Win32_BaseBoard.CreationClassName
- Win32_BaseBoard.Depth
- Win32_BaseBoard.Description
- Win32_BaseBoard.Height
- Win32_BaseBoard.HostingBoard
- Win32_BaseBoard.HotSwappable
- Win32_BaseBoard.InstallDate
- Win32_BaseBoard.Manufacturer
- Win32_BaseBoard.Model
- Win32_BaseBoard.Name
- Win32_BaseBoard.OtherIdentifyingInfo
- Win32_BaseBoard.PartNumber
- Win32_BaseBoard.PoweredOn
- Win32_BaseBoard.Product
- Win32_BaseBoard.Removable
- Win32_BaseBoard.Replaceable
- Win32_BaseBoard.RequirementsDescription
- Win32_BaseBoard.RequiresDaughterBoard
- Win32_BaseBoard.SerialNumber
- Win32_BaseBoard.SKU
- Win32_BaseBoard.SlotLayout
- Win32_BaseBoard.SpecialRequirements
- Win32_BaseBoard.Status
- Win32_BaseBoard.Tag
- Win32_BaseBoard.Version
- Win32_BaseBoard.Weight
- Win32_BaseBoard.Width
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_BaseBoard class

The **Win32\_BaseBoard** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) represents a baseboard, which is also known as a motherboard or system board.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{FAF76B95-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class Win32_BaseBoard : CIM_Card
{
  string   Caption;
  string   ConfigOptions[];
  string   CreationClassName;
  real32   Depth;
  string   Description;
  real32   Height;
  boolean  HostingBoard;
  boolean  HotSwappable;
  datetime InstallDate;
  string   Manufacturer;
  string   Model;
  string   Name;
  string   OtherIdentifyingInfo;
  string   PartNumber;
  boolean  PoweredOn;
  string   Product;
  boolean  Removable;
  boolean  Replaceable;
  string   RequirementsDescription;
  boolean  RequiresDaughterBoard;
  string   SerialNumber;
  string   SKU;
  string   SlotLayout;
  boolean  SpecialRequirements;
  string   Status;
  string   Tag;
  string   Version;
  real32   Weight;
  real32   Width;
};
```

## Members

The **Win32\_BaseBoard** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_BaseBoard** class has these methods.



| Method           | Description                 |
|:-----------------|:----------------------------|
| **IsCompatible** | Not implemented.<br/> |



 

### Properties

The **Win32\_BaseBoard** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

Short description of the object a one-line string.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ConfigOptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 12\|Configuration Options Strings")
</dt> </dl>

Array that represents the configuration of the jumpers and switches located on the baseboard.

Example: "JP2: 1-2 Cache Size is 256K, 2-3 Cache Size is 512K, SW1-1: Close to Disable On Board Video"

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Name of the first concrete class that appears in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, the property allows all instances of this class and its subclasses to be identified uniquely.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Depth**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("inches")
</dt> </dl>

Depth of the physical package in inches.

This property is inherited from [**CIM\_PhysicalPackage**](cim-physicalpackage.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Height**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("inches")
</dt> </dl>

Height of the physical package in inches.

This property is inherited from [**CIM\_PhysicalPackage**](cim-physicalpackage.md).

</dd> <dt>

**HostingBoard**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the card is a motherboard, or a baseboard in a chassis.

This property is inherited from [**CIM\_Card**](cim-card.md).

</dd> <dt>

**HotSwappable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the package can be hot-swapped. A physical package can be hot-swapped if it is possible to replace the element with a physically different but equivalent element while the containing package has power applied to it that is, while it is ON. For example, a disk drive package inserted using SCA connectors is removable and can be hot-swapped. All packages that can be hot-swapped are inherently removable and replaceable.

This property is inherited from [**CIM\_PhysicalPackage**](cim-physicalpackage.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

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

Name of the organization responsible for producing the physical element.

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

Name by which the physical element is known.

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

Label by which the object is known. When subclassed, the property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Captures additional data, beyond asset tag information, that can be used to identify a physical element. One example is bar code data that is associated with an element that also has an asset tag. Note that if only bar code data is available and unique or able to be used as an element key, the property value would be **NULL** and the bar code data would be used as the class key, in the tag property.

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

If **TRUE**, the physical element is powered ON.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 2\|Product")
</dt> </dl>

Baseboard part number defined by the manufacturer.

</dd> <dt>

**Removable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, a package is removable. A physical package is removable if it is designed to be taken in and out of the physical container in which it is normally found without impairing the function of the overall packaging. A package can still be removable if the power must be OFF to perform the removal. If the power can be ON and the package removed, then the element is removable and can be hot-swapped. For example, an extra battery in a laptop is removable, as is a disk drive package inserted using SCA connectors. However, the latter can also be hot-swapped. A laptop's display is not removable, nor is a nonredundant power supply. Removing these components would impact the function of the overall packaging, or is impossible due to the tight integration of the package.

This property is inherited from [**CIM\_PhysicalPackage**](cim-physicalpackage.md).

</dd> <dt>

**Replaceable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, a package is replaceable. A physical package is replaceable if it is possible to replace (FRU or upgrade) the element with a physically different one. For example, some computer systems allow the main processor chip to be upgraded to one of a higher clock rating. In this case, the processor is said to be replaceable. Another example is a power supply package mounted on sliding rails. All removable packages are inherently replaceable.

This property is inherited from [**CIM\_PhysicalPackage**](cim-physicalpackage.md).

</dd> <dt>

**RequirementsDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Card**](cim-card.md).**SpecialRequirements**")
</dt> </dl>

Free-form string that describes the way in which this card is physically unique from other cards. The property only has meaning when the corresponding Boolean property **SpecialRequirements** is set to **TRUE**.

This property is inherited from [**CIM\_Card**](cim-card.md).

</dd> <dt>

**RequiresDaughterBoard**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, at least one daughterboard or auxiliary card is required to function properly.

This property is inherited from [**CIM\_Card**](cim-card.md).

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

Stock-keeping unit number for the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**SlotLayout**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that describes the slot position, typical usage, restrictions, individual slot spacing or any other pertinent information for the slots on a card.

This property is inherited from [**CIM\_Card**](cim-card.md).

</dd> <dt>

**SpecialRequirements**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Card**](cim-card.md).**RequirementsDescription**")
</dt> </dl>

If **TRUE**, this card is physically unique from other cards of the same type and therefore requires a special slot. For example, a double-wide card requires two slots. Another example is where a certain card may be used for the same general function as other cards but requires a special slot (for example, extra long), whereas the other cards can be placed in any available slot. If set to **TRUE**, then the corresponding property, **RequirementsDescription**, should specify the nature of the uniqueness or purpose of the card.

This property is inherited from [**CIM\_Card**](cim-card.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

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

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Tag"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI")
</dt> </dl>

Unique identifier of the baseboard of the system.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

Example: "Base Board"

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Version of the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("pounds")
</dt> </dl>

Weight of the physical package in pounds.

This property is inherited from [**CIM\_PhysicalPackage**](cim-physicalelement.md).

</dd> <dt>

**Width**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("inches")
</dt> </dl>

Width of the physical package in inches.

This property is inherited from [**CIM\_PhysicalPackage**](cim-physicalelement.md).

</dd> </dl>

## Remarks

The **Win32\_BaseBoard** class is derived from [**CIM\_Card**](cim-card.md) which derives from [**CIM\_PhysicalPackage**](cim-physicalelement.md).

## Examples

The [List Computer Baseboard Properties](https://Gallery.TechNet.Microsoft.Com/932346d8-4a23-4dac-bdbd-01fc14d526f8) Perl sample returns information about the computer baseboard.

The [List Computer Baseboard Properties](https://Gallery.TechNet.Microsoft.Com/359772a2-c70e-45e9-bdad-f79efe2420a9) PowerShell sample returns information about the computer baseboard.

The following VBScript sample also returns information about the computer baseboard.


```VB
On Error Resume Next 
 
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set colItems = objWMIService.ExecQuery("Select * from Win32_BaseBoard") 
 
For Each objItem in colItems 
    For Each strOption in objItem.ConfigOptions 
        Wscript.Echo "Configuration Option: " & strOption 
    Next 
    Wscript.Echo "Depth: " & objItem.Depth 
    Wscript.Echo "Description: " & objItem.Description 
    Wscript.Echo "Height: " & objItem.Height 
    Wscript.Echo "Hosting Board: " & objItem.HostingBoard 
    Wscript.Echo "Hot Swappable: " & objItem.HotSwappable 
    Wscript.Echo "Manufacturer: " & objItem.Manufacturer 
    Wscript.Echo "Model: " & objItem.Model 
    Wscript.Echo "Name: " & objItem.Name 
    Wscript.Echo "Other Identifying Information: " & _ 
        objItem.OtherIdentifyingInfo 
    Wscript.Echo "Part Number: " & objItem.PartNumber 
    Wscript.Echo "Powered-On: " & objItem.PoweredOn 
    Wscript.Echo "Product: " & objItem.Product 
    Wscript.Echo "Removable: " & objItem.Removable 
    Wscript.Echo "Replaceable: " & objItem.Replaceable 
    Wscript.Echo "Requirements Description: " & objItem.RequirementsDescription 
    Wscript.Echo "Requires Daughterboard: " & objItem.RequiresDaughterBoard 
    Wscript.Echo "Serial Number: " & objItem.SerialNumber 
    Wscript.Echo "SKU: " & objItem.SKU 
    Wscript.Echo "Slot Layout: " & objItem.SlotLayout 
    Wscript.Echo "Special Requirements: " & objItem.SpecialRequirements 
    Wscript.Echo "Tag: " & objItem.Tag 
    Wscript.Echo "Version: " & objItem.Version 
    Wscript.Echo "Weight: " & objItem.Weight 
    Wscript.Echo "Width: " & objItem.Width 
Next 
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Card**](cim-card.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

