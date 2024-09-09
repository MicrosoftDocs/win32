---
description: Volume Object
ms.assetid: 92013015-b0f5-4b92-937b-c2637f65810c
title: Volume Object
ms.topic: article
ms.date: 05/31/2018
---

# Volume Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/windows-hardware/drivers/storage/windows-storage-management-api-portal).\]

A volume object models a logical storage unit that is created by a software provider and presented to the file system as a disk. Each volume comprises at least one volume plex, which is in turn composed of extents from one or more disks.

## Volume Types

VDS supports five volume types: simple, spanned, striped, mirrored, and striped with parity. Simple, spanned, and striped volumes are non-fault tolerant; mirrored and parity volumes are fault tolerant. The remainder of this section describes each of the VDS volume types.

-   A simple volume is a portion of a physical disk that functions as though it were a physically separate unit. A simple volume can consist of a single region on a disk or multiple regions of the same disk that are linked together.
-   A spanned volume combines areas of unallocated space from multiple disks into one logical volume, allowing you to more efficiently use all of the space and all the drive letters on a multiple-disk system.
-   A striped volume is created by combining areas of free space on two or more disks into one logical volume. Striped volumes use RAID-0, which stripes data across multiple disks. Striped volumes cannot be extended or mirrored, and do not offer fault tolerance. If one of the disks containing a striped volume fails, the entire volume fails. When creating striped volumes, it is best to use disks that are of the same size, model, and manufacturer.
-   A mirrored volume is a fault-tolerant volume that provides data redundancy by using two copies, or plexes, of the volume to duplicate the data that is stored on the volume. All data that is written to the mirrored volume is written to both plexes, which are located on separate physical disks. If one of the physical disks fails, the data on the failed disk becomes unavailable, but the system continues to operate using the unaffected disk.
-   A striped with parity volume is a fault-tolerant volume with data and parity striped intermittently across three or more physical disks. If a portion of a physical disk fails, you can recreate the data that was on the failed portion from the remaining data and parity. This volume type (also called a RAID-5 volume) is a good solution for data redundancy in a computer environment in which most activity consists of reading data.

### Volume Creation

Basic and dynamic software providers support partially directed volume creation; a caller specifies only those attributes that are of particular interest, and allows the provider to choose the rest. VDS mounts a newly created volume automatically, except on Windows Server 2003, Enterprise Edition and Windows Server 2003, Datacenter Edition platforms.

### Working with Volumes

Always create a volume within the same pack as the disks that contribute to it. Use the [**IVdsPack::CreateVolume**](/windows/desktop/api/Vds/nf-vds-ivdspack-createvolume) method to create a new volume object. You can determine the volumes that are contained within a specific pack by invoking the [**QueryVolumes**](/windows/desktop/api/Vds/nf-vds-ivdspack-queryvolumes) method, also exposed by [**IVdsPack**](/windows/desktop/api/Vds/nn-vds-ivdspack). A caller can get a pointer to a specific volume by selecting the desired volume object from the enumeration that is returned by **QueryVolumes**. With a volume object, you can set the status; query for plexes; extend and shrink the volume; add, break, and remove plexes; and delete the volume.

In addition to an object identifier, a name, and a serial number, volume object properties include the volume type, size, status, health, transition state, flags, and a recommended file system type.

The following table lists related interfaces, enumerations, and structures.



| Type                                              | Element                                                                                                                                                                                                               |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsVolume**](/windows/desktop/api/Vds/nn-vds-ivdsvolume), [**IVdsVolumeMF**](/windows/desktop/api/Vds/nn-vds-ivdsvolumemf), [**IVdsVolumeMF2**](/windows/desktop/api/Vds/nn-vds-ivdsvolumemf2)\*, [**IVdsVolumeOnline**](/windows/desktop/api/Vds/nn-vds-ivdsvolumeonline)\*, and [**IVdsVolumeShrink**](/windows/desktop/api/Vds/nn-vds-ivdsvolumeshrink)\*. |
| Associated enumerations                           | [**VDS\_VOLUME\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_volume_flag), [**VDS\_VOLUME\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_volume_status), [**VDS\_VOLUME\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_volume_type), and [**VDS\_DISK\_EXTENT\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_disk_extent_type).            |
| Associated structures                             | [**VDS\_VOLUME\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_volume_prop) and [**VDS\_VOLUME\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_volume_notification).                                                                                                        |



 

**\*Windows Server 2003:** These interfaces are not supported until Windows Vista.

## Related topics

<dl> <dt>

[Software Provider Objects](software-provider-objects.md)
</dt> </dl>

 

 
