---
Description: 'Windows Server 2008 R2.'
ms.assetid: '4ab37529-8d56-47a3-ad3d-0197cabd4f87'
title: 'What's New in VDS in Windows Server 2008 R2 and Windows 7'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in VDS in Windows Server 2008 R2 and Windows 7

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](https://msdn.microsoft.com/library/windows/desktop/hh830613).\]

Windows Server 2008 R2 and Windows 7 introduce the following changes to the Virtual Disk Service (VDS):

-   [New VDS Interfaces](#new-vds-interfaces)
-   [New VDS Enumerations](#new-vds-enumerations)
-   [New VDS Structures](#new-vds-structures)
-   [Modifications to Existing VDS Enumerations](#modifications-to-existing-vds-enumerations)
-   [Modifications to Existing VDS Structures](#modifications-to-existing-vds-structures)

## New VDS Interfaces

<dl>

[**IVdsDisk3**](/windows/desktop/api/Vds/nn-vds-ivdsdisk3)  
[**IVdsDiskPartitionMF2**](/windows/desktop/api/Vds/nn-vds-ivdsdiskpartitionmf2)  
[**IVdsDrive2**](/windows/desktop/api/Vds/nn-vds-ivdsdrive2)  
[**IVdsHwProviderStoragePools**](/windows/desktop/api/Vds/nn-vds-ivdshwproviderstoragepools)  
[**IVdsLun2**](/windows/desktop/api/Vds/nn-vds-ivdslun2)  
[**IVdsLunNumber**](/windows/desktop/api/Vds/nn-vds-ivdslunnumber)  
[**IVdsOpenVDisk**](/windows/desktop/api/Vds/nn-vds-ivdsopenvdisk)  
[**IVdsStoragePool**](/windows/desktop/api/Vds/nn-vds-ivdsstoragepool)  
[**IVdsSubSystem2**](/windows/desktop/api/Vds/nn-vds-ivdssubsystem2)  
[**IVdsSubSystemInterconnect**](/windows/desktop/api/Vds/nn-vds-ivdssubsysteminterconnect)  
[**IVdsVDisk**](/windows/desktop/api/Vds/nn-vds-ivdsvdisk)  
[**IVdsVdProvider**](/windows/desktop/api/Vds/nn-vds-ivdsvdprovider)  
[**IVdsVolume2**](/windows/desktop/api/Vds/nn-vds-ivdsvolume2)  
[**IVdsVolumeMF3**](/windows/desktop/api/Vds/nn-vds-ivdsvolumemf3)  
</dl>

## New VDS Enumerations

<dl>

[**VDS\_DISK\_OFFLINE\_REASON**](/windows/desktop/api/Vds/ne-vds-_vds_disk_offline_reason)  
[**VDS\_FORMAT\_OPTION\_FLAGS**](/windows/desktop/api/Vds/ne-vds-_vds_format_option_flags)  
[**VDS\_INTERCONNECT\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_interconnect_flag)  
[**VDS\_RAID\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_raid_type)  
[**VDS\_STORAGE\_POOL\_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_storage_pool_status)  
[**VDS\_STORAGE\_POOL\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_storage_pool_type)  
[**VDS\_SUB\_SYSTEM\_SUPPORTED\_RAID\_TYPE\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_sub_system_supported_raid_type_flag)  
[**VDS\_VDISK\_STATE**](/windows/desktop/api/Vds/ne-vds-_vds_vdisk_state)  
</dl>

## New VDS Structures

<dl>

[**VDS\_CREATE\_VDISK\_PARAMETERS**](/windows/desktop/api/Vds/ns-vds-_vds_create_vdisk_parameters)  
[**VDS\_DISK\_FREE\_EXTENT**](/windows/desktop/api/Vds/ns-vds-_vds_disk_free_extent)  
[**VDS\_DISK\_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_disk_prop2)  
[**VDS\_DRIVE\_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_drive_prop2)  
[**VDS\_HINTS2**](/windows/desktop/api/Vds/ns-vds-_vds_hints2)  
[**VDS\_POOL\_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-_vds_pool_attributes)  
[**VDS\_POOL\_CUSTOM\_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-_vds_pool_custom_attributes)  
[**VDS\_STORAGE\_POOL\_DRIVE\_EXTENT**](/windows/desktop/api/Vds/ns-vds-_vds_storage_pool_drive_extent)  
[**VDS\_STORAGE\_POOL\_PROP**](/windows/desktop/api/Vds/ns-vds-_vds_storage_pool_prop)  
[**VDS\_SUB\_SYSTEM\_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_sub_system_prop2)  
[**VDS\_VDISK\_PROPERTIES**](/windows/desktop/api/Vds/ns-vds-_vds_vdisk_properties)  
[**VDS\_VOLUME\_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_volume_prop)  
</dl>

## Modifications to Existing VDS Enumerations

[**VDS\_ASYNC\_OUTPUT\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_async_output_type) enumeration added values:

<dl> **VDS\_ASYNCOUT\_CREATE\_VDISK**  
**VDS\_ASYNCOUT\_ATTACH\_VDISK**  
**VDS\_ASYNCOUT\_COMPACT\_VDISK**  
**VDS\_ASYNCOUT\_MERGE\_VDISK**  
**VDS\_ASYNCOUT\_EXPAND\_VDISK**  
</dl>

[**VDS\_CONTROLLER\_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_controller_status) enumeration added value:

<dl> **VDS\_CS\_REMOVED**  
</dl>

[**VDS\_DISK\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_disk_flag) enumeration added value:

<dl> **VDS\_DF\_BOOT\_FROM\_DISK**  
**VDS\_DF\_CURRENT\_READ\_ONLY**  
</dl>

[**VDS\_DRIVE\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_drive_flag) enumeration added values:

<dl> **VDS\_DRF\_ASSIGNED**  
**VDS\_DRF\_UNASSIGNED**  
**VDS\_DRF\_HOTSPARE\_IN\_USE**  
**VDS\_DRF\_HOTSPARE\_STANDBY**  
</dl>

[**VDS\_DRIVE\_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_drive_status) enumeration added value:

<dl> **VDS\_DRS\_REMOVED**  
</dl>

[**VDS\_FILE\_SYSTEM\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_file_system_type) enumeration added value:

<dl> **VDS\_FST\_EXFAT**  
</dl>

[**VDS\_HEALTH**](/windows/desktop/api/Vds/ne-vds-_vds_health) enumeration added values:

<dl> **VDS\_H\_REPLACED**  
**VDS\_H\_PENDING\_FAILURE**  
**VDS\_H\_DEGRADED**  
</dl>

[**VDS\_HWPROVIDER\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_hwprovider_type) enumeration added values:

<dl> **VDS\_HWT\_SAS**  
**VDS\_HWT\_HYBRID**  
</dl>

[**VDS\_LUN\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_lun_flag) enumeration added values:

<dl> **VDS\_LF\_READ\_CACHE\_ENABLED**  
**VDS\_LF\_WRITE\_CACHE\_ENABLED**  
**VDS\_LF\_MEDIA\_SCAN\_ENABLED**  
**VDS\_LF\_CONSISTENCY\_CHECK\_ENABLED**  
**VDS\_LF\_SNAPSHOT**  
</dl>

[**VDS\_LUN\_PLEX\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_lun_plex_type) enumeration added values:

<dl> **VDS\_LPT\_RAID2**  
**VDS\_LPT\_RAID3**  
**VDS\_LPT\_RAID4**  
**VDS\_LPT\_RAID5**  
**VDS\_LPT\_RAID6**  
**VDS\_LPT\_RAID03**  
**VDS\_LPT\_RAID05**  
**VDS\_LPT\_RAID10**  
**VDS\_LPT\_RAID15**  
**VDS\_LPT\_RAID30**  
**VDS\_LPT\_RAID50**  
**VDS\_LPT\_RAID53**  
**VDS\_LPT\_RAID60**  
</dl>

[**VDS\_LUN\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_lun_type) enumeration added values:

<dl> **VDS\_LT\_RAID2**  
**VDS\_LT\_RAID3**  
**VDS\_LT\_RAID4**  
**VDS\_LT\_RAID5**  
**VDS\_LT\_RAID6**  
**VDS\_LT\_RAID01**  
**VDS\_LT\_RAID03**  
**VDS\_LT\_RAID05**  
**VDS\_LT\_RAID10**  
**VDS\_LT\_RAID15**  
**VDS\_LT\_RAID30**  
**VDS\_LT\_RAID50**  
**VDS\_LT\_RAID51**  
**VDS\_LT\_RAID53**  
**VDS\_LT\_RAID60**  
**VDS\_LT\_RAID61**  
</dl>

[**VDS\_OBJECT\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_object_type) enumeration added values:

<dl> **VDS\_OT\_STORAGE\_POOL**  
**VDS\_OT\_VDISK**  
**VDS\_OT\_OPEN\_VDISK**  
</dl>

[**VDS\_PORT\_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_port_status) enumeration added value:

<dl> **VDS\_DRS\_REMOVED**  
</dl>

[**VDS\_PROVIDER\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_provider_flag) enumeration added values:

<dl> **VDS\_PF\_SUPPORT\_MIRROR**  
**VDS\_PF\_SUPPORT\_RAID5**  
</dl>

[**VDS\_PROVIDER\_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_provider_type) enumeration added values:

<dl> **VDS\_PT\_VIRTUALDISK**  
**VDS\_PT\_MAX**  
</dl>

[**VDS\_SERVICE\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_service_flag) enumeration added values:

<dl> **VDS\_SVF\_SUPPORT\_MIRROR**  
**VDS\_SVF\_SUPPORT\_RAID5**  
</dl>

[**VDS\_SUB\_SYSTEM\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_sub_system_flag) enumeration added values:

<dl> **VDS\_SF\_SUPPORTS\_LUN\_NUMBER**  
**VDS\_SF\_SUPPORTS\_MIRRORED\_CACHE**  
**VDS\_SF\_READ\_CACHING\_CAPABLE**  
**VDS\_SF\_WRITE\_CACHING\_CAPABLE**  
**VDS\_SF\_MEDIA\_SCAN\_CAPABLE**  
**VDS\_SF\_CONSISTENCY\_CHECK\_CAPABLE**  
</dl>

[**VDS\_TRANSITION\_STATE**](/windows/desktop/api/Vds/ne-vds-_vds_transition_state) enumeration added value:

<dl> **VDS\_TS\_RESTRIPING**  
</dl>

[**VDS\_VERSION\_SUPPORT\_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_version_support_flag) enumeration added values:

<dl> **VDS\_VSF\_2\_0**  
**VDS\_VSF\_2\_1**  
**VDS\_VSF\_3\_0**  
</dl>

[**VDS\_VOLUME\_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_volume_status) enumeration added value:

<dl> **VDS\_VS\_OFFLINE**  
</dl>

## Modifications to Existing VDS Structures

[**VDS\_CONTROLLER\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-_vds_controller_notification) structure added **ulEvent** values:

<dl> VDS\_NF\_CONTROLLER\_MODIFY  
VDS\_NF\_CONTROLLER\_REMOVED  
</dl>

[**VDS\_DRIVE\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-_vds_drive_notification) structure added **ulEvent** value:

<dl> VDS\_NF\_DRIVE\_REMOVED  
</dl>

[**VDS\_PORT\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-_vds_port_notification) structure added **ulEvent** values:

<dl> VDS\_NF\_PORT\_MODIFY  
VDS\_NF\_PORT\_REMOVED  
</dl>

 

 



