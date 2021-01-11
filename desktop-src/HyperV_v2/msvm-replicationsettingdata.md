---
description: Represents the replication-specific settings for a virtual machine.
ms.assetid: f6f6a413-a949-4aca-930b-37e39bdc1fdb
title: Msvm_ReplicationSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReplicationSettingData
- Msvm_ReplicationSettingData.InstanceID
- Msvm_ReplicationSettingData.Caption
- Msvm_ReplicationSettingData.Description
- Msvm_ReplicationSettingData.ElementName
- Msvm_ReplicationSettingData.VirtualSystemIdentifier
- Msvm_ReplicationSettingData.VirtualSystemType
- Msvm_ReplicationSettingData.Notes
- Msvm_ReplicationSettingData.CreationTime
- Msvm_ReplicationSettingData.ConfigurationID
- Msvm_ReplicationSettingData.ConfigurationDataRoot
- Msvm_ReplicationSettingData.ConfigurationFile
- Msvm_ReplicationSettingData.SnapshotDataRoot
- Msvm_ReplicationSettingData.SuspendDataRoot
- Msvm_ReplicationSettingData.SwapFileDataRoot
- Msvm_ReplicationSettingData.LogDataRoot
- Msvm_ReplicationSettingData.AutomaticStartupAction
- Msvm_ReplicationSettingData.AutomaticStartupActionDelay
- Msvm_ReplicationSettingData.AutomaticStartupActionSequenceNumber
- Msvm_ReplicationSettingData.AutomaticShutdownAction
- Msvm_ReplicationSettingData.AutomaticRecoveryAction
- Msvm_ReplicationSettingData.RecoveryFile
- Msvm_ReplicationSettingData.AuthenticationType
- Msvm_ReplicationSettingData.CertificateThumbPrint
- Msvm_ReplicationSettingData.RootCertificateThumbPrint
- Msvm_ReplicationSettingData.CompressionEnabled
- Msvm_ReplicationSettingData.BypassProxyServer
- Msvm_ReplicationSettingData.RecoveryConnectionPoint
- Msvm_ReplicationSettingData.RecoveryHostSystem
- Msvm_ReplicationSettingData.PrimaryConnectionPoint
- Msvm_ReplicationSettingData.PrimaryHostSystem
- Msvm_ReplicationSettingData.RecoveryServerPortNumber
- Msvm_ReplicationSettingData.ReplicateHostKvpItems
- Msvm_ReplicationSettingData.ApplicationConsistentSnapshotInterval
- Msvm_ReplicationSettingData.RecoveryHistory
- Msvm_ReplicationSettingData.IncludedDisks
- Msvm_ReplicationSettingData.AutoResynchronizeEnabled
- Msvm_ReplicationSettingData.AutoResynchronizeIntervalStart
- Msvm_ReplicationSettingData.AutoResynchronizeIntervalEnd
- Msvm_ReplicationSettingData.EnableWriteOrderPreservationAcrossDisks
- Msvm_ReplicationSettingData.ReplicationProvider
- Msvm_ReplicationSettingData.AdditionalSettings
- Msvm_ReplicationSettingData.ReplicationInterval
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ReplicationSettingData class

Represents the replication-specific settings for a virtual machine. The client passes an instance of this class to [**Msvm\_ReplicationService.CreateReplicationRelationship**](createreplicationrelationship-msvm-replicationservice.md) to create a replication relationship. The client can't directly change the values of any of the properties for this class; it must call the [**Msvm\_ReplicationService.ModifyReplicationSettings**](modifyreplicationsettings-msvm-replicationservice.md) method to change the values. Each replication relationship has a single instance of settings.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ReplicationSettingData : CIM_VirtualSystemSettingData
{
  string   InstanceID = "Microsoft:Virtual Machine GUID\HVR";
  string   Caption = "Replication Settings";
  string   Description = "Virtual Machine Replication Settings Data";
  string   ElementName;
  string   VirtualSystemIdentifier;
  string   VirtualSystemType = "Microsoft:Hyper-V:Replica";
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
  uint16   AuthenticationType;
  string   CertificateThumbPrint;
  string   RootCertificateThumbPrint;
  boolean  CompressionEnabled;
  boolean  BypassProxyServer;
  string   RecoveryConnectionPoint;
  string   RecoveryHostSystem;
  string   PrimaryConnectionPoint;
  string   PrimaryHostSystem;
  uint16   RecoveryServerPortNumber = 0;
  boolean  ReplicateHostKvpItems = True;
  uint16   ApplicationConsistentSnapshotInterval;
  uint16   RecoveryHistory = 0;
  string   IncludedDisks[];
  boolean  AutoResynchronizeEnabled = False;
  datetime AutoResynchronizeIntervalStart = 00000000183000.000000:000;
  datetime AutoResynchronizeIntervalEnd = 00000000060000.000000:000;
  boolean  EnableWriteOrderPreservationAcrossDisks;
  string   ReplicationProvider;
  string   AdditionalSettings;
  uint16   ReplicationInterval = 300;
};
```

## Members

The **Msvm\_ReplicationSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReplicationSettingData** class has these properties.

<dl> <dt>

**AdditionalSettings**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional replication settings that the endpoint provider can use.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**ApplicationConsistentSnapshotInterval**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval between application consistent snapshots, specified in hours. Valid values are from 1 hour to 12 hours.

</dd> <dt>

**AuthenticationType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Define authentication mode used to connect to recover server.

<dt>

<span id="Kerberos_authentication"></span><span id="kerberos_authentication"></span><span id="KERBEROS_AUTHENTICATION"></span>

<span id="Kerberos_authentication"></span><span id="kerberos_authentication"></span><span id="KERBEROS_AUTHENTICATION"></span>**Kerberos authentication** (1)


</dt> <dd>

Kerberos authentication.

</dd> <dt>

<span id="Certificate_based_authentication"></span><span id="certificate_based_authentication"></span><span id="CERTIFICATE_BASED_AUTHENTICATION"></span>

<span id="Certificate_based_authentication"></span><span id="certificate_based_authentication"></span><span id="CERTIFICATE_BASED_AUTHENTICATION"></span>**Certificate based authentication** (2)


</dt> <dd>

Certificate based authentication.

</dd> </dl>

</dd> <dt>

**AutomaticRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used.

This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**AutomaticShutdownAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used.

This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**AutomaticStartupAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used.

This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**AutomaticStartupActionDelay**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The delay time before the virtual machine is automatically started up. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**AutomaticStartupActionSequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A number that indicates the relative sequence of virtual machine activation when the host system is started. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**AutoResynchronizeEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether resynchronization operations are automatically triggered when a replication error occurs due to power and hardware failures. Resynchronization operations are only triggered when the failure occurs between the times specified by the **AutoResynchronizeIntervalStart** and **AutoResynchronizeIntervalEnd** properties.

The default value is **False**.

</dd> <dt>

**AutoResynchronizeIntervalEnd**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the end time for automatic resynchronization operations to be triggered. This value is in local time. The default value is 06:00 (6:00 A.M.).

Resynchronization operations are only triggered when the failure occurs between the times specified by the **AutoResynchronizeIntervalStart** and **AutoResynchronizeIntervalEnd** properties.

Resynchronization operations can also be scheduled so that they are triggered during the next interval.

</dd> <dt>

**AutoResynchronizeIntervalStart**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the start time for automatic resynchronization operations to be triggered. This value is in local time. The default value is 18:30 (6:30 P.M.).

Resynchronization operations are only triggered when the failure occurs between the times specified by the **AutoResynchronizeIntervalStart** and **AutoResynchronizeIntervalEnd** properties.

Resynchronization operations can also be scheduled so that they are triggered during the next interval.

</dd> <dt>

**BypassProxyServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the proxy server should be bypassed when connecting to a recovery server.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Replication Settings".

</dd> <dt>

**CertificateThumbPrint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (128)
</dt> </dl>

Certificate thumbprint to use when the **AuthenticationType** property is certificate based authentication.

</dd> <dt>

**CompressionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether replication data will be compressed while sending it to the recovery server.

</dd> <dt>

**ConfigurationDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used.

This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**ConfigurationFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path and file name of a file where information about the virtual machine configuration is stored. This path is relative to the **ConfigurationDataRoot** property. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**ConfigurationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique identifier of the virtual machine configuration. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time at which the settings for the virtual machine were created. If this object represents the current settings for the virtual machine, this value would be the time at which the system was created. If this object represents the snapshot settings for the virtual machine, this value would be the time at which the snapshot was taken. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

This is a read-only property, but it can be changed by using the [**ModifySystemSettings**](modifysystemsettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Virtual Machine Replication Settings Data".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), and it is set to the display name for the virtual machine.

</dd> <dt>

**EnableWriteOrderPreservationAcrossDisks**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("No value")
</dt> </dl>

Specifies whether all replicating virtual hard disks for the virtual machine are replicated to the same point in time. This ensures replication honors the write-order of the applications in the virtual machine.

**Windows 8.1:** Beginning with Windows 8.1 and Windows Server 2012 R2, this property is deprecated and always set to **TRUE**.

</dd> <dt>

**IncludedDisks**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **HyperVEmbeddedInstance** ("CIM\_StorageAllocationSettingData"), [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed")
</dt> </dl>

The list of virtual hard disks (VHDs) attached to the system that will be replicated by the replication engine. This is an array of strings, each containing the **InstanceID** of the [**Msvm\_StorageAllocationSettingData**](msvm-storageallocationsettingdata.md) that represents the VHD.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)). For Windows 8, it is always set to "Microsoft:*Virtual Machine GUID*\\HVR". For Windows 8.1, it is set to "Microsoft:*Virtual Machine GUID*\\HVR\\<0/1>". In the Windows 8.1 value, 0 indicates primary and 1 indicates extended replication. For more info about extended replication, see [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md).

</dd> <dt>

**LogDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where log information for the virtual machine is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**Notes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used and can't be set.

This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**PrimaryConnectionPoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

The name of the primary connection point. In the case of a primary cluster, this is the broker CAP name. In the case of a standalone primary server, this is the host system name.

</dd> <dt>

**PrimaryHostSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

The fully qualified domain name of the primary host system that is hosting the virtual machine.

</dd> <dt>

**RecoveryConnectionPoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

The name of the recovery connection point. In the case of a recovery cluster, this is the broker CAP name. In the case of a standalone recovery server, this is the host system name.

</dd> <dt>

**RecoveryFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The full path of a file where recovery related information for the virtual machine is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**RecoveryHistory**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of recovery snapshots that will be stored on the recovery server. Valid values are from 0 to 24.

</dd> <dt>

**RecoveryHostSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

The fully qualified domain name of the recovery host system which is hosting the virtual machine.

</dd> <dt>

**RecoveryServerPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The recovery server port number to use when making a secure connection for replication.

</dd> <dt>

**ReplicateHostKvpItems**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether host-only [**Msvm\_KvpExchangeDataItem**](msvm-kvpexchangedataitem.md)s should be replicated from the primary virtual machine to the recovery virtual machine.

</dd> <dt>

**ReplicationInterval**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Replication interval of a replication relationship in seconds. Valid values are:

30

300

900

Default value is 300 seconds.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**ReplicationProvider**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path to the instance of the [**Msvm\_ReplicationProvider**](msvm-replicationprovider.md) class that identifies the replication provider endpoint.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**RootCertificateThumbPrint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (128)
</dt> </dl>

Root certificate thumbprint of the certificate in use when **AuthenticationType** is 2 (certificate based authorization).

</dd> <dt>

**SnapshotDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where information about the virtual machine snapshots is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**SuspendDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where information about the virtual machine suspend-related information is stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**SwapFileDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of a directory where swap files for the virtual machine are stored. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), but it is not used.

</dd> <dt>

**VirtualSystemIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the [**CIM\_ComputerSystem**](/windows/desktop/CIMWin32Prov/cim-computersystem) object to which this setting data belongs. This property is an override from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)).

</dd> <dt>

**VirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of virtual machine the setting data represents. This property is inherited from [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)), and it is always set to "Microsoft:Hyper-V:Replica".

</dd> </dl>

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

[**ModifyReplicationSettings**](modifyreplicationsettings-msvm-replicationservice.md)
</dt> </dl>

 

