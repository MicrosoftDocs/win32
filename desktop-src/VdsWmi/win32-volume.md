---
title: Win32\_Volume class
description: The Win32\_Volume class represents an area of storage on a hard disk.
ms.assetid: '21a33e2b-5f31-459f-8b08-b991e2edc547'
keywords: ["Win32_Volume class", "Win32_Volume class, described"]
topic_type:
- apiref
api_name:
- Win32_Volume
- Win32_Volume.Access
- Win32_Volume.Automount
- Win32_Volume.Availability
- Win32_Volume.BlockSize
- Win32_Volume.Capacity
- Win32_Volume.Caption
- Win32_Volume.Compressed
- Win32_Volume.ConfigManagerErrorCode
- Win32_Volume.ConfigManagerUserConfig
- Win32_Volume.CreationClassName
- Win32_Volume.Description
- Win32_Volume.DeviceID
- Win32_Volume.DirtyBitSet
- Win32_Volume.DriveLetter
- Win32_Volume.DriveType
- Win32_Volume.ErrorCleared
- Win32_Volume.ErrorDescription
- Win32_Volume.ErrorMethodology
- Win32_Volume.FileSystem
- Win32_Volume.FreeSpace
- Win32_Volume.IndexingEnabled
- Win32_Volume.InstallDate
- Win32_Volume.Label
- Win32_Volume.LastErrorCode
- Win32_Volume.MaximumFileNameLength
- Win32_Volume.Name
- Win32_Volume.NumberOfBlocks
- Win32_Volume.PNPDeviceID
- Win32_Volume.PowerManagementCapabilities
- Win32_Volume.PowerManagementSupported
- Win32_Volume.Purpose
- Win32_Volume.QuotasEnabled
- Win32_Volume.QuotasIncomplete
- Win32_Volume.QuotasRebuilding
- Win32_Volume.Status
- Win32_Volume.StatusInfo
- Win32_Volume.SystemCreationClassName
- Win32_Volume.SystemName
- Win32_Volume.SerialNumber
- Win32_Volume.SupportsDiskQuotas
- Win32_Volume.SupportsFileBasedCompression
api_location:
- Vdswmi.dll
api_type:
- DllExport
---

# Win32\_Volume class

The **Win32\_Volume** class represents an area of storage on a hard disk. The class returns local volumes that are formatted, unformatted, mounted, or offline. A volume is formatted by using a file system, such as FAT or NTFS, and might have a drive letter assigned to it. One hard disk can have multiple volumes, and volumes can span multiple physical disks. The **Win32\_Volume** class does not support disk drive management.

**Windows XP and earlier:** This class is not available.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_Volume : CIM_StorageVolume
{
  uint16   Access;
  boolean  Automount;
  uint16   Availability;
  uint64   BlockSize;
  uint64   Capacity;
  string   Caption;
  boolean  Compressed;
  uint32   ConfigManagerErrorCode;
  boolean  ConfigManagerUserConfig;
  string   CreationClassName;
  string   Description;
  string   DeviceID;
  boolean  DirtyBitSet;
  string   DriveLetter;
  uint32   DriveType;
  boolean  ErrorCleared;
  string   ErrorDescription;
  string   ErrorMethodology;
  string   FileSystem;
  uint64   FreeSpace;
  boolean  IndexingEnabled;
  datetime InstallDate;
  string   Label;
  uint32   LastErrorCode;
  uint32   MaximumFileNameLength;
  string   Name;
  uint64   NumberOfBlocks;
  string   PNPDeviceID;
  uint16[] PowerManagementCapabilities;
  boolean  PowerManagementSupported;
  string   Purpose;
  boolean  QuotasEnabled;
  boolean  QuotasIncomplete;
  boolean  QuotasRebuilding;
  string   Status;
  uint16   StatusInfo;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   SerialNumber;
  boolean  SupportsDiskQuotas;
  boolean  SupportsFileBasedCompression;
};
```

## Members

The **Win32\_Volume** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_Volume** class has these methods.



| Method                                                                        | Description                                                                                                                                    |
|:------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddMountPoint**](addmountpoint-method-in-class-win32-volume.md)           | Adds a mount point directory for the volume.<br/>                                                                                        |
| [**Chkdsk**](chkdsk-method-in-class-win32-volume.md)                         | Invokes the [**Chkdsk**](chkdsk-method-in-class-win32-volume.md) operation on the volume.<br/>                                          |
| [**Defrag**](defrag-method-in-class-win32-volume.md)                         | Defragments the volume.<br/>                                                                                                             |
| [**DefragAnalysis**](defraganalysis-method-in-class-win32-volume.md)         | Generates a fragmentation analysis for the volume.<br/>                                                                                  |
| [**Dismount**](dismount-method-in-class-win32-volume.md)                     | Dismounts a volume from the file system.<br/>                                                                                            |
| [**ExcludeFromAutoChk**](excludefromautochk-method-in-class-win32-volume.md) | Excludes volumes from the [**Chkdsk**](chkdsk-method-in-class-win32-volume.md) operation to be run at the next reboot.<br/>             |
| [**Format**](format-method-in-class-win32-volume.md)                         | Formats the volume.<br/>                                                                                                                 |
| [**Mount**](mount-method-in-class-win32-volume.md)                           | Mounts a volume to the file system.<br/>                                                                                                 |
| [**ScheduleAutoChk**](scheduleautochk-method-in-class-win32-volume.md)       | Schedules [**Chkdsk**](chkdsk-method-in-class-win32-volume.md) to be run at the next reboot if the dirty bit of the volume is set.<br/> |



 

### Properties

The **Win32\_Volume** class has these properties.

<dl> <dt>

**Access**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes whether the media is readable. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496). This can be one of the following values.



| Value                                                                              | Meaning                                        |
|------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Unknown media.<br/>                      |
| <dl> <dt>1 (0x1)</dt> </dl> | The media is readable.<br/>              |
| <dl> <dt>2 (0x2)</dt> </dl> | The media is writable.<br/>              |
| <dl> <dt>3 (0x3)</dt> </dl> | The media is readable and writable.<br/> |
| <dl> <dt>4 (0x4)</dt> </dl> | "Write once" media.<br/>                 |



 

</dd> <dt>

**Automount**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, the volume is mounted to the file system automatically when the first I/O is issued. If false, the volume is not mounted until explicitly mounted by using the [**Mount**](mount-method-in-class-win32-volume.md) method, or by adding a drive letter or mount point.

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the availability and status of the device. Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884). This can be one of the following values.



| Value                                                                                | Meaning                                                                                                                                              |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>1 (0x1)</dt> </dl>   | Other<br/>                                                                                                                                     |
| <dl> <dt>2 (0x2)</dt> </dl>   | Unknown<br/>                                                                                                                                   |
| <dl> <dt>3 (0x3)</dt> </dl>   | Running or Full Power<br/>                                                                                                                     |
| <dl> <dt>4 (0x4)</dt> </dl>   | Warning<br/>                                                                                                                                   |
| <dl> <dt>5 (0x5)</dt> </dl>   | In Test<br/>                                                                                                                                   |
| <dl> <dt>6 (0x6)</dt> </dl>   | Not Applicable<br/>                                                                                                                            |
| <dl> <dt>7 (0x7)</dt> </dl>   | Power Off<br/>                                                                                                                                 |
| <dl> <dt>8 (0x8)</dt> </dl>   | Offline<br/>                                                                                                                                   |
| <dl> <dt>9 (0x9)</dt> </dl>   | Off Duty<br/>                                                                                                                                  |
| <dl> <dt>10 (0xA)</dt> </dl>  | Degraded<br/>                                                                                                                                  |
| <dl> <dt>11 (0xB)</dt> </dl>  | Not Installed<br/>                                                                                                                             |
| <dl> <dt>12 (0xC)</dt> </dl>  | Install Error<br/>                                                                                                                             |
| <dl> <dt>13 (0xD)</dt> </dl>  | Power Save - Unknown <br/> The device is known to be in a power save mode, but its exact status is unknown.<br/>                         |
| <dl> <dt>14 (0xE)</dt> </dl>  | Power Save - Low Power Mode <br/> The device is in a power save state, but still functioning, and may exhibit degraded performance.<br/> |
| <dl> <dt>15 (0xF)</dt> </dl>  | Power Save - Standby <br/> The device is not functioning, but could be brought to full power quickly.<br/>                               |
| <dl> <dt>16 (0x10)</dt> </dl> | Power Cycle<br/>                                                                                                                               |
| <dl> <dt>17 (0x11)</dt> </dl> | Power Save - Warning <br/> The device is in a warning state, but also in a power save mode.<br/>                                         |
| <dl> <dt>18 (0x12)</dt> </dl> | Paused<br/>                                                                                                                                    |
| <dl> <dt>19 (0x13)</dt> </dl> | Not Ready<br/>                                                                                                                                 |
| <dl> <dt>20 (0x14)</dt> </dl> | Not Configured<br/>                                                                                                                            |
| <dl> <dt>21 (0x15)</dt> </dl> | Quiesced<br/>                                                                                                                                  |



 

</dd> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size in bytes of the blocks in this storage extent. If there is a variable block size, then the maximum block size in bytes is specified. If the block size is unknown or if a block concept is not valid (for example, for Aggregate Extents, Memory, or LogicalDisks), the value is 1 (one). his property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the volume in bytes.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the area of storage. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Compressed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the volume exists as one compressed entity, such as a DoubleSpace volume. If file-based compression is supported, such as the NTFS file system, this property is **false.**

</dd> <dt>

**ConfigManagerErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the Win32 Configuration Manager error code. This can be one of the following values.



| Value                                                                                | Meaning                                                                                                                                                      |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl>   | This device is working properly.<br/>                                                                                                                  |
| <dl> <dt>1 (0x1)</dt> </dl>   | This device is not configured correctly.<br/>                                                                                                          |
| <dl> <dt>2 (0x2)</dt> </dl>   | Windows cannot load the driver for this device.<br/>                                                                                                   |
| <dl> <dt>3 (0x3)</dt> </dl>   | The driver for this device might be corrupted, or your system may be running low on memory or other resources.<br/>                                    |
| <dl> <dt>4 (0x4)</dt> </dl>   | This device is not working properly. One of its drivers or your registry might be corrupted.<br/>                                                      |
| <dl> <dt>5 (0x5)</dt> </dl>   | The driver for this device needs a resource that Windows cannot manage.<br/>                                                                           |
| <dl> <dt>6 (0x6)</dt> </dl>   | The boot configuration for this device conflicts with other devices.<br/>                                                                              |
| <dl> <dt>7 (0x7)</dt> </dl>   | Cannot filter.<br/>                                                                                                                                    |
| <dl> <dt>8 (0x8)</dt> </dl>   | The driver loader for the device is missing.<br/>                                                                                                      |
| <dl> <dt>9 (0x9)</dt> </dl>   | This device is not working properly because the controlling firmware is reporting the resources for the device incorrectly.<br/>                       |
| <dl> <dt>10 (0xA)</dt> </dl>  | This device cannot start.<br/>                                                                                                                         |
| <dl> <dt>11 (0xB)</dt> </dl>  | This device failed.<br/>                                                                                                                               |
| <dl> <dt>12 (0xC)</dt> </dl>  | This device cannot find enough free resources that it can use.<br/>                                                                                    |
| <dl> <dt>13 (0xD)</dt> </dl>  | Windows cannot verify this device's resources.<br/>                                                                                                    |
| <dl> <dt>14 (0xE)</dt> </dl>  | This device cannot work properly until you restart your computer.<br/>                                                                                 |
| <dl> <dt>15 (0xF)</dt> </dl>  | This device is not working properly because there is probably a re-enumeration problem.<br/>                                                           |
| <dl> <dt>16 (0x10)</dt> </dl> | Windows cannot identify all the resources this device uses.<br/>                                                                                       |
| <dl> <dt>17 (0x11)</dt> </dl> | This device is asking for an unknown resource type.<br/>                                                                                               |
| <dl> <dt>18 (0x12)</dt> </dl> | Reinstall the drivers for this device.<br/>                                                                                                            |
| <dl> <dt>19 (0x13)</dt> </dl> | Failure using the VxD loader.<br/>                                                                                                                     |
| <dl> <dt>20 (0x14)</dt> </dl> | Your registry might be corrupted.<br/>                                                                                                                 |
| <dl> <dt>21 (0x15)</dt> </dl> | System failure. Try changing the driver for this device. If that does not work, see your hardware documentation. Windows is removing this device.<br/> |
| <dl> <dt>22 (0x16)</dt> </dl> | This device is disabled.<br/>                                                                                                                          |
| <dl> <dt>23 (0x17)</dt> </dl> | System failure. Try changing the driver for this device. If that does not work, see your hardware documentation.<br/>                                  |
| <dl> <dt>24 (0x18)</dt> </dl> | This device is not present, is not working properly, or does not have all of its drivers installed.<br/>                                               |
| <dl> <dt>25 (0x19)</dt> </dl> | Windows is still setting up this device.<br/>                                                                                                          |
| <dl> <dt>26 (0x1A)</dt> </dl> | Windows is still setting up this device.<br/>                                                                                                          |
| <dl> <dt>27 (0x1B)</dt> </dl> | This device does not have a valid log configuration.<br/>                                                                                              |
| <dl> <dt>28 (0x1C)</dt> </dl> | The drivers for this device are not installed.<br/>                                                                                                    |
| <dl> <dt>29 (0x1D)</dt> </dl> | This device is disabled because the firmware of the device did not give it the required resources.<br/>                                                |
| <dl> <dt>30 (0x1E)</dt> </dl> | This device is using an Interrupt Request resource that another device is using.<br/>                                                                  |
| <dl> <dt>31 (0x1F)</dt> </dl> | This device is not working properly because Windows cannot load the drivers required for this device.<br/>                                             |



 

</dd> <dt>

**ConfigManagerUserConfig**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the device is using a user-defined configuration. Otherwise, **False**. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the name of the class or the subclass used in the creation of an instance of this class. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: Key
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898)

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier for the volume on this system. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**DirtyBitSet**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the [**Chkdsk**](chkdsk-method-in-class-win32-volume.md) method is automatically run by the system at the next restart.

</dd> <dt>

**DriveLetter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Drive letter assigned to a volume. This property is **NULL** for volumes without drive letters.

</dd> <dt>

**DriveType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Numeric value that corresponds to the type of disk drive that this logical disk represents.

The values are:



| Value                                                                              | Meaning                      |
|------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Unknown<br/>           |
| <dl> <dt>1 (0x1)</dt> </dl> | No Root Directory<br/> |
| <dl> <dt>2 (0x2)</dt> </dl> | Removable Disk<br/>    |
| <dl> <dt>3 (0x3)</dt> </dl> | Local Disk<br/>        |
| <dl> <dt>4 (0x4)</dt> </dl> | Network Drive<br/>     |
| <dl> <dt>5 (0x5)</dt> </dl> | Compact Disk<br/>      |
| <dl> <dt>6 (0x6)</dt> </dl> | RAM Disk<br/>          |



 

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the error reported in **LastErrorCode** is now cleared. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

More information about the error recorded in **LastErrorCode**, and information on any corrective actions that may be taken. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**ErrorMethodology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of error detection and correction supported by this storage extent. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496).

</dd> <dt>

**FileSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File system on the logical disk.

Example: NTFS

</dd> <dt>

**FreeSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Space, in bytes, available on the logical disk. This property is inherited from [**CIM\_LogicalDisk**](https://msdn.microsoft.com/library/aa387886).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**IndexingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, context indexing is enabled.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the object was installed. This property does not require a value to indicate that the object is installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Label**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Volume name of the logical disk. This property is **null** for volumes without a label. For FAT and FAT32 systems, the maximum length is 11 characters. For NTFS file systems, the maximum length is 32 characters.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last error code reported by the logical device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**MaximumFileNameLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum length, in characters, of a filename component supported by a Windows drive. A filename component is the portion of a filename between backslashes. This value can be used to indicate that long names are supported by the file system. For example, for a FAT file system that supports long names, the property stores the value 255—not the previous 8.3 indicator. Long names can be supported on systems that use the NTFS file system.

Example: 255

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**NumberOfBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of consecutive blocks, each block the size of the value contained in the **BlockSize** property, which form this storage extent. Total size of the storage extent can be calculated by multiplying the value of the **BlockSize** property by the value of this property. If the value of **BlockSize** is 1, this property is the total size of the storage extent. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**PNPDeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the Win32 Plug and Play device ID of the logical device. Example: \*PNP030b.

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16\[\]**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the specific power-related capabilities of the logical device. This can be one of the following values.



| Value                                                                              | Meaning                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Unknown<br/>                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>1 (0x1)</dt> </dl> | Not Supported<br/>                                                                                                                                                                                                                                                                                                                                                                           |
| <dl> <dt>2 (0x2)</dt> </dl> | Disabled<br/>                                                                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>3 (0x3)</dt> </dl> | Enabled<br/> The power management features are currently enabled but the exact feature set is unknown or the information is unavailable.<br/>                                                                                                                                                                                                                                          |
| <dl> <dt>4 (0x4)</dt> </dl> | Power Saving Modes Entered Automatically<br/> The device can change its power state based on usage or other criteria.<br/>                                                                                                                                                                                                                                                             |
| <dl> <dt>5 (0x5)</dt> </dl> | Power State Settable<br/> The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method is supported. This method is found on the parent [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes](https://msdn.microsoft.com/library/aa390351).<br/> |
| <dl> <dt>6 (0x6)</dt> </dl> | Power Cycling Supported<br/> The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle).<br/>                                                                                                                                                                                         |
| <dl> <dt>7 (0x7)</dt> </dl> | Timed Power-On Supported<br/> The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle) and *Time* set to a specific date and time, or interval, for power-on.<br/>                                                                                                                  |



 

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True**, if the device can be power managed (put into a power save state), otherwise **False**. This boolean does not indicate that power management features are currently enabled, or if enabled, what features are supported. Refer to the PowerManagementCapabilities array for this information. If this boolean is false, the integer value 1, for the string, "Not Supported", should be the only entry in the PowerManagementCapabilities array. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**Purpose**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the media and its use. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496).

</dd> <dt>

**QuotasEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, quota management is enabled for this volume.

</dd> <dt>

**QuotasIncomplete**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, quota management was used but is disabled. Incomplete refers to the information left in the file system after quota management is disabled.

</dd> <dt>

**QuotasRebuilding**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the file system is in the process of compiling information and setting the disk up for quota management.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Serial number of the volume.

Example: A8C3D032

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

The values are:

<dl><span id="_OK_"></span><span id="_ok_"></span><dt>

**"OK"**
</dt><span id="_Error_"></span><span id="_error_"></span><span id="_ERROR_"></span><dt>

**"Error"**
</dt><span id="_Degraded_"></span><span id="_degraded_"></span><span id="_DEGRADED_"></span><dt>

**"Degraded"**
</dt><span id="_Unknown_"></span><span id="_unknown_"></span><span id="_UNKNOWN_"></span><dt>

**"Unknown"**
</dt><span id="_Pred_Fail_"></span><span id="_pred_fail_"></span><span id="_PRED_FAIL_"></span><dt>

**"Pred Fail"**
</dt><span id="_Starting_"></span><span id="_starting_"></span><span id="_STARTING_"></span><dt>

**"Starting"**
</dt><span id="_Stopping_"></span><span id="_stopping_"></span><span id="_STOPPING_"></span><dt>

**"Stopping"**
</dt><span id="_Service_"></span><span id="_service_"></span><span id="_SERVICE_"></span><dt>

**"Service"**
</dt><span id="_Stressed_"></span><span id="_stressed_"></span><span id="_STRESSED_"></span><dt>

**"Stressed"**
</dt><span id="_NonRecover_"></span><span id="_nonrecover_"></span><span id="_NONRECOVER_"></span><dt>

**"NonRecover"**
</dt><span id="_No_Contact_"></span><span id="_no_contact_"></span><span id="_NO_CONTACT_"></span><dt>

**"No Contact"**
</dt><span id="_Lost_Comm_"></span><span id="_lost_comm_"></span><span id="_LOST_COMM_"></span><dt>

**"Lost Comm"**
</dt> </dl>

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the state of the logical device. This can be one of the following values.



| Value                                                                              | Meaning                   |
|------------------------------------------------------------------------------------|---------------------------|
| <dl> <dt>1 (0x1)</dt> </dl> | Other<br/>          |
| <dl> <dt>2 (0x2)</dt> </dl> | Unknown<br/>        |
| <dl> <dt>3 (0x3)</dt> </dl> | Enabled<br/>        |
| <dl> <dt>4 (0x4)</dt> </dl> | Disabled<br/>       |
| <dl> <dt>5 (0x5)</dt> </dl> | Not Applicable<br/> |



 

</dd> <dt>

**SupportsDiskQuotas**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the volume supports disk quotas.

</dd> <dt>

**SupportsFileBasedCompression**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the logical disk partition supports file-based compression, such as is the case with the NTFS file system. This property is **False** when the **Compressed** property is **True**.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the system's creation class name.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the system's name.

</dd> </dl>

## Examples

The [Two WMI Functions](http://gallery.technet.microsoft.com/Two-WMI-Functions-94c31b5f) PowerShell example in the TechNet Gallery use **Win32\_Volume** to recreate the Windows 8 get-Volume cmdlet.

The following PowerShell sample retrieves the allocation size of the drives on the target system.


```PowerShell
$wql = "SELECT BlockSize,DriveLetter,Label FROM Win32_Volume WHERE FileSystem='NTFS'"
Get-WmiObject -Query $wql -ComputerName '.' | Select-Object DriveLetter,Label,BlockSize | Format-Table -AutoSize
```



The following PowerShell sample displays information on the volumes on the local system.


```PowerShell
$volumes = get-wmiobject Win32_Volume
foreach ($vol in $volumes) {
    "Volume: {0}" -f ++$i
    "============================="
    $vol | Format-List 
}
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Storage Volume Provider](storage-volume-provider.md)
</dt> <dt>

[**Win32\_VolumeQuota**](win32-volumequota.md)
</dt> <dt>

[**Win32\_VolumeUserQuota**](win32-volumeuserquota.md)
</dt> <dt>

[**Win32\_DefragAnalysis**](win32-defraganalysis.md)
</dt> <dt>

[**Win32\_MountPoint**](win32-mountpoint.md)
</dt> </dl>

 

 





