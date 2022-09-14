---
description: Drive Object
ms.assetid: c1c17a97-cf4b-45b7-bc32-4bad94c3ddb2
title: Drive Object
ms.topic: article
ms.date: 05/31/2018
---

# Drive Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

A drive object models a physical disk drive that is contained within a subsystem. Each drive connects to a bus, occupies a slot, and contains a set of drive extents. Each drive can contribute extents to any number of LUNs. A drive can also be designated as a hot spare.

Use the [**IVdsSubSystem::QueryDrives**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-querydrives) method to determine the drives that are contained by a specific subsystem. Callers can get a pointer to a specific drive by selecting the desired drive object from the enumeration that is returned by the **QueryDrives** method, or by invoking the [**IVdsSubSystem::GetDrive**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-getdrive) method and passing in the desired bus and slot number. With a drive object, you can set the drive status and query for drive properties, associated drive extents, and the subsystem containing the drive.

In addition to an object identifier, a name, and a serial number, drive object properties include the drive status, health, and flags; the size in bytes; and a bus and slot number.

The following table lists related interfaces, enumerations, and structures.



| Type                                              | Element                                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsDrive**](/windows/desktop/api/Vds/nn-vds-ivdsdrive)                                                                                                                  |
| Interfaces that may be exposed by this object     | [**IVdsMaintenance**](/windows/desktop/api/Vds/nn-vds-ivdsmaintenance)                                                                                                      |
| Associated enumerations                           | [**VDS\_DRIVE\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_drive_flag), [**VDS\_DRIVE\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_drive_status), and [**VDS\_DRIVE\_EXTENT**](/windows/desktop/api/Vds/ns-vds-vds_drive_extent). |
| Associated structures                             | [**VDS\_DRIVE\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_drive_prop) and [**VDS\_DRIVE\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_drive_notification).                                      |



 

## Related topics

<dl> <dt>

[Hardware Provider Objects](hardware-provider-objects.md)
</dt> <dt>

[**IVdsSubSystem::QueryDrives**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-querydrives)
</dt> <dt>

[**IVdsSubSystem::GetDrive**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-getdrive)
</dt> </dl>

 

 
