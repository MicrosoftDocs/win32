---
description: Represents a device that can use media to store and retrieve data.
ms.assetid: c63b1731-dbc0-4e5e-acb8-cd91b5569dd2
title: CIM_MediaAccessDevice class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MediaAccessDevice
- CIM_MediaAccessDevice.Capabilities
- CIM_MediaAccessDevice.CapabilityDescriptions
- CIM_MediaAccessDevice.ErrorMethodology
- CIM_MediaAccessDevice.CompressionMethod
- CIM_MediaAccessDevice.NumberOfMediaSupported
- CIM_MediaAccessDevice.MaxMediaSize
- CIM_MediaAccessDevice.DefaultBlockSize
- CIM_MediaAccessDevice.MaxBlockSize
- CIM_MediaAccessDevice.MinBlockSize
- CIM_MediaAccessDevice.NeedsCleaning
- CIM_MediaAccessDevice.MediaIsLocked
- CIM_MediaAccessDevice.Security
- CIM_MediaAccessDevice.LastCleaned
- CIM_MediaAccessDevice.MaxAccessTime
- CIM_MediaAccessDevice.UncompressedDataRate
- CIM_MediaAccessDevice.LoadTime
- CIM_MediaAccessDevice.UnloadTime
- CIM_MediaAccessDevice.MountCount
- CIM_MediaAccessDevice.TimeOfLastMount
- CIM_MediaAccessDevice.TotalMountTime
- CIM_MediaAccessDevice.UnitsDescription
- CIM_MediaAccessDevice.MaxUnitsBeforeCleaning
- CIM_MediaAccessDevice.UnitsUsed
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_MediaAccessDevice class (Hyper-V management)

Represents a device that can use media to store and retrieve data.

## Syntax

``` syntax
[Abstract, Version("2.6.0"), UMLPackagePath("CIM::Device::StorageDevices"), AMENDMENT]
class CIM_MediaAccessDevice : CIM_LogicalDevice
{
  uint16   Capabilities[];
  string   CapabilityDescriptions[];
  string   ErrorMethodology;
  string   CompressionMethod;
  uint32   NumberOfMediaSupported;
  uint64   MaxMediaSize;
  uint64   DefaultBlockSize;
  uint64   MaxBlockSize;
  uint64   MinBlockSize;
  boolean  NeedsCleaning;
  boolean  MediaIsLocked;
  uint16   Security;
  datetime LastCleaned;
  uint64   MaxAccessTime;
  uint32   UncompressedDataRate;
  uint64   LoadTime;
  uint64   UnloadTime;
  uint64   MountCount;
  datetime TimeOfLastMount;
  uint64   TotalMountTime;
  string   UnitsDescription;
  uint64   MaxUnitsBeforeCleaning;
  uint64   UnitsUsed;
};
```

## Members

The **CIM\_MediaAccessDevice** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_MediaAccessDevice** class has these methods.



| Method                                               | Description                                                            |
|:-----------------------------------------------------|:-----------------------------------------------------------------------|
| [**LockMedia**](cim-mediaaccessdevice-lockmedia.md) | Locks and unlocks removable media in a media access device.<br/> |



 

### Properties

The **CIM\_MediaAccessDevice** class has these properties.

<dl> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Storage Devices\|001.9", "MIF.DMTF\|Storage Devices\|001.11", "MIF.DMTF\|Storage Devices\|001.12", "MIF.DMTF\|Disks\|003.7", "MIF.DMTF\|Host Disk\|001.2", "MIF.DMTF\|Host Disk\|001.4"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MediaAccessDevice**.**CapabilityDescriptions**")
</dt> </dl>

An array that contains the capabilities of the media access device.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Sequential_Access"></span><span id="sequential_access"></span><span id="SEQUENTIAL_ACCESS"></span>

**Sequential Access** (2)


</dt> <dd></dd> <dt>

<span id="Random_Access"></span><span id="random_access"></span><span id="RANDOM_ACCESS"></span>

**Random Access** (3)


</dt> <dd></dd> <dt>

<span id="Supports_Writing"></span><span id="supports_writing"></span><span id="SUPPORTS_WRITING"></span>

**Supports Writing** (4)


</dt> <dd></dd> <dt>

<span id="Encryption"></span><span id="encryption"></span><span id="ENCRYPTION"></span>

**Encryption** (5)


</dt> <dd></dd> <dt>

<span id="Compression"></span><span id="compression"></span><span id="COMPRESSION"></span>

**Compression** (6)


</dt> <dd></dd> <dt>

<span id="Supports_Removeable_Media"></span><span id="supports_removeable_media"></span><span id="SUPPORTS_REMOVEABLE_MEDIA"></span>

**Supports Removeable Media** (7)


</dt> <dd></dd> <dt>

<span id="Manual_Cleaning"></span><span id="manual_cleaning"></span><span id="MANUAL_CLEANING"></span>

**Manual Cleaning** (8)


</dt> <dd></dd> <dt>

<span id="Automatic_Cleaning"></span><span id="automatic_cleaning"></span><span id="AUTOMATIC_CLEANING"></span>

**Automatic Cleaning** (9)


</dt> <dd></dd> <dt>

<span id="SMART_Notification"></span><span id="smart_notification"></span><span id="SMART_NOTIFICATION"></span>

**SMART Notification** (10)


</dt> <dd></dd> <dt>

<span id="Supports_Dual_Sided_Media"></span><span id="supports_dual_sided_media"></span><span id="SUPPORTS_DUAL_SIDED_MEDIA"></span>

**Supports Dual Sided Media** (11)


</dt> <dd></dd> <dt>

<span id="Predismount_Eject_Not_Required"></span><span id="predismount_eject_not_required"></span><span id="PREDISMOUNT_EJECT_NOT_REQUIRED"></span>

**Predismount Eject Not Required** (12)


</dt> <dd></dd> </dl>

</dd> <dt>

**CapabilityDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MediaAccessDevice**.**Capabilities**")
</dt> </dl>

An array of feature descriptions for the items in the **Capabilities** array.

</dd> <dt>

**CompressionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the algorithm or tool used by the device to support compression.

If a compression type is not specified, one of the following values can be used:

-   "Unknown"   compression support is unknown or not specified.
-   "Compressed"   compression is supported but the type is unknown or unspecified.
-   "Not Compressed"   the device does not support compression capabilities.

</dd> <dt>

**DefaultBlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The default block size, in bytes, for the device.

</dd> <dt>

**ErrorMethodology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of error detection and correction supported by the device.

</dd> <dt>

**LastCleaned**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when the device was last cleaned.

</dd> <dt>

**LoadTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("MilliSeconds"), **PUnit** ("second \* 10^-3")
</dt> </dl>

The time it takes, in milliseconds, for the device to be able to read or write a media after the device starts loading. For example, for disk drives, this is the interval between a disk not spinning to the disk reporting that it is ready for read/write operations. For tape drives, this starts when media is inserted and ends when the drive reports that it is ready for an application. This is usually at the tape's beginning-of-tape (BOT) area.

</dd> <dt>

**MaxAccessTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("MilliSeconds"), **PUnit** ("second \* 10^-3")
</dt> </dl>

The maximum access time of the media, in milliseconds. For a disk drive, this represents full seek and full rotational delay. For tape drives, this represents a search from the beginning of the tape to the most physically distant point.

</dd> <dt>

**MaxBlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The maximum block size, in bytes, for media accessed by the device.

</dd> <dt>

**MaxMediaSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Sequential Access Devices\|001.2", "MIF.DMTF\|Host Disk\|001.5")
</dt> </dl>

The maximum size, in kilobytes, of media supported by this device.

</dd> <dt>

**MaxUnitsBeforeCleaning**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MediaAccessDevice**.**UnitsDescription**")
</dt> </dl>

The maximum number of units that can be used before the device should be cleaned. **UnitsDescription** defines how the unit type.

</dd> <dt>

**MediaIsLocked**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the media is locked in the device and can not be ejected; otherwise, **false**. For non-removable devices, this value should be **true**.

</dd> <dt>

**MinBlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The minimum block size, in bytes, for media accessed by the device.

</dd> <dt>

**MountCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Counter**
</dt> </dl>

The number of times that media has been mounted for data transfer or to clean the device. If the device does not support removable media, this property should be set to zero.

</dd> <dt>

**NeedsCleaning**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the device needs cleaning; otherwise, **false**.

> [!Note]  
> The **Capabilities** property indicates whether manual or automatic cleaning is possible.

 

</dd> <dt>

**NumberOfMediaSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the device supports multiple individual media, this property defines the maximum number which can be supported or inserted.

</dd> <dt>

**Security**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Disks\|003.22")
</dt> </dl>

The operational security for the device.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (3)


</dt> <dd></dd> <dt>

<span id="Read_Only"></span><span id="read_only"></span><span id="READ_ONLY"></span>

**Read Only** (4)


</dt> <dd></dd> <dt>

<span id="Locked_Out"></span><span id="locked_out"></span><span id="LOCKED_OUT"></span>

**Locked Out** (5)


</dt> <dd></dd> <dt>

<span id="Boot_Bypass"></span><span id="boot_bypass"></span><span id="BOOT_BYPASS"></span>

**Boot Bypass** (6)


</dt> <dd></dd> <dt>

<span id="Boot_Bypass_and_Read_Only"></span><span id="boot_bypass_and_read_only"></span><span id="BOOT_BYPASS_AND_READ_ONLY"></span>

**Boot Bypass and Read Only** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**TimeOfLastMount**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The most recent date and time when media was mounted on the device. This property is only used by devices that support removable media.

</dd> <dt>

**TotalMountTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time, in seconds, that media has been mounted for data transfer or to clean the device. If the device does not support removable media, this property should be set to zero.

</dd> <dt>

**UncompressedDataRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("KiloBytes per Second"), **PUnit** ("byte / second \* 10^3")
</dt> </dl>

The sustained data transfer rate in kilobytes at which the device can read and write to a media. This is a sustained, raw data rate. Maximum rates or rates with compression should not be reported in this property.

</dd> <dt>

**UnitsDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MediaAccessDevice**.**MaxUnitsBeforeCleaning**", "**CIM\_MediaAccessDevice**.**UnitsUsed**")
</dt> </dl>

Describes the unit type of the **MaxUnitsBeforeCleaning** and **UnitsUsed** properties.

</dd> <dt>

**UnitsUsed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Gauge**](/windows/desktop/WmiSdk/standard-qualifiers), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MediaAccessDevice**.**UnitsDescription**", "**CIM\_MediaAccessDevice**.**MaxUnitsBeforeCleaning**")
</dt> </dl>

The number of units used by the device. This property is used to determine when the device should be cleaned. **UnitsDescription** defines how the unit type.

</dd> <dt>

**UnloadTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("MilliSeconds"), **PUnit** ("second \* 10^-3")
</dt> </dl>

The time it takes, in milliseconds, for the device to transition from reading or writing media to unloading. For example, for disk drives, this is the interval between a disk spinning at nominal speeds and a disk not spinning. For tape drives, this is the time for a media to go from its BOT to being fully ejected and accessible to a picker element or human operator.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 

