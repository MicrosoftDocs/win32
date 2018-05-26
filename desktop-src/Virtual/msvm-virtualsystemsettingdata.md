---
title: Msvm\_VirtualSystemSettingData class
description: Represents the virtualization-specific settings for a virtual system.
ms.assetid: 05989377-ebaf-41b1-b268-17f4352c0ee5
keywords:
- Msvm_VirtualSystemSettingData class Hyper-V
- Msvm_VirtualSystemSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemSettingData
- Msvm_VirtualSystemSettingData.Caption
- Msvm_VirtualSystemSettingData.Description
- Msvm_VirtualSystemSettingData.SettingType
- Msvm_VirtualSystemSettingData.SystemName
- Msvm_VirtualSystemSettingData.InstanceID
- Msvm_VirtualSystemSettingData.ElementName
- Msvm_VirtualSystemSettingData.AutoActivate
- Msvm_VirtualSystemSettingData.OtherVirtualSystemType
- Msvm_VirtualSystemSettingData.CreationTime
- Msvm_VirtualSystemSettingData.VirtualSystemType
- Msvm_VirtualSystemSettingData.Notes
- Msvm_VirtualSystemSettingData.BIOSGUID
- Msvm_VirtualSystemSettingData.BIOSSerialNumber
- Msvm_VirtualSystemSettingData.BaseBoardSerialNumber
- Msvm_VirtualSystemSettingData.ChassisSerialNumber
- Msvm_VirtualSystemSettingData.ChassisAssetTag
- Msvm_VirtualSystemSettingData.BIOSNumLock
- Msvm_VirtualSystemSettingData.BootOrder
- Msvm_VirtualSystemSettingData.Parent
- Msvm_VirtualSystemSettingData.NumaNodeList
- Msvm_VirtualSystemSettingData.NumaNodesAreRequired
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_VirtualSystemSettingData class

Represents the virtualization-specific settings for a virtual system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemSettingData : CIM_VirtualSystemSettingData
{
  string   Caption = "Virtual Machine";
  string   Description;
  uint16   SettingType;
  string   SystemName = "GUID";
  string   InstanceID = "Microsoft:GUID";
  string   ElementName;
  boolean  AutoActivate;
  string   OtherVirtualSystemType;
  datetime CreationTime;
  uint16   VirtualSystemType = 301;
  string   Notes;
  string   BIOSGUID;
  string   BIOSSerialNumber;
  string   BaseBoardSerialNumber;
  string   ChassisSerialNumber;
  string   ChassisAssetTag;
  boolean  BIOSNumLock;
  uint16   BootOrder[];
  string   Parent;
  uint16   NumaNodeList[];
  boolean  NumaNodesAreRequired;
};
```

## Members

The **Msvm\_VirtualSystemSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemSettingData** class has these properties.

<dl> <dt>

**AutoActivate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the virtual system is automatically started when the virtualization platform is started. This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and is set to **NULL**.

</dd> <dt>

**BaseBoardSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the base board for the virtual computer system.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**BIOSGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The globally unique identifier for the BIOS of the virtual computer system.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**BIOSNumLock**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is set to **TRUE** if the num lock key is set to on by the BIOS, **FALSE** if the num lock key is set to off by the BIOS.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**BIOSSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the BIOS for the virtual computer system.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**BootOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**MAX**](https://msdn.microsoft.com/library/aa393650) (4)
</dt> </dl>

The boot order set within the BIOS of the virtual computer system. This property is an array of values, **BootOrder**\[0\] through **BootOrder**\[3\], inclusive, where each value indicates a device to boot from. Each of the 4 values in the array must be set and must not be the same as another value in the array. The virtual computer system will first attempt to boot from the device indicated by the first value within the array. If that device does not contain a boot sector, the virtual computer system will attempt to boot from the next device specified by the **BootOrder** property and so on. If no device specified within the **BootOrder** contains a boot sector the virtual computer system will fail to boot. The default value for a virtual computer system is \[0, 1, 2, 3\].

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

<dt>

<span id="Floppy"></span><span id="floppy"></span><span id="FLOPPY"></span>

<span id="Floppy"></span><span id="floppy"></span><span id="FLOPPY"></span>**Floppy** (0)


</dt> <dd>

The virtual computer system will attempt to boot from the floppy disk within the floppy drive.

</dd> <dt>

<span id="CD-ROM"></span><span id="cd-rom"></span>

<span id="CD-ROM"></span><span id="cd-rom"></span>**CD-ROM** (1)


</dt> <dd>

The virtual computer system will attempt to boot from the first CD or DVD disk found with a boot sector.

</dd> <dt>

<span id="ID_Hard_Drive"></span><span id="id_hard_drive"></span><span id="ID_HARD_DRIVE"></span>

<span id="ID_Hard_Drive"></span><span id="id_hard_drive"></span><span id="ID_HARD_DRIVE"></span>**ID Hard Drive** (2)


</dt> <dd>

The virtual computer system will attempt to boot from the first hard disk drive found with a boot sector.

</dd> <dt>

<span id="PXE_Boot"></span><span id="pxe_boot"></span><span id="PXE_BOOT"></span>

<span id="PXE_Boot"></span><span id="pxe_boot"></span><span id="PXE_BOOT"></span>**PXE Boot** (3)


</dt> <dd>

The virtual computer system will attempt to PXE boot from the network.

</dd> <dt>

<span id="SCSI_Hard_Drive"></span><span id="scsi_hard_drive"></span><span id="SCSI_HARD_DRIVE"></span>

<span id="SCSI_Hard_Drive"></span><span id="scsi_hard_drive"></span><span id="SCSI_HARD_DRIVE"></span>**SCSI Hard Drive** (4)


</dt> <dd></dd> <dt>

4 65535
</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Virtual Machine".

</dd> <dt>

**ChassisAssetTag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The asset tag of the chassis for the virtual computer system.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**ChassisSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the chassis for the virtual computer system.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time at which the settings for the virtual system were created. If this object represents the current settings for the virtual system, this value would be the time at which the system was created. If this object represents the snapshot settings for the virtual system, this value would be the time at which the snapshot was taken. This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954).

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Active settings for the virtual machine" if not referring to a snapshot. If referring to a snapshot, it is set to "Snapshot settings for the virtual machine".

"Active settings for the virtual machine"

"Snapshot settings for the virtual machine"

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to the display name for the machine. This name may not exceed 100 characters in length. Changing this property will change the **ElementName** of the associated LogicalDevice derivative.

This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the **Msvm\_VirtualSystemManagementService** class.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to "Microsoft:*GUID*".

</dd> <dt>

**Notes**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A free-form string containing notes for the system.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**NumaNodeList**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

For non-uniform memory access (NUMA)-capable systems, this is the list of NUMA nodes on which the virtual machine is to be run.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**NumaNodesAreRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value")
</dt> </dl>

For non-uniform memory access (NUMA)-capable systems, this value indicates whether the nodes specified in **NumaNodeList** are required or preferred. If this value is **TRUE** (the nodes are required), the virtual machine will fail to start if there are not enough resources available on the specified NUMA nodes.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**OtherVirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).**VirtualSystemType**")
</dt> </dl>

This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) but it is not implemented.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this instance does not represent a system based on a snapshot of a virtual system, this property is **NULL**. Otherwise, the property holds the object path of the **Msvm\_VirtualSystemSettingData** object on which this instance is based. When building a snapshot tree hierarchy for the virtual machine, this property references the object from which the current instance is derived (the current instance is the child node and the object referenced in this property is the parent node.)

</dd> <dt>

**SettingType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The usage context for this instance of **Msvm\_VirtualSystemSettingData**. This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954).

<dt>

<span id="Input"></span><span id="input"></span><span id="INPUT"></span>

<span id="Input"></span><span id="input"></span><span id="INPUT"></span>**Input** (1)


</dt> <dd></dd> <dt>

<span id="Recorded"></span><span id="recorded"></span><span id="RECORDED"></span>

<span id="Recorded"></span><span id="recorded"></span><span id="RECORDED"></span>**Recorded** (2)


</dt> <dd></dd> <dt>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>**Current** (3)


</dt> <dd>

This instance represents the current settings for the virtual system.

</dd> <dt>

<span id="Capability"></span><span id="capability"></span><span id="CAPABILITY"></span>

<span id="Capability"></span><span id="capability"></span><span id="CAPABILITY"></span>**Capability** (4)


</dt> <dd></dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>**Snapshot** (5)


</dt> <dd>

This instance represents the settings for a snapshot of the virtual system.

</dd> </dl>

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The label by which the object is known. This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to "*GUID*". This corresponds to the **Name** property of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class and the **SystemName** property of the [**Msvm\_VirtualSystemGlobalSettingData**](msvm-virtualsystemglobalsettingdata.md) class.

</dd> <dt>

**VirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).**OtherVirtualSystemType**")
</dt> </dl>

The virtual system type. This value is set to 301 (Microsoft Hyper-V). This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954).

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 





