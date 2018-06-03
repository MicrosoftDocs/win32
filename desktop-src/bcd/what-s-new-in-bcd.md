---
title: What's New in the BCD WMI Provider
description: Windows 7 and Windows Server 2008 R2 include the following new programming elements in the Boot Configuration Data (BCD) Windows Management Instrumentation (WMI) provider.
ms.assetid: 4e6397fd-7083-4e9f-bbc5-2a7323bcb9ae
keywords:
- Boot Configuration Data WMI Provider Boot Config , what's new
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in the BCD WMI Provider

Windows 7 and Windows Server 2008 R2 include the following new programming elements in the Boot Configuration Data (BCD) Windows Management Instrumentation (WMI) provider.

## New Capabilities

The BCD WMI provider for Windows 7 and Windows Server 2008 R2 adds support for qualified partitions and virtual hard disks.

A *qualified partition* is a physical partition that is uniquely identified by its disk signature and either the partition offset for a disk that uses a master boot record (MBR) or the partition signature for a disk that uses a global partition table (GPT).

A *virtual hard disk* (VHD) is a file in VHD format that the operating system can use in the same ways as a physical hard disk, including as a boot device. For more information, see [About VHD](https://msdn.microsoft.com/library/windows/desktop/dd323654).

A BCD entry for a VHD boot device can be specified in the following ways:

-   As a *native VHD boot device*. If the VHD is mounted and has been assigned a volume, it can be specified as a native VHD boot device by calling the [**SetPartitionDeviceElement**](setpartitiondeviceelement-bcdobject.md) method with the corresponding partition path of the mounted VHD, in the same way as for a physical hard disk. A native VHD boot device entry has all of the information necessary to boot from the device including the VHD file name and path, the disk signature and partition identifier within the VHD (VPART) and the VHD file's parent disk signature and partition identifier (PPART).
-   As a *locate device*. If the disk signature and partition identifier within the VHD is omitted, it is necessary to search all VHD partitions to locate the partition that contains the boot device element (the application path for a device on which a boot application resides, or the system root for a device on which an operating system resides). This is a referred to as a *VPART locate device*. If the VHD file's parent disk signature and partition identifier is also omitted, it is also necessary to search all of the physical disks to locate the VHD file. This is referred to as a *VPART+PPART locate device*. A locate device can be specified by calling the [**SetVhdDeviceElement**](setvhddeviceelement-bcdobject.md) method.

## New Classes

<dl> <dt>

[**BcdDeviceLocateData**](bcddevicelocatedata.md)
</dt> <dd>

Represents the root class of all locate device data types and specifies the locate type of the device.

</dd> <dt>

[**BcdDeviceLocateElementChildData**](bcddevicelocateelementchilddata.md)
</dt> <dd>

Represents the element to locate within the VHD and specifies the VHD's parent file device for a VPART locate device.

</dd> <dt>

[**BcdDeviceLocateElementData**](bcddevicelocateelementdata.md)
</dt> <dd>

Represents a locate device element. This class is not used by the BCD WMI provider.

</dd> <dt>

[**BcdDeviceLocateStringData**](bcddevicelocatestringdata.md)
</dt> <dd>

Represents the parent of a VHD's parent file device and specifies the string to search for a VPART+PPART locate device.

</dd> <dt>

[**BcdDeviceQualifiedPartitionData**](bcddevicequalifiedpartitiondata.md)
</dt> <dd>

Represents a qualified partition device element.

</dd> </dl>

## New Methods of the BCDObject Class

<dl> <dt>

[**GetElementWithFlags**](getelementwithflags-bcdobject.md)
</dt> <dd>

Enumerates a qualified partition boot device.

</dd> <dt>

[**SetPartitionDeviceElementWithFlags**](setpartitiondeviceelementwithflags-bcdobject.md)
</dt> <dd>

Sets the specified partition device element. This method is the same as [**SetPartitionDeviceElement**](setpartitiondeviceelement-bcdobject.md) with additional options.

</dd> <dt>

[**SetQualifiedPartitionDeviceElement**](setqualifiedpartitiondeviceelement-bcdobject.md)
</dt> <dd>

Sets a qualified partition boot device.

</dd> <dt>

[**SetVhdDeviceElement**](setvhddeviceelement-bcdobject.md)
</dt> <dd>

Creates a VHD boot device.

</dd> </dl>

 

 




