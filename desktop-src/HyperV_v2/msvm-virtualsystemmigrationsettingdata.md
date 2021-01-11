---
description: Represents the migration settings for migrating a virtual system and the storage attached to a virtual system.
ms.assetid: 2d632fe2-31ee-4e4d-b2a6-c1d1f3b4d624
title: Msvm_VirtualSystemMigrationSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemMigrationSettingData
- Msvm_VirtualSystemMigrationSettingData.InstanceID
- Msvm_VirtualSystemMigrationSettingData.Caption
- Msvm_VirtualSystemMigrationSettingData.Description
- Msvm_VirtualSystemMigrationSettingData.ElementName
- Msvm_VirtualSystemMigrationSettingData.MigrationType
- Msvm_VirtualSystemMigrationSettingData.Priority
- Msvm_VirtualSystemMigrationSettingData.Bandwidth
- Msvm_VirtualSystemMigrationSettingData.BandwidthUnit
- Msvm_VirtualSystemMigrationSettingData.OtherTransportType
- Msvm_VirtualSystemMigrationSettingData.TransportType
- Msvm_VirtualSystemMigrationSettingData.RemoveSourceUnmanagedVhds
- Msvm_VirtualSystemMigrationSettingData.AvoidRemovingVHDs
- Msvm_VirtualSystemMigrationSettingData.CPUCappingMagnitude
- Msvm_VirtualSystemMigrationSettingData.CancelIfBlackoutThresholdExceeded
- Msvm_VirtualSystemMigrationSettingData.AllowOverwriteExistingFile
- Msvm_VirtualSystemMigrationSettingData.UnmanagedVhds
- Msvm_VirtualSystemMigrationSettingData.DestinationPlannedVirtualSystemId
- Msvm_VirtualSystemMigrationSettingData.DestinationIPAddressList
- Msvm_VirtualSystemMigrationSettingData.RetainVhdCopiesOnSource
- Msvm_VirtualSystemMigrationSettingData.EnableCompression
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualSystemMigrationSettingData class

Represents the migration settings for migrating a virtual system and the storage attached to a virtual system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemMigrationSettingData : CIM_VirtualSystemMigrationSettingData
{
  string  InstanceID;
  string  Caption = "Migration Setting Data";
  string  Description = "Virtual System Migration Setting Data";
  string  ElementName;
  uint16  MigrationType;
  uint16  Priority;
  uint16  Bandwidth;
  string  BandwidthUnit;
  string  OtherTransportType;
  uint16  TransportType;
  boolean RemoveSourceUnmanagedVhds;
  boolean AvoidRemovingVHDs;
  uint16  CPUCappingMagnitude;
  boolean CancelIfBlackoutThresholdExceeded;
  boolean AllowOverwriteExistingFile;
  string  UnmanagedVhds[];
  string  DestinationPlannedVirtualSystemId;
  string  DestinationIPAddressList[];
  boolean RetainVhdCopiesOnSource;
  boolean EnableCompression;
};
```

## Members

The **Msvm\_VirtualSystemMigrationSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemMigrationSettingData** class has these properties.

<dl> <dt>

**AllowOverwriteExistingFile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Allow the storage migration operation to overwrite existing .vhdx files.

> [!Note]  
> This property was added in Windows 10, version 1703.

 

</dd> <dt>

**AvoidRemovingVHDs**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Do not remove any VHDs during the migration, i.e. VHDs on the source in successand VHDs on the destination in failure.

> [!Note]  
> Added in Windows 10, version 1703 and Windows Server 2016.

 

</dd> <dt>

**Bandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the bandwidth assigned to or requested for a virtual system migration operation. The bandwidth units are specified by the **BandwidthUnit** property. Within a migration, a value of 0 indicates the default bandwidth. Otherwise, a value of 0 indicates that bandwidths are not supported.

**Bandwidth** and **Priority** can be used in conjunction. Migration processes that have the highest equal priority value share the available bandwidth based on their requested bandwidth. If not all bandwidth is consumed by this set of processes, migration processes with the next lower equal priority share the remaining bandwidth. If still more bandwidth remains, migration processes with the next lower equal priority are considered, and so forth.

This property is inherited from **CIM\_VirtualSystemMigrationSettingData**.

</dd> <dt>

**BandwidthUnit**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the units used by the **Bandwidth** property. The value of this property must be a legal value of the Programmatic Units qualifier as defined in Appendix C.1 of DSP0004 V2.4 or later.

If the value of this property is "percent", the value of the **Bandwidth** property must be between 0 and 100, with higher values indicating a higher bandwidth. A value of 100 indicates the total available bandwidth for performing virtual system migration operations. Values between 1 and 100 should linearly correlate with the available bandwidth range. For example, a value of 50 should request half of the available bandwidth.

This property is inherited from **CIM\_VirtualSystemMigrationSettingData**.

</dd> <dt>

**CancelIfBlackoutThresholdExceeded**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Cancels migration if the blackout threshold time is exceeded.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**CPUCappingMagnitude**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("CPUCappingMagnitude")
</dt> </dl>

Degree of CPU capping during migration.

> [!Note]  
> Added in Windows 10, version 1709.

 

<dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** (0)


</dt> <dd></dd> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**DestinationIPAddressList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This will be **Null** for storage migration. For virtual system migration, this can contain a list of IP addresses of the destination host.

</dd> <dt>

**DestinationPlannedVirtualSystemId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If a planned virtual machine exists at the migration destination, this property will be set to the GUID of the destination planned virtual machine where the virtual machine needs to migrate. This is useful for cases where a user has created a planned virtual machine at the destination, along with resource setup, and wants a virtual machine from the source to migrate into this planned virtual machine.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)).

</dd> <dt>

**EnableCompression**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to compress the live migration traffic. **True** indicates to compress; otherwise **False**.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**MigrationType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("MigrationType")
</dt> </dl>

Specifies the type of migration operation to be performed. This property is inherited from **CIM\_VirtualSystemMigrationSettingData**.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="VirtualSystem"></span><span id="virtualsystem"></span><span id="VIRTUALSYSTEM"></span>

<span id="VirtualSystem"></span><span id="virtualsystem"></span><span id="VIRTUALSYSTEM"></span>**VirtualSystem** (32768)


</dt> <dd>

Migrates the virtual system to the destination host.

</dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>**Storage** (32769)


</dt> <dd>

Migrates only the storage resources of the virtual system.

</dd> <dt>

<span id="Staged"></span><span id="staged"></span><span id="STAGED"></span>

<span id="Staged"></span><span id="staged"></span><span id="STAGED"></span>**Staged** (32770)


</dt> <dd>

Using the virtual system configuration, creates a planned virtual system at the destination host.

</dd> <dt>

<span id="VirtualSystemAndStorage"></span><span id="virtualsystemandstorage"></span><span id="VIRTUALSYSTEMANDSTORAGE"></span>

<span id="VirtualSystemAndStorage"></span><span id="virtualsystemandstorage"></span><span id="VIRTUALSYSTEMANDSTORAGE"></span>**VirtualSystemAndStorage** (32771)


</dt> <dd>

Migrates the virtual system and its storage to the destination host.

</dd> <dt>

<span id="StorageDeepCheck"></span><span id="storagedeepcheck"></span><span id="STORAGEDEEPCHECK"></span>

<span id="StorageDeepCheck"></span><span id="storagedeepcheck"></span><span id="STORAGEDEEPCHECK"></span>**StorageDeepCheck** (32772)


</dt> <dd>

Performs a virtual system storage resource migration ability check at the destination host.

</dd> </dl>

</dd> <dt>

**OtherTransportType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of transport to be applied if the value of **TransportType** is 1 (Other). This property is inherited from **CIM\_VirtualSystemMigrationSettingData**.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a relative migration importance, which the migration system may use to order or otherwise give preference among multiple pending migration requests. The lower the value, the higher the priority. Within a migration, a value of 0 indicates the default priority. Otherwise, a value of 0 indicates that priorities are not supported.

This property is inherited from **CIM\_VirtualSystemMigrationSettingData**.

</dd> <dt>

**RemoveSourceUnmanagedVhds**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Remove source unmanaged VHDs.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

**RetainVhdCopiesOnSource**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For a storage migration, this specifies whether the read-only VHDs on the source host should be removed after the migration is completed.

</dd> <dt>

**TransportType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("TransportType")
</dt> </dl>

Specifies the type of transport to be applied for a virtual system migration operation. This property is inherited from **CIM\_VirtualSystemMigrationSettingData**.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="SSH"></span><span id="ssh"></span>

**SSH** (2)


</dt> <dd></dd> <dt>

<span id="TLS"></span><span id="tls"></span>

**TLS** (3)


</dt> <dd></dd> <dt>

<span id="TLS_Strict"></span><span id="tls_strict"></span><span id="TLS_STRICT"></span>

**TLS Strict** (4)


</dt> <dd></dd> <dt>

<span id="TCP"></span><span id="tcp"></span>

**TCP** (5)


</dt> <dd></dd> <dt>

<span id="IPC"></span><span id="ipc"></span>

**IPC** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..)


</dt> <dd></dd> </dl>

For live migration, this property specifies the transport type to be used for transferring virtual system state to the destination host. The supported values are:

<dt>

<span id="TCP"></span><span id="tcp"></span>

<span id="TCP"></span><span id="tcp"></span>**TCP** (5)


</dt> <dd>

Indicates the TCP transport type.

</dd> <dt>

<span id="SMB"></span><span id="smb"></span>

<span id="SMB"></span><span id="smb"></span>**SMB** (32768)


</dt> <dd>

Indicates the transport type for transferring the virtual machine state is SMB.

</dd> </dl>

</dd> <dt>

**UnmanagedVhds**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), **HyperVEmbeddedInstance** ("Msvm\_MoveUnmanagedVhd")
</dt> </dl>

An array of embedded [**Msvm\_MoveUnmanagedVhd**](msvm-moveunmanagedvhd.md) instances which contain unmanaged VHDs information.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

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

[**CIM\_VirtualSystemMigrationSettingData**](cim-virtualsystemmigrationsettingdata.md)
</dt> <dt>

[**MigrateVirtualSystemToHost**](migratevirtualsystemtohost-msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

