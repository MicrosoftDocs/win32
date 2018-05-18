---
title: MSFT\_SMSystemCapabilities class
description: Represents the capabilities of a computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2b2e4ce7-79c5-4414-b42a-cb748e74e6dc'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMSystemCapabilities class", "MSFT_SMSystemCapabilities class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMSystemCapabilities
- MSFT_SMSystemCapabilities.ObjectId
- MSFT_SMSystemCapabilities.Identifier
- MSFT_SMSystemCapabilities.ReplicationSupportedTypeMirrorLocal
- MSFT_SMSystemCapabilities.ReplicationSupportedTypeMirrorRemote
- MSFT_SMSystemCapabilities.ReplicationSupportedTypeSnapshotLocal
- MSFT_SMSystemCapabilities.ReplicationSupportedTypeSnapshotRemote
- MSFT_SMSystemCapabilities.ReplicationSupportedTypeCloneLocal
- MSFT_SMSystemCapabilities.ReplicationSupportedTypeCloneRemote
- MSFT_SMSystemCapabilities.MaximumReplicasPerSourceSnapshot
- MSFT_SMSystemCapabilities.MaximumReplicasPerSourceClone
- MSFT_SMSystemCapabilities.MaximumReplicasPerSourceMirror
- MSFT_SMSystemCapabilities.StorageConfigSupportsPoolCreation
- MSFT_SMSystemCapabilities.StorageConfigSupportsPoolDeletion
- MSFT_SMSystemCapabilities.StorageConfigSupportsPoolModification
- MSFT_SMSystemCapabilities.StorageConfigSupportsPoolCapacityExpansion
- MSFT_SMSystemCapabilities.StorageConfigSupportsStorageVolumeCreation
- MSFT_SMSystemCapabilities.StorageConfigSupportsStorageVolumeDeletion
- MSFT_SMSystemCapabilities.StorageConfigSupportsStorageVolumeModification
- MSFT_SMSystemCapabilities.StorageConfigSupportsStorageVolumeCapacityExpansion
- MSFT_SMSystemCapabilities.StorageConfigSupportsStorageVolumeCapacityReduction
- MSFT_SMSystemCapabilities.StorageConfigSupportsThinProvisionedPools
- MSFT_SMSystemCapabilities.MaskingValidHardwareIdTypes
- MSFT_SMSystemCapabilities.MaskingValidHardwareIdTypeDescriptions
- MSFT_SMSystemCapabilities.MaskingOtherValidHardwareIDTypes
- MSFT_SMSystemCapabilities.MaskingPortsPerView
- MSFT_SMSystemCapabilities.MaskingPortsPerViewDescription
- MSFT_SMSystemCapabilities.MaskingClientSelectableDeviceNumbers
- MSFT_SMSystemCapabilities.MaskingOneHardwareIDPerView
- MSFT_SMSystemCapabilities.MaskingExposeStorageVolumesToHostsSupported
- MSFT_SMSystemCapabilities.MaskingHideStorageVolumesFromHostsSupported
- MSFT_SMSystemCapabilities.MaskingMaximumMapCount
- MSFT_SMSystemCapabilities.iSCSITargetEndpointCreation
- MSFT_SMSystemCapabilities.iSCSITargetEndpointCreationDescription
- MSFT_SMSystemCapabilities.SupportedHostTypes
- MSFT_SMSystemCapabilities.OtherHostTypeDescriptions
- MSFT_SMSystemCapabilities.SupportedHostTypeDescriptions
- MSFT_SMSystemCapabilities.SupportsFileSystemCreation
- MSFT_SMSystemCapabilities.SupportsFileServer
- MSFT_SMSystemCapabilities.SupportsFileServerCreation
- MSFT_SMSystemCapabilities.SupportsContinuouslyAvailableFileServer
- MSFT_SMSystemCapabilities.SupportedFileServerProtocols
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMSystemCapabilities class

Represents the capabilities of a computer system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMSystemCapabilities
{
  String  ObjectId;
  String  Identifier;
  boolean ReplicationSupportedTypeMirrorLocal;
  boolean ReplicationSupportedTypeMirrorRemote;
  boolean ReplicationSupportedTypeSnapshotLocal;
  boolean ReplicationSupportedTypeSnapshotRemote;
  boolean ReplicationSupportedTypeCloneLocal;
  boolean ReplicationSupportedTypeCloneRemote;
  uint16  MaximumReplicasPerSourceSnapshot;
  uint16  MaximumReplicasPerSourceClone;
  uint16  MaximumReplicasPerSourceMirror;
  boolean StorageConfigSupportsPoolCreation;
  boolean StorageConfigSupportsPoolDeletion;
  boolean StorageConfigSupportsPoolModification;
  boolean StorageConfigSupportsPoolCapacityExpansion;
  boolean StorageConfigSupportsStorageVolumeCreation;
  boolean StorageConfigSupportsStorageVolumeDeletion;
  boolean StorageConfigSupportsStorageVolumeModification;
  boolean StorageConfigSupportsStorageVolumeCapacityExpansion;
  boolean StorageConfigSupportsStorageVolumeCapacityReduction;
  boolean StorageConfigSupportsThinProvisionedPools;
  uint16  MaskingValidHardwareIdTypes[];
  string  MaskingValidHardwareIdTypeDescriptions[];
  string  MaskingOtherValidHardwareIDTypes[];
  uint16  MaskingPortsPerView;
  string  MaskingPortsPerViewDescription;
  boolean MaskingClientSelectableDeviceNumbers;
  boolean MaskingOneHardwareIDPerView;
  boolean MaskingExposeStorageVolumesToHostsSupported;
  boolean MaskingHideStorageVolumesFromHostsSupported;
  uint16  MaskingMaximumMapCount;
  uint16  iSCSITargetEndpointCreation;
  string  iSCSITargetEndpointCreationDescription;
  uint16  SupportedHostTypes[] = 15;
  string  OtherHostTypeDescriptions[];
  string  SupportedHostTypeDescriptions[];
  boolean SupportsFileSystemCreation;
  boolean SupportsFileServer;
  boolean SupportsFileServerCreation;
  boolean SupportsContinuouslyAvailableFileServer;
  uint16  SupportedFileServerProtocols[];
};
```

## Members

The **MSFT\_SMSystemCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemCapabilities** class has these properties.

<dl> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

</dd> <dt>

**iSCSITargetEndpointCreation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if iSCSITargetEndpoints are dynamically created and deleted in a node or preexisting and statically defined.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Preexisting_and_statically_defined"></span><span id="preexisting_and_statically_defined"></span><span id="PREEXISTING_AND_STATICALLY_DEFINED"></span>

**Preexisting and statically defined** (1)


</dt> <dd></dd> <dt>

<span id="Dynamically_created_and_deleted"></span><span id="dynamically_created_and_deleted"></span><span id="DYNAMICALLY_CREATED_AND_DELETED"></span>

**Dynamically created and deleted** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**iSCSITargetEndpointCreationDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the value in the **iSCSITargetEndpointCreation** property.

</dd> <dt>

**MaskingClientSelectableDeviceNumbers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if this storage system allows the client to specify the *DeviceNumber* parameter when calling the Controller Configuration Service **AttachDevice** method or **ExposePaths** method. Set to **False** if the implementation does not allow unit numbers to vary for a ProtocolController.

</dd> <dt>

**MaskingExposeStorageVolumesToHostsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if this storage system supports the **ExposePaths** method.

</dd> <dt>

**MaskingHideStorageVolumesFromHostsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if this storage system supports the **HidePaths** method.

</dd> <dt>

**MaskingMaximumMapCount**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of ProtocolControllerForUnit associations that can be associated with a single LogicalDevice (for example, StorageVolume). Zero indicates there is no limit.

</dd> <dt>

**MaskingOneHardwareIDPerView**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if this storage system limits configurations to a single subject hardware ID per view. Set to **False** multiple hardware ID types can be used. The default is **False**.

</dd> <dt>

**MaskingOtherValidHardwareIDTypes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Describe types for [**MSFT\_SMStorageHardwareID**](msft-smstoragehardwareid.md).**IDType** when the **IdType** is **Other**.

</dd> <dt>

**MaskingPortsPerView**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the way that ports per view (ProtocolController) are handled by the underlying storage system.

The possible values are.

<dt>

<span id="One_Port_per_View"></span><span id="one_port_per_view"></span><span id="ONE_PORT_PER_VIEW"></span>

**One Port per View** (2)


</dt> <dd></dd> <dt>

<span id="Multiple_Ports_per_View"></span><span id="multiple_ports_per_view"></span><span id="MULTIPLE_PORTS_PER_VIEW"></span>

**Multiple Ports per View** (3)


</dt> <dd></dd> <dt>

<span id="All_Ports_share_the_same_View"></span><span id="all_ports_share_the_same_view"></span><span id="ALL_PORTS_SHARE_THE_SAME_VIEW"></span>

**All Ports share the same View** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**MaskingPortsPerViewDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the value in the **MaskingPortsPerView** property.

</dd> <dt>

**MaskingValidHardwareIdTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The string values that correspond to *MaskingValidHardwareIdTypes* values.

</dd> <dt>

**MaskingValidHardwareIdTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

A list of the valid values for [**MSFT\_SMStorageHardwareID**](msft-smstoragehardwareid.md).**IDType**.

The possible values are.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="PortWWN"></span><span id="portwwn"></span><span id="PORTWWN"></span>

**PortWWN** (2)


</dt> <dd></dd> <dt>

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>

**NodeWWN** (3)


</dt> <dd></dd> <dt>

<span id="Hostname"></span><span id="hostname"></span><span id="HOSTNAME"></span>

**Hostname** (4)


</dt> <dd></dd> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>

**iSCSI Name** (5)


</dt> <dd></dd> <dt>

<span id="SwitchWWN"></span><span id="switchwwn"></span><span id="SWITCHWWN"></span>

**SwitchWWN** (6)


</dt> <dd></dd> <dt>

<span id="SAS_Address"></span><span id="sas_address"></span><span id="SAS_ADDRESS"></span>

**SAS Address** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**MaximumReplicasPerSourceClone**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of replicas that can be associated with one source element.

</dd> <dt>

**MaximumReplicasPerSourceMirror**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of replicas that can be associated with one source element.

</dd> <dt>

**MaximumReplicasPerSourceSnapshot**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of replicas that can be associated with one source element.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

</dd> <dt>

**OtherHostTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageClientSettingData.ClientTypes")
</dt> </dl>

The host type when the corresponding **SupportedHostTypes** entry is **Other**.

</dd> <dt>

**ReplicationSupportedTypeCloneLocal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this storage system supports replication type Clone Local.

</dd> <dt>

**ReplicationSupportedTypeCloneRemote**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this storage system supports replication type Clone Remote.

</dd> <dt>

**ReplicationSupportedTypeMirrorLocal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this storage system supports replication type Mirror Local.

</dd> <dt>

**ReplicationSupportedTypeMirrorRemote**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this storage system supports replication type Mirror Remote.

</dd> <dt>

**ReplicationSupportedTypeSnapshotLocal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this storage system supports replication type Snapshot Local.

</dd> <dt>

**ReplicationSupportedTypeSnapshotRemote**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this storage system supports replication type Snapshot Remote.

</dd> <dt>

**StorageConfigSupportsPoolCapacityExpansion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports Pool capacity expansion.

</dd> <dt>

**StorageConfigSupportsPoolCreation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports Pool creation.

</dd> <dt>

**StorageConfigSupportsPoolDeletion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports Pool deletion.

</dd> <dt>

**StorageConfigSupportsPoolModification**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports Pool modification.

</dd> <dt>

**StorageConfigSupportsStorageVolumeCapacityExpansion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports storage volume capacity expansion.

</dd> <dt>

**StorageConfigSupportsStorageVolumeCapacityReduction**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports storage volume capacity reduction.

</dd> <dt>

**StorageConfigSupportsStorageVolumeCreation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports storage volume creation.

</dd> <dt>

**StorageConfigSupportsStorageVolumeDeletion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports storage volume deletion.

</dd> <dt>

**StorageConfigSupportsStorageVolumeModification**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports storage volume modification.

</dd> <dt>

**StorageConfigSupportsThinProvisionedPools**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage system supports thin provisioned pools.

</dd> <dt>

**SupportedFileServerProtocols**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of protocol values supported for file server creation.

**Windows Server 2012 and Windows Server 2012 R2:  **

Not supported

</dd> <dt>

**SupportedHostTypeDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

String values for the corresponding entries in the **SupportedHostTypes** property.

</dd> <dt>

**SupportedHostTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Defines the operating system, version, driver, and other host environment factors that influence the behavior exposed by storage systems.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Standard"></span><span id="standard"></span><span id="STANDARD"></span>

**Standard** (2)


</dt> <dd></dd> <dt>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>

**Solaris** (3)


</dt> <dd></dd> <dt>

<span id="HPUX"></span><span id="hpux"></span>

**HPUX** (4)


</dt> <dd></dd> <dt>

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>

**OpenVMS** (5)


</dt> <dd></dd> <dt>

<span id="Tru64"></span><span id="tru64"></span><span id="TRU64"></span>

**Tru64** (6)


</dt> <dd></dd> <dt>

<span id="Netware"></span><span id="netware"></span><span id="NETWARE"></span>

**Netware** (7)


</dt> <dd></dd> <dt>

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>

**Sequent** (8)


</dt> <dd></dd> <dt>

<span id="AIX"></span><span id="aix"></span>

**AIX** (9)


</dt> <dd></dd> <dt>

<span id="DGUX"></span><span id="dgux"></span>

**DGUX** (10)


</dt> <dd></dd> <dt>

<span id="Dynix"></span><span id="dynix"></span><span id="DYNIX"></span>

**Dynix** (11)


</dt> <dd></dd> <dt>

<span id="Irix"></span><span id="irix"></span><span id="IRIX"></span>

**Irix** (12)


</dt> <dd></dd> <dt>

<span id="Cisco_iSCSI_Storage_Router"></span><span id="cisco_iscsi_storage_router"></span><span id="CISCO_ISCSI_STORAGE_ROUTER"></span>

**Cisco iSCSI Storage Router** (13)


</dt> <dd></dd> <dt>

<span id="Linux"></span><span id="linux"></span><span id="LINUX"></span>

**Linux** (14)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows"></span><span id="microsoft_windows"></span><span id="MICROSOFT_WINDOWS"></span>

**Microsoft Windows** (15)


</dt> <dd></dd> <dt>

<span id="OS400"></span><span id="os400"></span>

**OS400** (16)


</dt> <dd></dd> <dt>

<span id="TRESPASS"></span><span id="trespass"></span>

**TRESPASS** (17)


</dt> <dd></dd> <dt>

<span id="HI-UX"></span><span id="hi-ux"></span>

**HI-UX** (18)


</dt> <dd></dd> <dt>

<span id="VMware_ESXi"></span><span id="vmware_esxi"></span><span id="VMWARE_ESXI"></span>

**VMware ESXi** (19)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows_Server_2008"></span><span id="microsoft_windows_server_2008"></span><span id="MICROSOFT_WINDOWS_SERVER_2008"></span>

**Microsoft Windows Server 2008** (20)


</dt> <dd></dd> <dt>

<span id="Microsoft_Windows_Server_2003"></span><span id="microsoft_windows_server_2003"></span><span id="MICROSOFT_WINDOWS_SERVER_2003"></span>

**Microsoft Windows Server 2003** (21)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>22–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SupportsContinuouslyAvailableFileServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if the storage system allows a continuously available file server to be created.

**Windows Server 2012 and Windows Server 2012 R2:  **

Not supported

</dd> <dt>

**SupportsFileServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if the storage system exposes file servers.

**Windows Server 2012 and Windows Server 2012 R2:  **

Not supported

</dd> <dt>

**SupportsFileServerCreation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if the storage system allows the creation of file servers.

**Windows Server 2012 and Windows Server 2012 R2:  **

Not supported

</dd> <dt>

**SupportsFileSystemCreation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **True** if the storage system allows the creation of file systems.

**Windows Server 2012 and Windows Server 2012 R2:  **

Not supported

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





