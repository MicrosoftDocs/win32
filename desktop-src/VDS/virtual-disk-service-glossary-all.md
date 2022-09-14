---
description: This section provides a glossary of technical terms used in the Virtual Disk Service (VDS) documentation.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 1cf28cfb-ce96-4659-955d-0088bddcb9ce
title: Virtual Disk Service Glossary
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Disk Service Glossary

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

This section provides a glossary of technical terms used in the Virtual Disk Service (VDS) documentation.

<dl> <dt>

<span id="base.automagic_configuration"></span><span id="BASE.AUTOMAGIC_CONFIGURATION"></span>**automagic configuration**
</dt> <dd>

Hardware RAID provider that supplies a set of rules for choosing LUN logical block remapping based on simple attributes. Automagic providers can also dynamically alter the mapping for performance or fault management.

</dd> <dt>

<span id="base.binding_hints"></span><span id="BASE.BINDING_HINTS"></span>**automagic hints**
</dt> <dd>

Information supplied to an automagic provider to guide the LUN logical block configuration. Hints include information as to the desired fault tolerance, physical atomicity, and intended I/O access pattern.

</dd> <dt>

<span id="base.basic_disk"></span><span id="BASE.BASIC_DISK"></span>**basic disk**
</dt> <dd>

A disk managed by the simplest possible software provider. The basic disk provider supports only volumes that directly map to partition configuration data structures.

</dd> <dt>

<span id="base.binding"></span><span id="BASE.BINDING"></span>**binding**
</dt> <dd>

Selecting for a set of mappings to physical resources.

</dd> <dt>

<span id="base.convert"></span><span id="BASE.CONVERT"></span>**convert**
</dt> <dd>

The process of converting a basic disk to a dynamic disk.

</dd> <dt>

<span id="base.configuration"></span><span id="BASE.CONFIGURATION"></span>**configuration**
</dt> <dd>

A collection of the operating parameters that supply the mapping from a volume, or LUN, to physical resources.

</dd> <dt>

<span id="base.controller"></span><span id="BASE.CONTROLLER"></span>**controller**
</dt> <dd>

A software program that contains the runtime intelligence for a hardware provider.

</dd> <dt>

<span id="base.disk"></span><span id="BASE.DISK"></span>**disk**
</dt> <dd>

A physical disk or hardware RAID LUN. Disks are targets for runtime storage I/O load; Plug and Play (PNP) does not distinguish between JBOD and LUNs.

</dd> <dt>

<span id="base.disk_platter"></span><span id="BASE.DISK_PLATTER"></span>**disk platter**
</dt> <dd>

A subset of a pack used for exporting or importing volumes from a pack.

</dd> <dt>

<span id="base.disk_pack"></span><span id="BASE.DISK_PACK"></span>**disk pack**
</dt> <dd>

See *pack*.

</dd> <dt>

<span id="base.drive"></span><span id="BASE.DRIVE"></span>**drive**
</dt> <dd>

A physical disk spindle within a hardware RAID subsystem. Drives are bound into LUNs by the subsystem.

</dd> <dt>

<span id="base.dynamic_disk"></span><span id="BASE.DYNAMIC_DISK"></span>**dynamic disk**
</dt> <dd>

A disk managed by a software RAID provider with support for flexible volume reconfiguration. A dynamic disk uses a partition as a container for volumes; there is no guaranteed mapping.

</dd> <dt>

<span id="base.explicit_configuration"></span><span id="BASE.EXPLICIT_CONFIGURATION"></span>**explicit configuration**
</dt> <dd>

A configuration with the parameters, including the volume type and the exact layout, for a collection of target volumes.

</dd> <dt>

<span id="base.export"></span><span id="BASE.EXPORT"></span>**export**
</dt> <dd>

The act of moving a disk platter and all volumes contained on that platter out of a pack.

</dd> <dt>

<span id="base.extent"></span><span id="BASE.EXTENT"></span>**extent**
</dt> <dd>

A contiguous range of logical sectors contributing to a single volume or disk. An extent can also be range of unallocated sectors. Commonly, a file system displays the extent details to an end-user.

</dd> <dt>

<span id="base.guid_partition_table_gpt"></span><span id="BASE.GUID_PARTITION_TABLE_GPT"></span>**GUID Partition Table (GPT)**
</dt> <dd>

Structures used by EFI firmware. GPT is one of two lowest level software configuration data formats used by platform firmware to locate a bootable operating system or other executable image.

</dd> <dt>

<span id="base.hardware_provider"></span><span id="BASE.HARDWARE_PROVIDER"></span>**hardware provider**
</dt> <dd>

A collection of software that executes on the host, a bus adapter, and possibly an external storage subsystem that works together to surface and manage RAID LUNs. Hardware providers for most external storage subsystems contain only user-mode, host-based software.

</dd> <dt>

<span id="base.health"></span><span id="BASE.HEALTH"></span>**health**
</dt> <dd>

The current fault-management status of a volume or a LUN.

</dd> <dt>

<span id="base.hot_spotting"></span><span id="BASE.HOT_SPOTTING"></span>**hot sparing**
</dt> <dd>

Temporarily adding a volume plex to a volume.

</dd> <dt>

<span id="base.import"></span><span id="BASE.IMPORT"></span>**import**
</dt> <dd>

The act of moving a disk platter and all its volumes into an existing pack.

</dd> <dt>

<span id="base.JBOD"></span><span id="base.jbod"></span><span id="BASE.JBOD"></span>**just a bunch of disks (JBOD)**
</dt> <dd>

A collection of physical spindles without the coordinated control provided by a hardware RAID device.

</dd> <dt>

<span id="base.logical_block_number_LBN"></span><span id="base.logical_block_number_lbn"></span><span id="BASE.LOGICAL_BLOCK_NUMBER_LBN"></span>**logical block number (LBN)**
</dt> <dd>

The smallest addressable unit of storage data. LBN is used with I/O command protocols.

</dd> <dt>

<span id="base.logical_block_mapping"></span><span id="BASE.LOGICAL_BLOCK_MAPPING"></span>**logical block mapping**
</dt> <dd>

The transformation of the logical blocks presented to a provider to those exposed by the provider.

</dd> <dt>

<span id="base.logical_Unit_Number_LUN"></span><span id="base.logical_unit_number_lun"></span><span id="BASE.LOGICAL_UNIT_NUMBER_LUN"></span>**logical unit number (LUN)**
</dt> <dd>

A physically addressable storage unit as surfaced by a hardware RAID subsystem. This term can also refer to the SCSI identifier for the storage unit.

</dd> <dt>

<span id="base.LUN_number"></span><span id="base.lun_number"></span><span id="BASE.LUN_NUMBER"></span>**LUN number**
</dt> <dd>

A number that a VDS hardware provider assigns to a LUN in an array. This is not the same as the "logical unit number" in the disk's SCSI address.

</dd> <dt>

<span id="base.management_service"></span><span id="BASE.MANAGEMENT_SERVICE"></span>**management service**
</dt> <dd>

A software program that executes as needed to perform volume configuration, monitoring, or fault handling.

</dd> <dt>

<span id="base.mapping"></span><span id="BASE.MAPPING"></span>**mapping**
</dt> <dd>

A volume that is exposed to the operating system and has an associated volume name (a drive letter). A volume is accessible by a file system.

</dd> <dt>

<span id="base.masking"></span><span id="BASE.MASKING"></span>**masking**
</dt> <dd>

A disk not recognized by the operating system. A disk can be masked by the hardware RAID subsystem, switch, SCSI RESERVE by another computer host, or software in the disk stack.

</dd> <dt>

<span id="base.master_Boot_Record_partitioning_MBR"></span><span id="base.master_boot_record_partitioning_mbr"></span><span id="BASE.MASTER_BOOT_RECORD_PARTITIONING_MBR"></span>**master boot record partitioning (MBR)**
</dt> <dd>

MBR is one of two lowest level software configuration data formats, and is used by BIOS firmware to locate a bootable operating system image.

</dd> <dt>

<span id="base.member"></span><span id="BASE.MEMBER"></span>**member**
</dt> <dd>

A collection of concatenated disk extents contained on one more disks. A disk can contribute to only one member of a volume.

</dd> <dt>

<span id="base.mirror"></span><span id="BASE.MIRROR"></span>**mirror**
</dt> <dd>

A volume or disk mapping that maintains two or more identical data copies. The type of mapping is also called RAID Level 1.

</dd> <dt>

<span id="base.pack"></span><span id="BASE.PACK"></span>**pack**
</dt> <dd>

A collection of logical volumes and underlying disks. A pack is the unit of transitive closure for a volume. Dynamic disk packs and disk groups are terms for the same item.

</dd> <dt>

<span id="base.parity_stripe"></span><span id="BASE.PARITY_STRIPE"></span>**parity stripe**
</dt> <dd>

A volume or disk mapping that maintains parity check information as well as data. Each vendor supplies the exact mapping and protection scheme. Includes RAID 3, 4, 5, and 6.

</dd> <dt>

<span id="base.partially_directed_configuration"></span><span id="BASE.PARTIALLY_DIRECTED_CONFIGURATION"></span>**partially directed configuration**
</dt> <dd>

A volume or disk configuration that is not fully explicit. The binding type and a collection of target resources are specified; the actual layout is not. Partially directed configuration is the most common volume configuration.

</dd> <dt>

<span id="base.partition"></span><span id="BASE.PARTITION"></span>**partition**
</dt> <dd>

A contiguous range of logical sectors described by a single entry in the MBR or GPT structure. On basic disks, partitions directly correspond to simple volumes. Partition structures are shared between the BIOS or EFI platform firmware and an operating system or other bootable image.

</dd> <dt>

<span id="base.path"></span><span id="BASE.PATH"></span>**path**
</dt> <dd>

The access path from a computer to a disk or external hardware LUN.

</dd> <dt>

<span id="base.plex"></span><span id="BASE.PLEX"></span>**plex**
</dt> <dd>

One member of a mirrored volume or LUN.

</dd> <dt>

<span id="base.port"></span><span id="BASE.PORT"></span>**port**
</dt> <dd>

The endpoint of a path at a disk.

</dd> <dt>

<span id="base.redundant_array_of_independent_disks_RAID"></span><span id="base.redundant_array_of_independent_disks_raid"></span><span id="BASE.REDUNDANT_ARRAY_OF_INDEPENDENT_DISKS_RAID"></span>**redundant array of independent disks (RAID)**
</dt> <dd>

A collection of techniques for managing multiple disks.

</dd> <dt>

<span id="base.runtime_service"></span><span id="BASE.RUNTIME_SERVICE"></span>**runtime service**
</dt> <dd>

A software program that executes on an I/O-request basis.

</dd> <dt>

<span id="base.simple_disk"></span><span id="BASE.SIMPLE_DISK"></span>**simple disk**
</dt> <dd>

A spindle that is not connected to a hardware RAID controller. See also Just a Bunch Of Disks (JBOD).

</dd> <dt>

<span id="base.software_provider"></span><span id="BASE.SOFTWARE_PROVIDER"></span>**software provider**
</dt> <dd>

Host-based software that exposes logical volumes and operates on disks. A software provider includes kernel-mode runtime services, configuration data, and user-mode management services.

</dd> <dt>

<span id="base.span"></span><span id="BASE.SPAN"></span>**span**
</dt> <dd>

A volume or disk linear mapping of multiple discontinuous disk or drive extents. The extents can be on one or more spindles or LUNs.

</dd> <dt>

<span id="base.spindle"></span><span id="BASE.SPINDLE"></span>**spindle**
</dt> <dd>

A physical unit of disk storage.

</dd> <dt>

<span id="base.stacking"></span><span id="BASE.STACKING"></span>**stacking**
</dt> <dd>

The act of constructing a volume or LUN by performing more than one logical block mapping operation. An example is a mirrored striped volume. The most common stacking occurs when software RAID is used across LUNs constructed by hardware RAID.

</dd> <dt>

<span id="base.stripe"></span><span id="BASE.STRIPE"></span>**stripe**
</dt> <dd>

A volume or disk mapping that interleaves contiguous extents across multiple volumes, disks, or drives. This mapping is also called RAID 0.

</dd> <dt>

<span id="base.status"></span><span id="BASE.STATUS"></span>**status**
</dt> <dd>

The current availability of a volume, disk, or drive.

</dd> <dt>

<span id="base.subsystem"></span><span id="BASE.SUBSYSTEM"></span>**subsystem**
</dt> <dd>

The instantiation of hardware-provider software. A subsystem contains at least one controller and one drive. If the subsystem is external to the computer, one or more network paths connect the subsystem to the computer.

</dd> <dt>

<span id="base.jello"></span><span id="BASE.JELLO"></span>**transition state**
</dt> <dd>

Status of the logical to physical mapping that is undergoing change.

</dd> <dt>

<span id="base.uninitialized_disk"></span><span id="BASE.UNINITIALIZED_DISK"></span>**uninitialized disk**
</dt> <dd>

A disk that is not a member of a pack.

</dd> <dt>

<span id="base.unmasked_disk"></span><span id="BASE.UNMASKED_DISK"></span>**unmasked disk**
</dt> <dd>

A disk that is visible to the operating system. The contents of an unmasked disk are visible to software volume managers, file systems, and so on.

</dd> <dt>

<span id="base.volume"></span><span id="BASE.VOLUME"></span>**volume**
</dt> <dd>

A number of disk extents bound into a virtually contiguous range of logical blocks. A volume can be accessed through a drive letter, a mounted folder, or a volume GUID path.

</dd> </dl>

 

 
