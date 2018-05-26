---
title: Msvm\_VirtualSystemSettingData class
description: Represents the virtualization-specific settings for a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dd2c692d-a3bc-45fd-8589-d68abcdfffa2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_VirtualSystemSettingData class
- Msvm_VirtualSystemSettingData class, described
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemSettingData
- Msvm_VirtualSystemSettingData.Caption
- Msvm_VirtualSystemSettingData.Description
- Msvm_VirtualSystemSettingData.InstanceID
- Msvm_VirtualSystemSettingData.ElementName
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
- Msvm_VirtualSystemSettingData.ChassisAssetTag
- Msvm_VirtualSystemSettingData.BIOSNumLock
- Msvm_VirtualSystemSettingData.BootOrder
- Msvm_VirtualSystemSettingData.BootSourceOrder
- Msvm_VirtualSystemSettingData.Parent
- Msvm_VirtualSystemSettingData.UserSnapshotType
- Msvm_VirtualSystemSettingData.VirtualSystemIdentifier
- Msvm_VirtualSystemSettingData.IsSaved
- Msvm_VirtualSystemSettingData.AdditionalRecoveryInformation
- Msvm_VirtualSystemSettingData.AllowFullSCSICommandSet
- Msvm_VirtualSystemSettingData.DebugChannelId
- Msvm_VirtualSystemSettingData.DebugPortEnabled
- Msvm_VirtualSystemSettingData.DebugPort
- Msvm_VirtualSystemSettingData.Version
- Msvm_VirtualSystemSettingData.IncrementalBackupEnabled
- Msvm_VirtualSystemSettingData.VirtualNumaEnabled
- Msvm_VirtualSystemSettingData.LowMmioGapSize
- Msvm_VirtualSystemSettingData.HighMmioGapSize
- Msvm_VirtualSystemSettingData.AllowReducedFcRedundancy
- Msvm_VirtualSystemSettingData.VirtualSystemSubType
- Msvm_VirtualSystemSettingData.SecureBootEnabled
- Msvm_VirtualSystemSettingData.SecureBootTemplateId
- Msvm_VirtualSystemSettingData.PauseAfterBootFailure
- Msvm_VirtualSystemSettingData.NetworkBootPreferredProtocol
- Msvm_VirtualSystemSettingData.ConsoleMode
- Msvm_VirtualSystemSettingData.AutomaticCriticalErrorAction
- Msvm_VirtualSystemSettingData.AutomaticCriticalErrorActionTimeout
- Msvm_VirtualSystemSettingData.LockOnDisconnect
- Msvm_VirtualSystemSettingData.GuestControlledCacheTypes
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_VirtualSystemSettingData class

Represents the virtualization-specific settings for a virtual machine.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemSettingData : CIM_VirtualSystemSettingData
{
  string   Caption;
  string   Description;
  string   InstanceID;
  string   ElementName;
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
  string   ChassisAssetTag;
  boolean  BIOSNumLock;
  uint16   BootOrder[];
  string   BootSourceOrder[];
  string   Parent;
  uint16   UserSnapshotType;
  string   VirtualSystemIdentifier;
  boolean  IsSaved;
  string   AdditionalRecoveryInformation;
  boolean  AllowFullSCSICommandSet;
  uint32   DebugChannelId;
  uint16   DebugPortEnabled;
  uint32   DebugPort;
  string   Version;
  boolean  IncrementalBackupEnabled;
  boolean  VirtualNumaEnabled;
  uint64   LowMmioGapSize;
  uint64   HighMmioGapSize;
  boolean  AllowReducedFcRedundancy = False;
  string   VirtualSystemSubType;
  boolean  SecureBootEnabled;
  string   SecureBootTemplateId;
  boolean  PauseAfterBootFailure;
  uint16   NetworkBootPreferredProtocol;
  uint16   ConsoleMode;
  uint16   AutomaticCriticalErrorAction;
  datetime AutomaticCriticalErrorActionTimeout;
  boolean  LockOnDisconnect;
  boolean  GuestControlledCacheTypes;
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

Any additional information provided to the recovery action. The meaning of this property is defined by the action in **AutomaticRecoveryAction**. If **AutomaticRecoveryAction** is 0 ("None") or 1 ("Restart"), this value is **NULL**. If **AutomaticRecoveryAction** is 2 ("Revert to Snapshot"), this is the object path to a snapshot that should be applied on failure of the virtual machine worker process. This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](https://msdn.microsoft.com/library/cc136809) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**AllowFullSCSICommandSet**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Any additional information provided to the recovery action. The meaning of this property is defined by the action in **AutomaticRecoveryAction**. If **AutomaticRecoveryAction** is 0 ("None") or 1 ("Restart"), this value is **Null**. If **AutomaticRecoveryAction** is 2 ("Revert to Snapshot"), this is the object path to a snapshot that should be applied on failure of the virtual machine worker process.

</dd> <dt>

**AllowReducedFcRedundancy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether live migration of a virtual machine that is configured with a virtual Fibre Channel adapter is allowed to a destination computer that may have no or reduced paths to the target Fibre Channel devices. This property should be cleared after a live migration.

The possible values are:

<dt>

False
</dt> <dd>

The virtual machine cannot be live migrated to a target computer that may have no or reduced paths to the target Fibre Channel devices.

</dd> <dt>

True
</dt> <dd>

The virtual machine can be live migrated to a target computer that may have no or reduced paths to the target Fibre Channel devices. The guest operating system may lose connectivity to storage and may behave in an unpredictable manner.

</dd> </dl>

</dd> <dt>

**AutomaticCriticalErrorAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The action to take on the VM when a critical error happens, such as an error caused by disconnected storage.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

No action is taken.

</dd> <dt>

<span id="Pause_Resume"></span><span id="pause_resume"></span><span id="PAUSE_RESUME"></span>

<span id="Pause_Resume"></span><span id="pause_resume"></span><span id="PAUSE_RESUME"></span>**Pause Resume** (1)


</dt> <dd>

The VM is paused and automatically resumed when the critical error condition is resolved.

</dd> </dl>

</dd> <dt>

**AutomaticCriticalErrorActionTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**SubType**](https://msdn.microsoft.com/library/aa393651) ("interval")
</dt> </dl>

The maximum duration for which the action of the**AutomaticCriticalErrorAction** property is performed. This is only applicable when the value of **AutomaticCriticalErrorAction** is not "0" (None). Once the timeout expires, the VM is powered off. The value is rounded up to the nearest minute. A value of "0" implies that the VM should be powered off immediately when it encounters a critical error condition.

</dd> <dt>

**AutomaticRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The action to take for the virtual system when the software executed by the virtual system fails. The failures addressed by this property only include those that are detectable by the host platform, such as a non-interruptible wait state condition.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="Restart"></span><span id="restart"></span><span id="RESTART"></span>

**Restart** (3)


</dt> <dd></dd> <dt>

<span id="Revert_to_snapshot"></span><span id="revert_to_snapshot"></span><span id="REVERT_TO_SNAPSHOT"></span>

**Revert to snapshot** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 65535</dd> </dl>

</dd> <dt>

**AutomaticShutdownAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The action to take for the virtual system when the host is shut down.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

<dt>

<span id="Turn_Off"></span><span id="turn_off"></span><span id="TURN_OFF"></span>

**Turn Off** (2)


</dt> <dd></dd> <dt>

<span id="Save_state"></span><span id="save_state"></span><span id="SAVE_STATE"></span>

**Save state** (3)


</dt> <dd></dd> <dt>

<span id="Shutdown"></span><span id="shutdown"></span><span id="SHUTDOWN"></span>

**Shutdown** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 65535</dd> </dl>

</dd> <dt>

**AutomaticStartupAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The action to take on the virtual system when the host is started.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="Restart_if_previously_active"></span><span id="restart_if_previously_active"></span><span id="RESTART_IF_PREVIOUSLY_ACTIVE"></span>

**Restart if previously active** (3)


</dt> <dd></dd> <dt>

<span id="Always_startup"></span><span id="always_startup"></span><span id="ALWAYS_STARTUP"></span>

**Always startup** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 65535</dd> </dl>

</dd> <dt>

**AutomaticStartupActionDelay**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The delay for the startup action. This value is an interval variant of the **datetime** data type.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**AutomaticStartupActionSequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The sequence number fo virtual system activation when the host system is started. A lower number indicates earlier activation. If one or more configurations show the same value, the sequence is implementation dependent. A value of "0" indicates that the sequence is implementation dependent.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**BaseBoardSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the base board for the virtual machine.

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

</dd> <dt>

**BIOSGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The globally unique identifier for the BIOS of the virtual machine.

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

</dd> <dt>

**BIOSNumLock**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if the num lock key is set to on by the BIOS; **False** if the num lock key is set to off by the BIOS.

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

</dd> <dt>

**BIOSSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the BIOS for the virtual machine.

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

</dd> <dt>

**BootOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**MAX**](https://msdn.microsoft.com/library/aa393650) (4)
</dt> </dl>

The boot order set within the BIOS of the virtual machine. This property is an array of values, **BootOrder**\[0\] through **BootOrder**\[3\], inclusive, where each value indicates a device to boot from. Each of the 4 values in the array must be set and must not be the same as another value in the array. The virtual machine will first attempt to boot from the device indicated by the first value within the array. If that device does not contain a boot sector, the virtual machine will attempt to boot from the next device specified by the **BootOrder** property and so on. If no device specified within the **BootOrder** contains a boot sector the virtual machine will fail to boot. The default value for a virtual machine is \[0, 1, 2, 3\].

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

The possible values are.

<dt>

<span id="Floppy"></span><span id="floppy"></span><span id="FLOPPY"></span>

**Floppy** (0)


</dt> <dd></dd> <dt>

<span id="CD-ROM"></span><span id="cd-rom"></span>

**CD-ROM** (1)


</dt> <dd></dd> <dt>

<span id="IDE_Hard_Drive"></span><span id="ide_hard_drive"></span><span id="IDE_HARD_DRIVE"></span>

**IDE Hard Drive** (2)


</dt> <dd></dd> <dt>

<span id="PXE_Boot"></span><span id="pxe_boot"></span><span id="PXE_BOOT"></span>

**PXE Boot** (3)


</dt> <dd></dd> <dt>

<span id="SCSI_Hard_Drive"></span><span id="scsi_hard_drive"></span><span id="SCSI_HARD_DRIVE"></span>

**SCSI Hard Drive** (4)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved**


</dt> <dd>5 65535</dd> </dl>

</dd> <dt>

**BootSourceOrder**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The boot source order for the virtual machine.

</dd> <dt>

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

**ChassisAssetTag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The asset tag of the chassis for the virtual machine.

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

</dd> <dt>

**ChassisSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the chassis for the virtual machine.

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

</dd> <dt>

**ConfigurationDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file path of the directory where information about the virtual system configuration is stored. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**ConfigurationFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path of the file where information about the virtual system configuration is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**ConfigurationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique id of the virtual system configuration.

> [!Note]  
> **ConfigurationID** is different from the **InstanceID**, and is assigned by the implementation to a virtual system or a virtual system configuration. **ConfigurationID** is not a key, and the same value may occur for more than one instance.

 

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**ConsoleMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The console mode for the VM.

The possible values are.

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

The date and time when the virtual system configuration was created.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

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

Specifies whether the virtual machine is using synthetic debugging.

The possible values are.

<dt>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>

**Off** (0)


</dt> <dd></dd> <dt>

<span id="On"></span><span id="on"></span><span id="ON"></span>

**On** (1)


</dt> <dd></dd> <dt>

<span id="OnAutoAssigned"></span><span id="onautoassigned"></span><span id="ONAUTOASSIGNED"></span>

**OnAutoAssigned** (2)


</dt> <dd></dd> </dl>

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
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for an instance of this class. In addition, the user-friendly name can be used as an index for a search or query. The name does not have to be unique within a namespace.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**GuestControlledCacheTypes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** if the guest can control cache types; **false** if the guest cannot.

</dd> <dt>

**HighMmioGapSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The size, in MB, of the high (above 4GB) memory-mapped IO gap.

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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> -   *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID** property, or be a registered ID that is assigned by a recognized global authority.
> -   *OrgID* must not contain a colon. The first colon in **InstanceID** must be between the *OrgID* and*LocalID*.
> -   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
> -   If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
> -   For DMTF defined instances, the pattern must be used with the *OrgID* set to "CIM".

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**IsSaved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the configuration has a reference to a saved state file; otherwise, **false**. This does not indicate the presence of such a file, only that the configuration specifies one.

</dd> <dt>

**LockOnDisconnect**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to lock the console when disconnecting from vmconnect; otherwise, **false**.

</dd> <dt>

**LogDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative file path of the directory where log information for the virtual system is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**LowMmioGapSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Configures the size, in megabytes, of the first MMIO gap for a virtual machine (VM).

The possible values are.

Range: 128 3584

</dd> <dt>

**NetworkBootPreferredProtocol**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP protocol used for PXE booting.

The possible values are.

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

An array that contains user supplied notes that are related to the virtual system.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this instance does not represent a system based on a snapshot of a virtual machine, this property is **Null**. Otherwise, the property holds the object path of the [**Msvm\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850257) object on which this instance is based. When building a snapshot tree hierarchy for the virtual machine, this property references the object from which the current instance is derived (the current instance is the child node and the object referenced in this property is the parent node.)

</dd> <dt>

**PauseAfterBootFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Pause after boot failure setting for the VM

**true** to pause the VM after a boot failure, and then wait for user input; otherwise, **false**.

</dd> <dt>

**RecoveryFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of the file where recovery related information of the virtual system is stored. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**SecureBootEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether secure boot is enabled for the virtual machine (VM). **true** if enabled; otherwise, **false**.

> [!Note]  
> Secure boot can only be enabled for generation 2 VMs.

 

</dd> <dt>

**SecureBootTemplateId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The globally-unique identifier of the template of initial values of UEFI Secure Boot related variables.

> [!Note]  
> This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

 

</dd> <dt>

**SnapshotDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path of the directory where information about virtual system snapshots is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**SuspendDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path of the directory where suspend related information about the virtual system is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**SwapFileDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative file path of the directory where swap files of the virtual system are stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**UserSnapshotType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A user-defined snapshot type.

The possible values are.

<dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>**Disable** (2)


</dt> <dd>

Disable the creation of any snapshot.

</dd> <dt>

<span id="ProductionFallbackToTest"></span><span id="productionfallbacktotest"></span><span id="PRODUCTIONFALLBACKTOTEST"></span>

<span id="ProductionFallbackToTest"></span><span id="productionfallbacktotest"></span><span id="PRODUCTIONFALLBACKTOTEST"></span>**ProductionFallbackToTest** (3)


</dt> <dd>

A data-consistent snapshot for use in the production environment. If a data consistent snapshot can not be created, a snapshot is created using the application state.

</dd> <dt>

<span id="ProductionNoFallback"></span><span id="productionnofallback"></span><span id="PRODUCTIONNOFALLBACK"></span>

<span id="ProductionNoFallback"></span><span id="productionnofallback"></span><span id="PRODUCTIONNOFALLBACK"></span>**ProductionNoFallback** (4)


</dt> <dd>

A data-consistent snapshot for use in the production environment. If a data consistent snapshot can not be created, a snapshot is not created using the application state.

</dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>**Test** (5)


</dt> <dd>

A snapshot that contains memory and device information for test and development purposes.

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

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("Msvm\_ProcessorSettingData.MaxProcessorsPerNumaNode, Msvm\_MemorySettingData.MaxMemoryBlocksPerNumaNode")
</dt> </dl>

**True** if virtual non-uniform memory access (NUMA) nodes are projected into the virtual machine; **False** if the virtual machine will have a single node. If **True**, the number of virtual NUMA nodes projected into the virtual machine is determined from the values of the **MaxProcessorsPerNumaNode** and **MaxMemoryBlocksPerNumaNode** properties of the [**Msvm\_ProcessorSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850190) class.

</dd> <dt>

**VirtualSystemIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_VirtualSystemSettingData.VirtualSystemIdentifier"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**Name**")
</dt> </dl>

The name of the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) object to which this setting data belongs.

</dd> <dt>

**VirtualSystemSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The sub type of the virtual machine.

The possible values are.

<dt>

<span id="Microsoft_Hyper-V_SubType_1"></span><span id="microsoft_hyper-v_subtype_1"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_1"></span>

<span id="Microsoft_Hyper-V_SubType_1"></span><span id="microsoft_hyper-v_subtype_1"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_1"></span>**Microsoft:Hyper-V:SubType:1** ("Microsoft:Hyper-V:SubType:1")


</dt> <dd>

A generation 1 VM.

</dd> <dt>

<span id="Microsoft_Hyper-V_SubType_2"></span><span id="microsoft_hyper-v_subtype_2"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_2"></span>

<span id="Microsoft_Hyper-V_SubType_2"></span><span id="microsoft_hyper-v_subtype_2"></span><span id="MICROSOFT_HYPER-V_SUBTYPE_2"></span>**Microsoft:Hyper-V:SubType:2** ("Microsoft:Hyper-V:SubType:2")


</dt> <dd>

A generation 2 VM.

</dd> </dl>

</dd> <dt>

**VirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the virtual system.

> [!Note]  
> If the virtual system type is unknown, this value must be set to "DMTF:unknown".

 

This property is formatted using the following Augmented Backus Naur Form (ABNF) format:

vs-type = dmtf-value / other-org-value / legacy-value; dmtf-value = "DMTF:" defining-org ":" org-vs-type; other-org-value = defining-org ":" org-vs-type;

The value of the above ABNF format are:

-   *dmtf-value*   a property value defined by DMTF and is defined in the description of this property.
-   *other-org-value*   is a property value defined by a business entity other than DMTF and is not defined in the description of this property.
-   *legacy-value*   a property value defined by a business entity other than DMTF and is not defined in the description of this property. These values are permitted but recommended to be deprecated over time.
-   *defining-org*   an identifier for the business entity that defines the virtual system type. It should include a copyrighted, trademarked, or a unique name that is owned by the business entity. It should not be "DMTF" and shall not contain a colon.
-   *org-vs-type*   an identifier for the virtual system type within the defining business entity. It should be unique within defining-org. org-vs-type may use any character allowed for CIM strings, except the following: U0000-U001F (Unicode C0 controls), U0020 (space), U007F (Unicode C0 controls), or U0080-U009F (Unicode C1 controls).
-   If there is a need to structure the value into segments, the segments should be separated with a single colon.
-   The values of this property should be processed case sensitively. They are intended to be processed programmatically, instead of being a display name, and should be short.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





