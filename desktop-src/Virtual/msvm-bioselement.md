---
title: Msvm\_BIOSElement class
description: Represents the low-level software that is loaded into RAM to configure and start the system.
ms.assetid: a17ee4d1-2b3c-4199-a117-f8a9525bf613
keywords:
- Msvm_BIOSElement class Hyper-V
- Msvm_BIOSElement class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_BIOSElement
- Msvm_BIOSElement.Caption
- Msvm_BIOSElement.Description
- Msvm_BIOSElement.ElementName
- Msvm_BIOSElement.InstallDate
- Msvm_BIOSElement.OperationalStatus
- Msvm_BIOSElement.Status
- Msvm_BIOSElement.HealthState
- Msvm_BIOSElement.Name
- Msvm_BIOSElement.SoftwareElementState
- Msvm_BIOSElement.SoftwareElementID
- Msvm_BIOSElement.TargetOperatingSystem
- Msvm_BIOSElement.OtherTargetOS
- Msvm_BIOSElement.BuildNumber
- Msvm_BIOSElement.SerialNumber
- Msvm_BIOSElement.CodeSet
- Msvm_BIOSElement.IdentificationCode
- Msvm_BIOSElement.LanguageEdition
- Msvm_BIOSElement.Version
- Msvm_BIOSElement.Manufacturer
- Msvm_BIOSElement.PrimaryBIOS
- Msvm_BIOSElement.CurrentLanguage
- Msvm_BIOSElement.LoadedStartingAddress
- Msvm_BIOSElement.LoadedEndingAddress
- Msvm_BIOSElement.LoadUtilityInformation
- Msvm_BIOSElement.EmbeddedControllerFirmwareMinorRelease
- Msvm_BIOSElement.EmbeddedControllerFirmwareMajorRelease
- Msvm_BIOSElement.SystemBIOSMinorRelease
- Msvm_BIOSElement.SystemBIOSMajorRelease
- Msvm_BIOSElement.StatusDescriptions
- Msvm_BIOSElement.ListOfLanguages
- Msvm_BIOSElement.ReleaseDate
- Msvm_BIOSElement.BIOSGUID
- Msvm_BIOSElement.BIOSSerialNumber
- Msvm_BIOSElement.BaseBoardSerialNumber
- Msvm_BIOSElement.ChassisSerialNumber
- Msvm_BIOSElement.ChassisAssetTag
- Msvm_BIOSElement.BIOSNumLock
- Msvm_BIOSElement.BootOrder
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_BIOSElement class

Represents the low-level software that is loaded into RAM to configure and start the system. The BIOS is not a logical device, hence the virtual BIOS should not be thought of as a virtual computer system device. As it is not a device, it does not have a corresponding resource pool. The BIOS object is associated with the virtual computer system through the [**Msvm\_SystemBIOS**](msvm-systembios.md) association.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_BIOSElement : CIM_BIOSElement
{
  string   Caption = "BIOS";
  string   Description = "Microsoft Virtual BIOS";
  string   ElementName = "BIOS";
  datetime InstallDate;
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  string   Name = "BIOS";
  uint16   SoftwareElementState = 2;
  string   SoftwareElementID = "Microsoft:GUID\device-specific data";
  uint16   TargetOperatingSystem = 0;
  string   OtherTargetOS;
  string   BuildNumber = 14;
  string   SerialNumber;
  string   CodeSet;
  string   IdentificationCode;
  string   LanguageEdition;
  string   Version = "8.02.00";
  string   Manufacturer = "Microsoft Corporation";
  boolean  PrimaryBIOS = True;
  string   CurrentLanguage = "en|US|iso8859-1";
  uint64   LoadedStartingAddress = 0xE0000;
  uint64   LoadedEndingAddress = 0xFFFFF;
  string   LoadUtilityInformation;
  uint8    EmbeddedControllerFirmwareMinorRelease = 255;
  uint8    EmbeddedControllerFirmwareMajorRelease = 255;
  uint8    SystemBIOSMinorRelease = 2;
  uint8    SystemBIOSMajorRelease = 8;
  string   StatusDescriptions[] = "OK";
  string   ListOfLanguages[] = "en|US|iso8859-1";
  datetime ReleaseDate;
  string   BIOSGUID;
  string   BIOSSerialNumber;
  string   BaseBoardSerialNumber;
  string   ChassisSerialNumber;
  string   ChassisAssetTag;
  boolean  BIOSNumLock;
  uint16   BootOrder[];
};
```

## Members

The **Msvm\_BIOSElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_BIOSElement** class has these properties.

<dl> <dt>

**BaseBoardSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The serial number for the base board on the virtual system.

</dd> <dt>

**BIOSGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique identifier for the BIOS.

</dd> <dt>

**BIOSNumLock**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled state of the Num Lock in the BIOS.

</dd> <dt>

**BIOSSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The serial number for the BIOS.

</dd> <dt>

**BootOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**MAX**](https://msdn.microsoft.com/library/aa393650) (4)
</dt> </dl>

The order in which devices will be searched for a boot sector at startup.

</dd> <dt>

**BuildNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Software Component Information\|002.4")
</dt> </dl>

The internal identifier for this compilation of software element. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is always set to 14.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "BIOS".

</dd> <dt>

**ChassisAssetTag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Automatically populated by the BIOS when the virtual machine is created.

</dd> <dt>

**ChassisSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Automatically populated by the BIOS when the virtual machine is created.

</dd> <dt>

**CodeSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The code set used by the software element. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is set to **NULL**.

</dd> <dt>

**CurrentLanguage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_BIOSElement**](cim-bioselement.md).**ListOfLanguages**")
</dt> </dl>

The currently selected language for the BIOS. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to "en\|US\|iso8859-1".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Microsoft Virtual BIOS".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the element. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "BIOS".

</dd> <dt>

**EmbeddedControllerFirmwareMajorRelease**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The major release of the embedded controller firmware. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to 255.

</dd> <dt>

**EmbeddedControllerFirmwareMinorRelease**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The minor release of the embedded controller firmware. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to 255.

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 5 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and operates within normal operational parameters and without error.

</dd> </dl>

</dd> <dt>

**IdentificationCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|SubComponent Software\|001.6")
</dt> </dl>

The manufacturer's identifier for this software element. Often this will be a stock keeping unit (SKU) or a part number. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is set to **NULL**.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Automatically populated by the BIOS when the virtual machine is created. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**LanguageEdition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (32), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|SubComponent Software\|001.7")
</dt> </dl>

The language edition of this software element. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is set to **NULL**.

</dd> <dt>

**ListOfLanguages**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of installable languages for the BIOS. THIS property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to "en\|US\|iso8859-1".

</dd> <dt>

**LoadedEndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System BIOS\|001.6")
</dt> </dl>

The ending address of the memory which this BIOS occupies. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is set to 0xFFFFF.

</dd> <dt>

**LoadedStartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System BIOS\|001.5")
</dt> </dl>

The starting address of the memory which this BIOS occupies. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is set to 0xE0000.

</dd> <dt>

**LoadUtilityInformation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System BIOS\|001.7")
</dt> </dl>

A free-form string that describes the BIOS flash/load utility that is required to update the BIOS element. Version and other information may be indicated in this property. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is set to **NULL**.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System BIOS\|001.2")
</dt> </dl>

The manufacturer of this BIOS. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to "Microsoft Corporation".

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name used to identify this software element. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is always set to "BIOS".

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

The current status of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 2 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> </dl>

</dd> <dt>

**OtherTargetOS**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_OperatingSystem**](https://msdn.microsoft.com/library/aa387937).**OtherTypeDescription**")
</dt> </dl>

The manufacturer and operating system for a software element when the **TargetOperatingSystem** property has a value of 1 (Other), which requires the **OtherTargetOS** property to have a non-**NULL** value. For all other values of **TargetOperatingSystem**, the **OtherTargetOS** property must be **NULL**. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is set to **NULL**.

</dd> <dt>

**PrimaryBIOS**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System BIOS\|001.9")
</dt> </dl>

If True, this is the primary BIOS of the computer system. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is set to **True**.

</dd> <dt>

**ReleaseDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System BIOS\|001.8")
</dt> </dl>

The date that the BIOS was released.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.4")
</dt> </dl>

The assigned serial number of the BIOS. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467).

</dd> <dt>

**SoftwareElementID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

An identifier for the software element. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is always set to "Microsoft:*GUID*\\*device-specific data*".

</dd> <dt>

**SoftwareElementState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The state of a software element's life cycle. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is always set to 2 (Executable).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) but it is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Strings that describes the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "OK".

</dd> <dt>

**SystemBIOSMajorRelease**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The major release of the system BIOS. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to 8.

</dd> <dt>

**SystemBIOSMinorRelease**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The minor release of the system BIOS. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to 2.

</dd> <dt>

**TargetOperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|SubComponent Software\|001.8"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_OperatingSystem**](https://msdn.microsoft.com/library/aa387937).**OSType**")
</dt> </dl>

The element's operating system environment. This property is inherited from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) and it is always set to 0 (Unknown).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System BIOS\|001.3")
</dt> </dl>

The version of the BIOS. This property is inherited from [**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191) and it is always set to "8.02.00".

</dd> </dl>

## Remarks

Access to the **Msvm\_BIOSElement** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_BIOSElement**](cim-bioselement.md)
</dt> <dt>

[BIOS Classes](bios-classes.md)
</dt> <dt>

[**CIM\_BIOSElement**](https://msdn.microsoft.com/library/aa387191)
</dt> </dl>

 

 





