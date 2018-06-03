---
title: DISK\_PERFORMANCE structure
description: The DISK\_PERFORMANCE structure is used in conjunction with the IOCTL\_DISK\_PERFORMANCE request to collect summary disk statistics for purposes of measuring disk performance.
ms.assetid: 34d954db-4220-4a3f-849c-f1164e6130f7
keywords:
- DISK_PERFORMANCE structure Storage Devices
- PDISK_PERFORMANCE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DISK_PERFORMANCE
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DISK\_PERFORMANCE structure

The DISK\_PERFORMANCE structure is used in conjunction with the [**IOCTL\_DISK\_PERFORMANCE**](ioctl-disk-performance.md) request to collect summary disk statistics for purposes of measuring disk performance.

## Syntax


```C++
typedef struct _DISK_PERFORMANCE {
  LARGE_INTEGER BytesRead;
  LARGE_INTEGER BytesWritten;
  LARGE_INTEGER ReadTime;
  LARGE_INTEGER WriteTime;
  LARGE_INTEGER IdleTime;
  ULONG         ReadCount;
  ULONG         WriteCount;
  ULONG         QueueDepth;
  ULONG         SplitCount;
  LARGE_INTEGER QueryTime;
  ULONG         StorageDeviceNumber;
  WCHAR         StorageManagerName[8];
} DISK_PERFORMANCE, *PDISK_PERFORMANCE;
```



## Members

<dl> <dt>

**BytesRead**
</dt> <dd>

Contains a cumulative count of bytes read from the disk since the performance counters were enabled.

</dd> <dt>

**BytesWritten**
</dt> <dd>

Contains a cumulative count of bytes written to the disk since the performance counters were enabled.

</dd> <dt>

**ReadTime**
</dt> <dd>

Contains a cumulative time, expressed in increments of 100 nanoseconds, spent on disk reads since the performance counters were enabled.

</dd> <dt>

**WriteTime**
</dt> <dd>

Contains a cumulative time, expressed in increments of 100 nanoseconds, spent on disk reads since the performance counters were enabled.

</dd> <dt>

**IdleTime**
</dt> <dd>

Contains a cumulative time, expressed in increments of 100 nanoseconds, since the performance counters were enabled in which there was no disk activity.

</dd> <dt>

**ReadCount**
</dt> <dd>

Contains the number of disk accesses for reads since the performance counters were enabled.

</dd> <dt>

**WriteCount**
</dt> <dd>

Contains the number of disk accesses for writes since the performance counters were enabled.

</dd> <dt>

**QueueDepth**
</dt> <dd>

Contains a snapshot of the number of queued disk I/O requests at the time that the query for performance statistics was performed.

</dd> <dt>

**SplitCount**
</dt> <dd>

Contains the number of disk accesses by means of an associated IRP since the performance counters were enabled.

</dd> <dt>

**QueryTime**
</dt> <dd>

Contains a timestamp indicating the system time at the moment that the query took place. System time is a count of 100-nanosecond intervals since January 1, 1601. System time is typically updated approximately every ten milliseconds. For more information about system time, see [**KeQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff553068).

</dd> <dt>

**StorageDeviceNumber**
</dt> <dd>

Contains a unique number assigned to every disk or volume across a particular storage type. The storage types are *disk.sys*, *ftdisk.sys*, and *dmio.sys*.

</dd> <dt>

**StorageManagerName**
</dt> <dd>

Contains an 8-character string that indicates which device driver provided the performance statistics. In Windows 2000, this can be either "LogiDisk" for the driver *logidisk.sys* or "PhysDisk" for the driver *physdisk.sys*. These drivers collect performance statistics for devices and physical disks respectively. In Windows XP and later operating systems, this can be any of the following three strings: "FTDISK" for the driver *ftdisk.sys*, "DMIO" for the driver *dmio.sys*, or PARTMGR" for the driver *partmgr.sys*. These three drivers collect performance statistics for basic disk volumes, dynamic disk volumes, and physical disks respectively. Note that these strings are 8-character case-sensitive strings with blank fill. For example, in the case of the string "FTDISK", the **StorageManagerName** character array should contain two trailing blanks ("FTDISK&lt;b&gt;&lt;b&gt;"), and in the case of the string "DMIO", the array should contain four trailing blanks ("DMIO&lt;b&gt;&lt;b&gt;&lt;b&gt;&lt;b&gt;").

</dd> </dl>

## Remarks

Counting halts whenever the performance counters are disabled, but the counters are not reset, so the cumulative values assigned to the structure members might potentially reflect disk activity across several enablings and disablings of the counters.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_PERFORMANCE**](ioctl-disk-performance.md)
</dt> <dt>

[**IOCTL\_DISK\_PERFORMANCE\_OFF**](ioctl-disk-performance-off.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_PERFORMANCE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






