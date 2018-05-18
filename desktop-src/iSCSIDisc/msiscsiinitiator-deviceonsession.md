---
Description: 'The MSIscsiInitiator\_DeviceOnSession structure describes the characteristics of a device currently associated with a session.'
ms.assetid: '14ff764d-1c70-49d6-b1d1-81b751cf4c96'
title: 'MSIscsiInitiator\_DeviceOnSession class'
---

# MSIscsiInitiator\_DeviceOnSession class

The **MSIscsiInitiator\_DeviceOnSession** structure describes the characteristics of a device currently associated with a session.

## Syntax

``` syntax
class MSIscsiInitiator_DeviceOnSession
{
  string InitiatorName;
  string TargetName;
  uint8  ScsiPortNumber;
  uint8  ScsiPathId;
  uint8  ScsiTargetId;
  uint8  ScsiLun;
  string DeviceInterfaceGuid;
  string DeviceInterfaceName;
  string LegacyName;
  uint32 DeviceType;
  uint32 DeviceNumber;
  uint32 PartitionNumber;
};
```

## Members

The **MSIscsiInitiator\_DeviceOnSession** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_DeviceOnSession** class has these properties.

<dl> <dt>

**DeviceInterfaceGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The global unique identifier for the Plug-and-Play device interface. Device interface class GUIDs include, but are not limited to, the following:



| Value                                                                                                                                                                                                                | Meaning                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| <span id="GUID_DEVINTERFACE_DISK"></span><span id="guid_devinterface_disk"></span><dl> <dt>**GUID\_DEVINTERFACE\_DISK**</dt> </dl>                            | Disk<br/>            |
| <span id="GUID_DEVINTERFACE_TAPE"></span><span id="guid_devinterface_tape"></span><dl> <dt>**GUID\_DEVINTERFACE\_TAPE**</dt> </dl>                            | Tape<br/>            |
| <span id="GUID_DEVINTERFACE_CDROM"></span><span id="guid_devinterface_cdrom"></span><dl> <dt>**GUID\_DEVINTERFACE\_CDROM**</dt> </dl>                         | CD-ROM<br/>          |
| <span id="GUID_DEVINTERFACE_WRITEONCEDISK"></span><span id="guid_devinterface_writeoncedisk"></span><dl> <dt>**GUID\_DEVINTERFACE\_WRITEONCEDISK**</dt> </dl> | Write Once Disk<br/> |
| <span id="GUID_DEVINTERFACE_CDCHANGER"></span><span id="guid_devinterface_cdchanger"></span><dl> <dt>**GUID\_DEVINTERFACE\_CDCHANGER**</dt> </dl>             | CD Changer<br/>      |
| <span id="GUID_DEVINTERFACE_MEDIUMCHANGER"></span><span id="guid_devinterface_mediumchanger"></span><dl> <dt>**GUID\_DEVINTERFACE\_MEDIUMCHANGER**</dt> </dl> | Medium Changer<br/>  |
| <span id="GUID_DEVINTERFACE_FLOPPY"></span><span id="guid_devinterface_floppy"></span><dl> <dt>**GUID\_DEVINTERFACE\_FLOPPY**</dt> </dl>                      | Floppy<br/>          |



 

</dd> <dt>

**DeviceInterfaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the Plug-and-Play device interface.

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device number.

</dd> <dt>

**DeviceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The FILE\_DEVICE\_XXX type for this device.

</dd> <dt>

**InitiatorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the Initiator.

</dd> <dt>

**LegacyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the Legacy Device interface.

</dd> <dt>

**PartitionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the device is partitionable, the partition number of the device. Otherwise this property has a default value of -1

</dd> <dt>

**ScsiLun**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Operating System designated SCSI Logical Unit Number (LUN)

</dd> <dt>

**ScsiPathId**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Operating System designated SCSI path identifier or bus number

</dd> <dt>

**ScsiPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Operating System designated SCSI port number.

</dd> <dt>

**ScsiTargetId**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Operating System designated SCSI Target ID.

</dd> <dt>

**TargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the Target.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




