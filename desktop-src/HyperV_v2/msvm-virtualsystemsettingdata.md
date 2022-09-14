---
description: Represents the virtualization-specific settings for a virtual machine.
ms.assetid: BE81405E-E773-41CE-9441-33D60B63550E
title: Msvm_VirtualSystemSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemSettingData
- Msvm_VirtualSystemSettingData.InstanceID
- Msvm_VirtualSystemSettingData.Caption
- Msvm_VirtualSystemSettingData.Description
- Msvm_VirtualSystemSettingData.ElementName
- Msvm_VirtualSystemSettingData.VirtualSystemIdentifier
- Msvm_VirtualSystemSettingData.VirtualSystemType
- Msvm_VirtualSystemSettingData.Notes
- Msvm_VirtualSystemSettingData.CreationTime
- Msvm_VirtualSystemSettingData.ConfigurationID
- Msvm_VirtualSystemSettingData.ConfigurationDataRoot
- Msvm_VirtualSystemSettingData.ConfigurationFile
- Msvm_VirtualSystemSettingData.SnapshotDataRoot
- Msvm_VirtualSystemSettingData.SuspendDataRoot
- Msvm_VirtualSystemSettingData.SwapFileDataRoot
- Msvm_VirtualSystemSettingData.LogDataRoot
- Msvm_VirtualSystemSettingData.AutomaticStartupAction
- Msvm_VirtualSystemSettingData.AutomaticStartupActionDelay
- Msvm_VirtualSystemSettingData.AutomaticStartupActionSequenceNumber
- Msvm_VirtualSystemSettingData.AutomaticShutdownAction
- Msvm_VirtualSystemSettingData.AutomaticRecoveryAction
- Msvm_VirtualSystemSettingData.RecoveryFile
- Msvm_VirtualSystemSettingData.BIOSGUID
- Msvm_VirtualSystemSettingData.BIOSSerialNumber
- Msvm_VirtualSystemSettingData.BaseBoardSerialNumber
- Msvm_VirtualSystemSettingData.ChassisSerialNumber
- Msvm_VirtualSystemSettingData.Architecture
- Msvm_VirtualSystemSettingData.ChassisAssetTag
- Msvm_VirtualSystemSettingData.BIOSNumLock
- Msvm_VirtualSystemSettingData.BootOrder
- Msvm_VirtualSystemSettingData.Parent
- Msvm_VirtualSystemSettingData.UserSnapshotType
- Msvm_VirtualSystemSettingData.IsSaved
- Msvm_VirtualSystemSettingData.AdditionalRecoveryInformation
- Msvm_VirtualSystemSettingData.AllowFullSCSICommandSet
- Msvm_VirtualSystemSettingData.DebugChannelId
- Msvm_VirtualSystemSettingData.DebugPortEnabled
- Msvm_VirtualSystemSettingData.DebugPort
- Msvm_VirtualSystemSettingData.Version
- Msvm_VirtualSystemSettingData.IncrementalBackupEnabled
- Msvm_VirtualSystemSettingData.VirtualNumaEnabled
- Msvm_VirtualSystemSettingData.AllowReducedFcRedundancy
- Msvm_VirtualSystemSettingData.VirtualSystemSubType
- Msvm_VirtualSystemSettingData.BootSourceOrder
- Msvm_VirtualSystemSettingData.PauseAfterBootFailure
- Msvm_VirtualSystemSettingData.NetworkBootPreferredProtocol
- Msvm_VirtualSystemSettingData.GuestControlledCacheTypes
- Msvm_VirtualSystemSettingData.AutomaticSnapshotsEnabled
- Msvm_VirtualSystemSettingData.IsAutomaticSnapshot
- Msvm_VirtualSystemSettingData.GuestStateFile
- Msvm_VirtualSystemSettingData.GuestStateDataRoot
- Msvm_VirtualSystemSettingData.LockOnDisconnect
- Msvm_VirtualSystemSettingData.ParentPackage
- Msvm_VirtualSystemSettingData.AutomaticCriticalErrorActionTimeout
- Msvm_VirtualSystemSettingData.AutomaticCriticalErrorAction
- Msvm_VirtualSystemSettingData.ConsoleMode
- Msvm_VirtualSystemSettingData.SecureBootEnabled
- Msvm_VirtualSystemSettingData.SecureBootTemplateId
- Msvm_VirtualSystemSettingData.LowMmioGapSize
- Msvm_VirtualSystemSettingData.HighMmioGapSize
- Msvm_VirtualSystemSettingData.EnhancedSessionTransportType
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualSystemSettingData class

Represents the virtualization-specific settings for a virtual machine.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemSettingData : CIM_VirtualSystemSettingData
{
  string   InstanceID;
  string   Caption = "Virtual Machine Settings";
  string   Description;
  string   ElementName;
  string   VirtualSystemIdentifier;
  string   VirtualSystemType;
  string   Notes[];
  datetime CreationTime;
  string   ConfigurationID;
  string   ConfigurationDataRoot;
  string   ConfigurationFile;
  string   SnapshotDataRoot;
  string   SuspendDataRoot;
  string   SwapFileDataRoot;
  string   LogDataRoot;
  uint16   AutomaticStartupAction;
  datetime AutomaticStartupActionDelay;
  uint16   AutomaticStartupActionSequenceNumber;
  uint16   AutomaticShutdownAction;
  uint16   AutomaticRecoveryAction;
  string   RecoveryFile;
  string   BIOSGUID;
  string   BIOSSerialNumber;
  string   BaseBoardSerialNumber;
  string   ChassisSerialNumber;
  string   Architecture;
  string   ChassisAssetTag;
  boolean  BIOSNumLock;
  uint16   BootOrder[];
  string   Parent;
  uint16   UserSnapshotType;
  boolean  IsSaved;
  string   AdditionalRecoveryInformation;
  boolean  AllowFullSCSICommandSet;
  uint32   DebugChannelId;
  uint16   DebugPortEnabled;
  uint32   DebugPort;
  string   Version;
  boolean  IncrementalBackupEnabled;
  boolean  VirtualNumaEnabled;
  boolean  AllowReducedFcRedundancy = False;
  string   VirtualSystemSubType;
  string   BootSourceOrder[];
  boolean  PauseAfterBootFailure;
  uint16   NetworkBootPreferredProtocol;
  boolean  GuestControlledCacheTypes;
  boolean  AutomaticSnapshotsEnabled;
  boolean  IsAutomaticSnapshot;
  string   GuestStateFile;
  string   GuestStateDataRoot;
  boolean  LockOnDisconnect;
  string   ParentPackage;
  datetime AutomaticCriticalErrorActionTimeout;
  uint16   AutomaticCriticalErrorAction;
  uint16   ConsoleMode;
  boolean  SecureBootEnabled;
  string   SecureBootTemplateId;
  uint64   LowMmioGapSize;
  uint64   HighMmioGapSize;
  uint16   EnhancedSessionTransportType;
};
```

## Members

The **Msvm\_VirtualSystemSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemSettingData** class has these properties.

<dl> <dt>

**AdditionalRecoveryInformation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Any additional information provided to the recovery action. The meaning of this property is defined by the action in **AutomaticRecoveryAction**. If **AutomaticRecoveryAction** is 0 ("None") or 1 ("Restart"), this value is **Null**. If **AutomaticRecoveryAction** is 2 ("Revert to Snapshot"), this is the object path to a snapshot that should be applied on failure of the virtual machine worker process.

</dd> <dt>

**AllowFullSCSICommandSet**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if SCSI commands from the guest operating system are passed to pass-through disks; otherwise, **False**. If **True**, SCSI commands emitted by the guest operating system to pass-through disks are not filtered. We recommend that SCSI filtering remain enabled for production deployments.

</dd> <dt>

**AllowReducedFcRedundancy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether live migration of a virtual machine that is configured with a virtual Fibre Channel adapter is allowed to a destination computer that may have no or reduced paths to the target Fibre Channel devices. This property should be cleared after a live migration.



| Value                                                                            | Meaning                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>False</dt> </dl> | The virtual machine cannot be live migrated to a target computer that may have no or reduced paths to the target Fibre Channel devices.<br/>                                                                                                     |
| <dl> <dt>True</dt> </dl>  | The virtual machine can be live migrated to a target computer that may have no or reduced paths to the target Fibre Channel devices. The guest operating system may lose connectivity to storage and may behave in an unpredictable manner.<br/> |



 

</dd> <dt>

**Architecture**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The architecture of this system.

> [!Note]  
> Added in Windows 10, version 1709.

 

<dt>

<span id="x64"></span><span id="X64"></span>

**x64** ()


</dt> <dd></dd> <dt>

<span id="arm64"></span><span id="ARM64"></span>

**arm64** ()


</dt> <dd></dd> </dl>

</dd> <dt>

**AutomaticCriticalErrorAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifies the action to be taken on VM, when a critical error happens, like storage disconnect.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

No specific action will be taken for critical error conditions.

</dd> <dt>

<span id="Pause_Resume"></span><span id="pause_resume"></span><span id="PAUSE_RESUME"></span>

<span id="Pause_Resume"></span><span id="pause_resume"></span><span id="PAUSE_RESUME"></span>**Pause Resume** (1)


</dt> <dd>

Causes the VM to be paused and automatically resumed when the critical error condition is resolved.

</dd> </dl>

</dd> <dt>

**AutomaticCriticalErrorActionTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**SubType**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("interval")
</dt> </dl>

Identifies the maximum duration for which the **AutomaticCriticalErrorAction** will be performed to resolve the critical error. This is applicable only when the value of the **AutomaticCriticalErrorAction** property is not 0 (None). Once the timeout expires, the VM will be powered off. The value will be rounded up to the nearest minute. A value of 0 implies that the VM should be powered off immediately when it encounters a critical error condition.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

**AutomaticRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Action to take for the virtual machine when the software executed by the virtual machine fails. Failures in this case means a failure that is detectable by the host platform, such as a noninterruptible wait state condition. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

This can be one of the following values.



| Value                                                                               | Meaning                        |
|-------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>2</dt> </dl>        | None.<br/>               |
| <dl> <dt>3</dt> </dl>        | Restart.<br/>            |
| <dl> <dt>4</dt> </dl>        | Revert to snapshot.<br/> |
| <dl> <dt>5..32768</dt> </dl> | Reserved.<br/>           |



 

</dd> <dt>

**AutomaticShutdownAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Action to take for the virtual machine when the host is shut down. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

This can be one of the following values.



| Value                                                                               | Meaning                |
|-------------------------------------------------------------------------------------|------------------------|
| <dl> <dt>2</dt> </dl>        | Turn off.<br/>   |
| <dl> <dt>3</dt> </dl>        | Save state.<br/> |
| <dl> <dt>4</dt> </dl>        | Shutdown.<br/>   |
| <dl> <dt>5..32768</dt> </dl> | Reserved.<br/>   |



 

</dd> <dt>

**AutomaticSnapshotsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether this virtual machine should have automatic snapshots enabled.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**AutomaticStartupAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Action to take for the virtual machine when the host is started. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

This can be one of the following values.



| Value                                                                               | Meaning                                  |
|-------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>2</dt> </dl>        | None.<br/>                         |
| <dl> <dt>3</dt> </dl>        | Restart if previously active.<br/> |
| <dl> <dt>4</dt> </dl>        | Always start.<br/>                 |
| <dl> <dt>5..32768</dt> </dl> | Reserved.<br/>                     |



 

</dd> <dt>

**AutomaticStartupActionDelay**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The delay time before the virtual machine is automatically started up. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**AutomaticStartupActionSequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A number that indicates the relative sequence of virtual machine activation when the host system is started. A lower number indicates earlier activation. If one or more configurations show the same value, the sequence is implementation dependent. A value of 0 indicates that the sequence is implementation dependent. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**BaseBoardSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the base board for the virtual machine.

</dd> <dt>

**BIOSGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The globally unique identifier for the BIOS of the virtual machine.

</dd> <dt>

**BIOSNumLock**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if the num lock key is set to on by the BIOS; **False** if the num lock key is set to off by the BIOS.

</dd> <dt>

**BIOSSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the BIOS for the virtual machine.

</dd> <dt>

**BootOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**MAX**](/windows/desktop/WmiSdk/standard-qualifiers) (4)
</dt> </dl>

The boot order set within the BIOS of the virtual machine. This property is an array of values, **BootOrder**\[0\] through **BootOrder**\[3\], inclusive, where each value indicates a device to boot from. Each of the 4 values in the array must be set and must not be the same as another value in the array. The virtual machine will first attempt to boot from the device indicated by the first value within the array. If that device does not contain a boot sector, the virtual machine will attempt to boot from the next device specified by the **BootOrder** property and so on. If no device specified within the **BootOrder** contains a boot sector the virtual machine will fail to boot. The default value for a virtual machine is \[0, 1, 2, 3\].

<dt>

<span id="Floppy"></span><span id="floppy"></span><span id="FLOPPY"></span>

<span id="Floppy"></span><span id="floppy"></span><span id="FLOPPY"></span>**Floppy** (0)


</dt> <dd>

The virtual machine will attempt to boot from the floppy disk within the floppy drive.

</dd> <dt>

<span id="CD-ROM"></span><span id="cd-rom"></span>

<span id="CD-ROM"></span><span id="cd-rom"></span>**CD-ROM** (1)


</dt> <dd>

The virtual machine will attempt to boot from the first CD or DVD disk found with a boot sector.

</dd> <dt>

<span id="IDE_Hard_Drive"></span><span id="ide_hard_drive"></span><span id="IDE_HARD_DRIVE"></span>

<span id="IDE_Hard_Drive"></span><span id="ide_hard_drive"></span><span id="IDE_HARD_DRIVE"></span>**IDE Hard Drive** (2)


</dt> <dd>

The virtual machine will attempt to boot from the first hard disk drive found with a boot sector.

</dd> <dt>

<span id="PXE_Boot"></span><span id="pxe_boot"></span><span id="PXE_BOOT"></span>

<span id="PXE_Boot"></span><span id="pxe_boot"></span><span id="PXE_BOOT"></span>**PXE Boot** (3)


</dt> <dd>

The virtual machine will attempt to PXE boot from the network.

</dd> <dt>

<span id="SCSI_Hard_Drive"></span><span id="scsi_hard_drive"></span><span id="SCSI_HARD_DRIVE"></span>

<span id="SCSI_Hard_Drive"></span><span id="scsi_hard_drive"></span><span id="SCSI_HARD_DRIVE"></span>**SCSI Hard Drive** (4)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>**Reserved** (5..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**BootSourceOrder**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The boot source order for the virtual machine.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**ChassisAssetTag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The asset tag of the chassis for the virtual machine.

</dd> <dt>

**ChassisSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the chassis for the virtual machine.

</dd> <dt>

**ConfigurationDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where information about the virtual machine configuration is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**ConfigurationFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path and file name of a file where information about the virtual machine configuration is stored. This path is relative to the **ConfigurationDataRoot** property. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**ConfigurationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique identifier of the virtual machine configuration. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**ConsoleMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifies the Console Mode for the VM.

> [!Note]  
> This property was added in Windows 10 and Windows Server 2016.

 

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

**Default** (0)


</dt> <dd></dd> <dt>

<span id="COM1"></span><span id="com1"></span>

**COM1** (1)


</dt> <dd></dd> <dt>

<span id="COM2"></span><span id="com2"></span>

**COM2** (2)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time at which the settings for the virtual machine were created. If this object represents the current settings for the virtual machine, this value would be the time at which the system was created. If this object represents the snapshot settings for the virtual machine, this value would be the time at which the snapshot was taken. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**DebugChannelId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The channel identifier used to debug the virtual machine using the unified debugger.

</dd> <dt>

**DebugPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The TCP/IP port used to debug the virtual machine using synthetic debugging.

</dd> <dt>

**DebugPortEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the virtual machine is using synthetic debugging. This can be one of the following values.

<dt>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>**Off** (0)


</dt> <dd></dd> <dt>

<span id="On"></span><span id="on"></span><span id="ON"></span>

<span id="On"></span><span id="on"></span><span id="ON"></span>**On** (1)


</dt> <dd></dd> <dt>

<span id="OnAutoAssigned"></span><span id="onautoassigned"></span><span id="ONAUTOASSIGNED"></span>

<span id="OnAutoAssigned"></span><span id="onautoassigned"></span><span id="ONAUTOASSIGNED"></span>**OnAutoAssigned** (2)


</dt> <dd>

Auto-assigned

</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to one of the following values.



| Value                                                                                                                  | Meaning                                               |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>"Active settings for the virtual machine"</dt> </dl>   | This instance refers to a virtual machine.<br/> |
| <dl> <dt>"Snapshot settings for the virtual machine"</dt> </dl> | This instance refers to a snapshot.<br/>        |



 

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), and it is always set to the display name for the machine. This name may not exceed 100 characters in length.

</dd> <dt>

**EnhancedSessionTransportType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the transport type to use when connecting to an enhanced session.

> [!Note]  
> This property was added in Windows 10, version 1803.

 

<dt>

<span id="VMBus_Pipe"></span><span id="vmbus_pipe"></span><span id="VMBUS_PIPE"></span>

**VMBus Pipe** (0)


</dt> <dd></dd> <dt>

<span id="Hyper-V_Socket"></span><span id="hyper-v_socket"></span><span id="HYPER-V_SOCKET"></span>

**Hyper-V Socket** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**GuestControlledCacheTypes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the guest can control cache types.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

**GuestStateDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Filepath of a directory where information about the guest runtime state is stored.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**GuestStateFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Filepath of a file where information about the guest runtime state is stored. A relative path appends to the value of the **GuestStateDataRoot** property.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**HighMmioGapSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The size of the High (above 4GB) Memory-Mapped IO Gap in MB

> [!Note]  
> This property was added in Windows 10, version 1703.

 

</dd> <dt>

**IncrementalBackupEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the Hyper-V VSS writer supports taking incremental backups of this virtual machine.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)).

</dd> <dt>

**IsAutomaticSnapshot**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this is a snapshot created automatically for the user.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**IsSaved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the configuration has a reference to a saved state file; otherwise, **False**. This does not indicate the presence of such a file, only that the configuration specifies one.

</dd> <dt>

**LockOnDisconnect**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lock the console when disconnecting from vmconnect.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

**LogDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where log information for the virtual machine is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**LowMmioGapSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Configures the size, in megabytes, of the first MMIO gap for a virtual machine (VM).

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

Range: 128 3584

</dd> <dt>

**NetworkBootPreferredProtocol**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines if the preferred protocol for PXE boot is IPv4 or IPv6.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

<dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

**IPv4** (4096)


</dt> <dd></dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

**IPv6** (4097)


</dt> <dd></dd> </dl>

</dd> <dt>

**Notes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

User supplied notes that are related to the virtual machine. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this instance does not represent a system based on a snapshot of a virtual machine, this property is **Null**. Otherwise, the property holds the object path of the **Msvm\_VirtualSystemSettingData** object on which this instance is based. When building a snapshot tree hierarchy for the virtual machine, this property references the object from which the current instance is derived (the current instance is the child node and the object referenced in this property is the parent node.)

</dd> <dt>

**ParentPackage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If this system is a container, the path to the Msvm\_ContainerPackage from which this system is based.

> [!Note]  
> Added in Windows 10; removed in Windows 10, version 1703.

 

</dd> <dt>

**PauseAfterBootFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the BIOS pauses after every boot entry failure waiting for the user to press a key. **True** if the BIOS pauses; otherwise, **False**.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**RecoveryFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The full path of a file where recovery related information for the virtual machine is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**SecureBootEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether secure boot is enabled for the virtual machine (VM). **True** if enabled; otherwise, **False**.

> [!Note]  
> Secure boot can only be enabled for generation 2 VMs.

 

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**SecureBootTemplateId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The globally-unique identifier of the template of intial values of UEFI Secure Boot related variables.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](https://www.bing.com/search?q=**ModifyVirtualSystem**) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

**SnapshotDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where information about the virtual machine snapshots is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**SuspendDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where information about the virtual machine suspend-related information is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**SwapFileDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where swap files for the virtual machine are stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**UserSnapshotType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the user-defined snapshot type.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

<dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>**Disable** (2)


</dt> <dd>

Disable the creation of any snapshot.

</dd> <dt>

<span id="ProductionFallbackToTest"></span><span id="productionfallbacktotest"></span><span id="PRODUCTIONFALLBACKTOTEST"></span>

<span id="ProductionFallbackToTest"></span><span id="productionfallbacktotest"></span><span id="PRODUCTIONFALLBACKTOTEST"></span>**ProductionFallbackToTest** (3)


</dt> <dd>

Data-consistent snapshot for use in the production environment.Performs a snapshot with application state when the ability to create data consistent snapshot is not available.

</dd> <dt>

<span id="ProductionNoFallback"></span><span id="productionnofallback"></span><span id="PRODUCTIONNOFALLBACK"></span>

<span id="ProductionNoFallback"></span><span id="productionnofallback"></span><span id="PRODUCTIONNOFALLBACK"></span>**ProductionNoFallback** (4)


</dt> <dd>

Data-consistent snapshot for use in the production environment.Does not create a snapshot with application state if it is not possible to create a data consistent snapshot.

</dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>**Test** (5)


</dt> <dd>

Snapshot that contains memory and device information for test and development purpose.

</dd> </dl>

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the virtual machine in a format of "major.minor", for example "2.0".

</dd> <dt>

**VirtualNumaEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**Msvm\_ProcessorSettingData**](msvm-processorsettingdata.md).**MaxProcessorsPerNumaNode**", "[**Msvm\_MemorySettingData**](msvm-memorysettingdata.md).**MaxMemoryBlocksPerNumaNode**")
</dt> </dl>

**True** if virtual non-uniform memory access (NUMA) nodes are projected into the virtual machine; **False** if the virtual machine will have a single node. If **True**, the number of virtual NUMA nodes projected into the virtual machine is determined from the values of the [**Msvm\_ProcessorSettingData.MaxProcessorsPerNumaNode**](msvm-processorsettingdata.md) and [**Msvm\_MemorySettingData.MaxMemoryBlocksPerNumaNode**](msvm-memorysettingdata.md) properties.

</dd> <dt>

**VirtualSystemIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\_VirtualSystemSettingData.VirtualSystemIdentifier"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**Name**")
</dt> </dl>

The name of the [**CIM\_ComputerSystem**](/windows/desktop/CIMWin32Prov/cim-computersystem) object to which this setting data belongs. This property is an override from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**VirtualSystemSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The valid values for this property are Microsoft:Hyper-V:SubType:1 and Microsoft:Hyper-V:SubType:2. A  Generation 1  VM is subtype 1. A  Generation 2  VM is subtype 2.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

<dt>

<span id="Microsoft_Hyper-V_SubType_1"></span><span id="microsoft_hyper-v_subtype_1"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_1"></span>

**Microsoft:Hyper-V:SubType:1** ("Microsoft:Hyper-V:SubType:1")


</dt> <dd></dd> <dt>

<span id="Microsoft_Hyper-V_SubType_2"></span><span id="microsoft_hyper-v_subtype_2"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_2"></span>

**Microsoft:Hyper-V:SubType:2** ("Microsoft:Hyper-V:SubType:2")


</dt> <dd></dd> </dl>

</dd> <dt>

**VirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of virtual machine the setting data represents. This property is inherited from the [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)) class. This will be one of the following values.



| Value                                                                                                                                 | Meaning                                              |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>"Microsoft:Hyper-V:System:Realized"</dt> </dl>                        | A realized virtual machine.<br/>               |
| <dl> <dt>"Microsoft:Hyper-V:System:Planned"</dt> </dl>                         | A planned virtual machine.<br/>                |
| <dl> <dt>"Microsoft:Hyper-V:Snapshot:Realized"</dt> </dl>                      | A snapshot of a realized virtual machine.<br/> |
| <dl> <dt>"Microsoft:Hyper-V:Snapshot:Recovery"</dt> </dl>                      | A snapshot of a recovery virtual machine.<br/> |
| <dl> <dt>"Microsoft:Hyper-V:Snapshot:Planned"</dt> </dl>                       | A snapshot of a planned virtual machine.<br/>  |
| <dl> <dt>"Microsoft:Hyper-V:Snapshot:Missing"</dt> </dl>                       | A missing snapshot.<br/>                       |
| <dl> <dt>"Microsoft:Hyper-V:Snapshot:Replica:Standard"</dt> </dl>              | A time-based replication point snapshot.<br/>  |
| <dl> <dt>"Microsoft:Hyper-V:Snapshot:Replica:ApplicationConsistent"</dt> </dl> | A VSS replication point snapshot.<br/>         |
| <dl> <dt>"Microsoft:Hyper-V:Snapshot:Replica:PlannedFailover"</dt> </dl>       | A planned replication snapshot.<br/>           |



 

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85))
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

