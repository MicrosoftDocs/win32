---
title: Msvm\_VirtualSystemGlobalSettingData class
description: Represents the global settings for a virtual system.
ms.assetid: c0a45ae9-fd09-4bae-a434-2cfac166ada3
keywords:
- Msvm_VirtualSystemGlobalSettingData class Hyper-V
- Msvm_VirtualSystemGlobalSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemGlobalSettingData
- Msvm_VirtualSystemGlobalSettingData.Caption
- Msvm_VirtualSystemGlobalSettingData.Description
- Msvm_VirtualSystemGlobalSettingData.SystemName
- Msvm_VirtualSystemGlobalSettingData.InstanceID
- Msvm_VirtualSystemGlobalSettingData.ElementName
- Msvm_VirtualSystemGlobalSettingData.VirtualSystemType
- Msvm_VirtualSystemGlobalSettingData.AutoActivate
- Msvm_VirtualSystemGlobalSettingData.OtherVirtualSystemType
- Msvm_VirtualSystemGlobalSettingData.CreationTime
- Msvm_VirtualSystemGlobalSettingData.ExternalDataRoot
- Msvm_VirtualSystemGlobalSettingData.SettingType
- Msvm_VirtualSystemGlobalSettingData.SnapshotDataRoot
- Msvm_VirtualSystemGlobalSettingData.AutomaticStartupAction
- Msvm_VirtualSystemGlobalSettingData.AutomaticStartupActionDelay
- Msvm_VirtualSystemGlobalSettingData.AutomaticShutdownAction
- Msvm_VirtualSystemGlobalSettingData.AutomaticRecoveryAction
- Msvm_VirtualSystemGlobalSettingData.AdditionalRecoveryInformation
- Msvm_VirtualSystemGlobalSettingData.ScopeOfResidence
- Msvm_VirtualSystemGlobalSettingData.DebugChannelId
- Msvm_VirtualSystemGlobalSettingData.DebugPort
- Msvm_VirtualSystemGlobalSettingData.DebugPortEnabled
- Msvm_VirtualSystemGlobalSettingData.AllowFullSCSICommandSet
- Msvm_VirtualSystemGlobalSettingData.Version
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

# Msvm\_VirtualSystemGlobalSettingData class

Represents the global settings for a virtual system. These settings do not change if a new snapshot is applied to the virtual system.

The **Msvm\_VirtualSystemGlobalSettingData** class is derived from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954).

**Windows Server 2008:** The **Msvm\_VirtualSystemGlobalSettingData** class is derived from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemGlobalSettingData : CIM_VirtualSystemSettingData
{
  string   Caption = "Global Virtual Machine Settings";
  string   Description = "Global settings for the virtual machine";
  string   SystemName = "GUID";
  string   InstanceID = "Microsoft:GUID\Global";
  string   ElementName = "Global Virtual Machine Settings";
  uint16   VirtualSystemType = 301;
  boolean  AutoActivate;
  string   OtherVirtualSystemType;
  datetime CreationTime;
  string   ExternalDataRoot;
  uint16   SettingType = 32768;
  string   SnapshotDataRoot;
  uint16   AutomaticStartupAction = 1;
  datetime AutomaticStartupActionDelay = 00000000000000.000000:000;
  uint16   AutomaticShutdownAction = 1;
  uint16   AutomaticRecoveryAction = 1;
  string   AdditionalRecoveryInformation;
  string   ScopeOfResidence;
  uint32   DebugChannelId;
  uint32   DebugPort;
  uint16   DebugPortEnabled;
  boolean  AllowFullSCSICommandSet = False;
  string   Version;
};
```

## Members

The **Msvm\_VirtualSystemGlobalSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemGlobalSettingData** class has these properties.

<dl> <dt>

**AdditionalRecoveryInformation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Any additional information provided to the recovery action. The meaning of this property is defined by the action in **AutomaticRecoveryAction**. If **AutomaticRecoveryAction** is 0 (None) or 1 (Restart), this value is **NULL**. If **AutomaticRecoveryAction** is 2 (Revert to Snapshot), this is the object path to a snapshot that should be applied on failure of the virtual machine worker process.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**AllowFullSCSICommandSet**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether SCSI commands from the guest operating system are passed to pass-through disks. It is recommended that SCSI filtering remains enabled for production deployments.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

**Windows Server 2008:** The **AllowFullSCSICommandSet** property is not supported before Windows Server 2008 R2.



| Value                                                                            | Meaning                                                                                                |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>False</dt> </dl> | SCSI commands emitted by the guest operating system to pass-through disks are filtered.<br/>     |
| <dl> <dt>True</dt> </dl>  | SCSI commands emitted by the guest operating system to pass-through disks are not filtered.<br/> |



 

</dd> <dt>

**AutoActivate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to **NULL**.

**Windows Server 2008:** The **AutoActivate** property is not supported before Windows Server 2008 R2.

</dd> <dt>

**AutomaticRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The action to be taken if the virtual machine worker process terminates abnormally. The default action is 1 (Restart).

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Restart"></span><span id="restart"></span><span id="RESTART"></span>

**Restart** (1)


</dt> <dd></dd> <dt>

<span id="Revert_to_Snapshot"></span><span id="revert_to_snapshot"></span><span id="REVERT_TO_SNAPSHOT"></span>

**Revert to Snapshot** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**AutomaticShutdownAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The action to take when the host is shut down. The default action is 1 (Save State).

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

<dt>

<span id="Turn_Off"></span><span id="turn_off"></span><span id="TURN_OFF"></span>

**Turn Off** (0)


</dt> <dd></dd> <dt>

<span id="Save_State"></span><span id="save_state"></span><span id="SAVE_STATE"></span>

**Save State** (1)


</dt> <dd></dd> <dt>

<span id="ShutDown"></span><span id="shutdown"></span><span id="SHUTDOWN"></span>

**ShutDown** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**AutomaticStartupAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The action to be taken when the host is started. The default action is 1 ("Restart if Previously Running").

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

None

</dd> <dt>

<span id="Restart_if_Previously_Running"></span><span id="restart_if_previously_running"></span><span id="RESTART_IF_PREVIOUSLY_RUNNING"></span>

<span id="Restart_if_Previously_Running"></span><span id="restart_if_previously_running"></span><span id="RESTART_IF_PREVIOUSLY_RUNNING"></span>**Restart if Previously Running** (1)


</dt> <dd>

Restart if Previously Running

</dd> <dt>

<span id="Always_Startup"></span><span id="always_startup"></span><span id="ALWAYS_STARTUP"></span>

<span id="Always_Startup"></span><span id="always_startup"></span><span id="ALWAYS_STARTUP"></span>**Always Startup** (2)


</dt> <dd>

Always Startup

</dd> </dl>

</dd> <dt>

**AutomaticStartupActionDelay**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**SubType**](https://msdn.microsoft.com/library/aa393651) ("Interval")
</dt> </dl>

The time interval to wait before performing the startup action. By default, there is no delay.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Global Virtual Machine Settings".

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the virtual system setting data was created. For snapshots, this value corresponds to the time at which the snapshot was taken. For non-snapshots, this value corresponds to the time at which the virtual system was created. This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954).

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

**Windows Server 2008:** The **CreationTime** property is not supported before Windows Server 2008 R2.

</dd> <dt>

**DebugChannelId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The channel identifier used to debug the virtual system using the VUD unified debugger.

</dd> <dt>

**DebugPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The tcpip port used to debug the virtual system using synthetic debugging.

</dd> <dt>

**DebugPortEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the virtual system is using synthetic debugging.

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

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Global settings for the virtual machine".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it defaults to "Global Virtual Machine Settings". Changing this property will change the **ElementName** of the associated [**Msvm\_ComputerSystem**](msvm-computersystem.md) derivative.

This is a read-only property, but it can be changed using the **ModifyVirtualSystem** method of the **Msvm\_VirtualSystemManagementService** class.

</dd> <dt>

**ExternalDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fully qualified path to the root directory of an external data store. This store is managed by the virtual system management service and may contain private data from multiple virtual systems. This property may be specified only at the time the virtual machine is defined.

This is a read-only property, but it can be changed before the virtual machine is created using the [**DefineVirtualSystem**](definevirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) and it is set to "Microsoft:*GUID*\\Global".

</dd> <dt>

**OtherVirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).**VirtualSystemType**")
</dt> </dl>

This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to **NULL**.

**Windows Server 2008:** The **OtherVirtualSystemType** property is not supported before Windows Server 2008 R2.

</dd> <dt>

**ScopeOfResidence**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The authorization scope to use in determining the access control policy for this virtual system.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**SettingType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (SettingType)
</dt> </dl>

This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to 32768, which means "Global setting type".

**Windows Server 2008:** The **SettingType** property is not supported before Windows Server 2008 R2.

<dt>

<span id="Input"></span><span id="input"></span><span id="INPUT"></span>

**Input** (1)


</dt> <dd></dd> <dt>

<span id="Recorded"></span><span id="recorded"></span><span id="RECORDED"></span>

**Recorded** (2)


</dt> <dd></dd> <dt>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>

**Current** (3)


</dt> <dd></dd> <dt>

<span id="Capability"></span><span id="capability"></span><span id="CAPABILITY"></span>

**Capability** (4)


</dt> <dd></dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

**Snapshot** (5)


</dt> <dd></dd> <dt>

<span id="Global"></span><span id="global"></span><span id="GLOBAL"></span>

**Global** (32768)


</dt> <dd></dd> </dl>

</dd> <dt>

**SnapshotDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fully qualified path to the root directory of the external data store used to store snapshots for this virtual system. This store is managed by the virtual system management service and may contain private data from multiple virtual systems. Changes made to this property affect only snapshots taken subsequent to the change.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The label by which the object is known. This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to "*GUID*". This corresponds to the **Name** property of the associated [**Msvm\_ComputerSystem**](msvm-computersystem.md) class and the **SystemName** property of the associated [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) class.

**Windows Server 2008:** The **SystemName** property is not supported before Windows Server 2008 R2.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the virtual system in a format of "*major*.*minor*", for example "2.0".

**Windows Server 2008:** The **Version** property is not supported before Windows Server 2008 R2.

</dd> <dt>

**VirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).**OtherVirtualSystemType**")
</dt> </dl>

This property is inherited from [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and it is set to 301, which means "Hyper-V".

**Windows Server 2008:** The **VirtualSystemType** property is not supported before Windows Server 2008 R2.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemGlobalSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911)
</dt> <dt>

[**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 





