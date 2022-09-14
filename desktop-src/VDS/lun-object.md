---
description: LUN Object
ms.assetid: ea22bd6d-4a7a-4674-82e9-08460914ff8e
title: LUN Object
ms.topic: article
ms.date: 05/31/2018
---

# LUN Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

A LUN (logical unit number) object models a logical unit of addressable storage space that is created by a hardware provider and surfaced by a subsystem. Each LUN comprises at least one LUN plex, which is in turn composed of extents from one or more drives.

## LUN Types

VDS supports five LUN types: simple, spanned, striped, mirrored, and striped with parity. Simple, spanned, and striped LUNs are non-fault tolerant; mirrored and parity LUNs are fault tolerant. The remainder of this section describes each of the VDS LUN types.

-   A simple LUN is a non-fault tolerant LUN that is made up of a single contiguous drive extent from a single drive. The contiguous extent can comprise of a single range of blocks or multiple ranges of blocks linked together.
-   A spanned LUN is a non-fault tolerant LUN that is made up of multiple discontiguous extents from multiple drives. Data is written linearly to each of the extents on the first drive until all of the first drive extents are filled, and then to each of the extents on the second drive, and so on. Spanned LUNs provide for efficient use of drive space in subsystems that comprise of drives of various sizes.
-   A striped LUN is a non-fault tolerant LUN made up of multiple, interleaved, contiguous extents from multiple drives. Striped LUNs use a RAID-0 configuration, such that data is "striped" cyclically across the extents on the contributing drives. Striped LUNs work best with drives of the same size, model, and manufacturer.
-   Mirrored LUNs are fault tolerant LUNs that provide for disaster recovery by duplicating the data to multiple LUN plexes. Each plex in a mirrored LUN contains a copy of the data that is stored on the original plex. Each of the plexes resides on a separate drive. All data that is written to a mirrored LUN is written simultaneously to each of its plexes. Should one of the contributing drives fail, the plex on that drive becomes unavailable, but the system continues to operate using the unaffected plex or plexes. A mirrored LUN can have any number of plexes.
-   Striped with parity LUNs are fault-tolerant LUNs that provide for disaster recovery by striping parity data intermittently across three or more drives. Should one of the contributing drives fail, the lost data can be recreated from the remaining data and parity.

## LUN Creation

VDS supports four models by which applications can create LUNs: explicitly directed, partially directed, automagic, and vendor-specific. All hardware providers must support explicitly and partially directed LUN creation, and are strongly encouraged to support automagic LUN creation. (Vendor-specific LUN creation is outside the scope of this guide.)

Explicitly directed LUN creation enables the caller to specify all of the attributes of the LUN. Partially directed LUN creation enables the caller to specify only those attributes that are of particular interest, and then allows the provider to choose the rest. Automagic LUN creation involves enabling the caller to simply specify the LUN type and size along with a set of "automagic hints" (predefined preferences for LUN attributes), and then allowing the provider to create the LUN automatically.

## LUN Masking

VDS supports LUN unmasking for subsystems that offer this capability. All LUNs are surfaced to the computer on which the provider is running. LUN unmasking allows a caller to "unmask" selected LUNs to other computers on the network. If you unmask a LUN to a computer, the computer has access to the LUN. Computers for which a LUN is masked do not.

An unmasked LUN exposes both the [**IVdsLun**](/windows/desktop/api/Vds/nn-vds-ivdslun) and [**IVdsDisk**](/windows/desktop/api/Vds/nn-vds-ivdsdisk) interfaces to the local host. You can use **IVdsDisk** to add a LUN to a software-provider pack, create and remove volumes, assign drive letters, and so on. For more information about the operations performed on a disk, see the [Disk Object](disk-object.md).

After a LUN is unmasked to a target machine or masked from a target machine, the LUN's visibility on that machine may not change until a bus rescan is performed. The VDS application on the target machine initiates the bus rescan by calling [**IVdsService::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdsservice-reenumerate). The initiating of the bus rescan is the responsibility of the VDS application, not the hardware provider.

## LUN Multipathing

Hardware providers that support multipath I/O (MPIO) can set load balancing policies on paths between a LUN and the local host. LUNs that support this capability expose the [**IVdsLunMpio**](/windows/desktop/api/Vds/nn-vds-ivdslunmpio) interface to the local host.

## Working with LUNs

Use the [**IVdsSubSystem::CreateLun**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-createlun) method to create a new LUN object. You can query the LUNs that are surfaced by a specific subsystem by invoking the [**QueryLuns**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-queryluns) method, also exposed by [**IVdsSubSystem**](/windows/desktop/api/Vds/nn-vds-ivdssubsystem). A caller can get a pointer to a specific LUN by selecting the desired LUN object from the enumeration that is returned by **QueryLuns**. With a LUN object, you can set the LUN status; query for all active controllers, plexes, and automagic hints; extend and shrink the LUN; add and remove plexes; set masks; apply hints; and delete the LUN.

In addition to an object identifier, a name, and a serial number, LUN object properties include the LUN type, size, status, health, transition state, and flags; an unmasking list; and a rebuild priority setting.

The following table lists related interfaces, enumerations, and structures.



| Type                                                                                              | Element                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object                                                 | [**IVdsLun**](/windows/desktop/api/Vds/nn-vds-ivdslun)                                                                                                                                                                                                                                                                                          |
| Interfaces that are always exposed by this object in VDS 1.1 and 2.0 Fibre Channel providers only | [**IVdsLunControllerPorts**](/windows/desktop/api/Vds/nn-vds-ivdsluncontrollerports)                                                                                                                                                                                                                                                            |
| Interfaces that are always exposed by this object in VDS 1.1 and 2.0 iSCSI providers only         | [**IVdsLunIscsi**](/windows/desktop/api/Vds/nn-vds-ivdsluniscsi)                                                                                                                                                                                                                                                                                |
| Interfaces that may be exposed by this object\*                                                   | [**IVdsMaintenance**](/windows/desktop/api/Vds/nn-vds-ivdsmaintenance), [**IVdsLunMpio**](/windows/desktop/api/Vds/nn-vds-ivdslunmpio), [**IVdsLunNaming**](/windows/desktop/api/Vds/nn-vds-ivdslunnaming), and [**IVdsLunNumber**](/windows/desktop/api/Vds/nn-vds-ivdslunnumber)**Windows Server 2008, Windows Vista and Windows Server 2003:** The [**IVdsLunNumber**](/windows/desktop/api/Vds/nn-vds-ivdslunnumber) interface is not supported.<br/> |
| Associated enumerations                                                                           | [**VDS\_LUN\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_lun_flag) and [**VDS\_LUN\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_lun_status), and [**VDS\_LUN\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_lun_type)                                                                                                                                                                                   |
| Associated structures                                                                             | [**VDS\_LUN\_INFORMATION**](/windows/desktop/api/VdsLun/ns-vdslun-vds_lun_information), [**VDS\_LUN\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_lun_prop), and [**VDS\_LUN\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_lun_notification)                                                                                                                                                            |



 

\* See [Disk Object](disk-object.md) for additional interface ([**IVdsDisk**](/windows/desktop/api/Vds/nn-vds-ivdsdisk)) that is exposed if the LUN is unmasked as a disk on the local host computer.

## Related topics

<dl> <dt>

[Hardware Provider Objects](hardware-provider-objects.md)
</dt> <dt>

[Pack Object](pack-object.md)
</dt> <dt>

[Disk Object](disk-object.md)
</dt> <dt>

[**IVdsLun**](/windows/desktop/api/Vds/nn-vds-ivdslun)
</dt> <dt>

[**IVdsDisk**](/windows/desktop/api/Vds/nn-vds-ivdsdisk)
</dt> <dt>

[Adding a Drive Letter to a LUN](adding-a-drive-letter-to-a-lun.md)
</dt> </dl>

 

