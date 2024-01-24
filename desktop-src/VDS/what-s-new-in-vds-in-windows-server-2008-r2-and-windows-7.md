---
description: Learn about new changes for the Virtual Disk Service (VDS) in Windows Server 2008 R2 and Windows 7.
ms.assetid: 4ab37529-8d56-47a3-ad3d-0197cabd4f87
title: "What's New in VDS in Windows Server 2008 R2 and Windows 7"
ms.topic: article
ms.date: 05/31/2018
---

# What's New in VDS in Windows Server 2008 R2 and Windows 7

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/windows-hardware/drivers/storage/windows-storage-management-api-portal).\]

Windows Server 2008 R2 and Windows 7 introduce the following changes to the Virtual Disk Service (VDS):

- [New VDS Interfaces](#new-vds-interfaces)
- [New VDS Enumerations](#new-vds-enumerations)
- [New VDS Structures](#new-vds-structures)
- [Modifications to Existing VDS Enumerations](#modifications-to-existing-vds-enumerations)
- [Modifications to Existing VDS Structures](#modifications-to-existing-vds-structures)

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


## New VDS Enumerations

<dl>

[**VDS_DISK_OFFLINE_REASON**](/windows/desktop/api/Vds/ne-vds-vds_disk_offline_reason)  
[**VDS_FORMAT_OPTION_FLAGS**](/windows/desktop/api/Vds/ne-vds-vds_format_option_flags)  
[**VDS_INTERCONNECT_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_interconnect_flag)  
[**VDS_RAID_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_raid_type)  
[**VDS_STORAGE_POOL_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_storage_pool_status)  
[**VDS_STORAGE_POOL_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_storage_pool_type)  
[**VDS_SUB_SYSTEM_SUPPORTED_RAID_TYPE_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_sub_system_supported_raid_type_flag)  
[**VDS_VDISK_STATE**](/windows/desktop/api/Vds/ne-vds-vds_vdisk_state)  


## New VDS Structures

<dl>

[**VDS_CREATE_VDISK_PARAMETERS**](/windows/desktop/api/Vds/ns-vds-vds_create_vdisk_parameters)  
[**VDS_DISK_FREE_EXTENT**](/windows/desktop/api/Vds/ns-vds-vds_disk_free_extent)  
[**VDS_DISK_PROP2**](/windows/desktop/api/Vds/ns-vds-vds_disk_prop2)  
[**VDS_DRIVE_PROP2**](/windows/desktop/api/Vds/ns-vds-vds_drive_prop2)  
[**VDS_HINTS2**](/windows/desktop/api/Vds/ns-vds-vds_hints2)  
[**VDS_POOL_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-vds_pool_attributes)  
[**VDS_POOL_CUSTOM_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-vds_pool_custom_attributes)  
[**VDS_STORAGE_POOL_DRIVE_EXTENT**](/windows/desktop/api/Vds/ns-vds-vds_storage_pool_drive_extent)  
[**VDS_STORAGE_POOL_PROP**](/windows/desktop/api/Vds/ns-vds-vds_storage_pool_prop)  
[**VDS_SUB_SYSTEM_PROP2**](/windows/desktop/api/Vds/ns-vds-vds_sub_system_prop2)  
[**VDS_VDISK_PROPERTIES**](/windows/desktop/api/Vds/ns-vds-vds_vdisk_properties)  
[**VDS_VOLUME_PROP2**](/windows/desktop/api/Vds/ns-vds-vds_volume_prop)  


## Modifications to Existing VDS Enumerations

[**VDS_ASYNC_OUTPUT_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_async_output_type) enumeration added values:

 **VDS_ASYNCOUT_CREATE_VDISK**  
**VDS_ASYNCOUT_ATTACH_VDISK**  
**VDS_ASYNCOUT_COMPACT_VDISK**  
**VDS_ASYNCOUT_MERGE_VDISK**  
**VDS_ASYNCOUT_EXPAND_VDISK**  


[**VDS_CONTROLLER_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_controller_status) enumeration added value:

**VDS_CS_REMOVED**  


[**VDS_DISK_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_disk_flag) enumeration added value:

**VDS_DF_BOOT_FROM_DISK**  
**VDS_DF_CURRENT_READ_ONLY**  


[**VDS_DRIVE_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_drive_flag) enumeration added values:

**VDS_DRF_ASSIGNED**  
**VDS_DRF_UNASSIGNED**  
**VDS_DRF_HOTSPARE_IN_USE**  
**VDS_DRF_HOTSPARE_STANDBY**  


[**VDS_DRIVE_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_drive_status) enumeration added value:

**VDS_DRS_REMOVED**  


[**VDS_FILE_SYSTEM_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_file_system_type) enumeration added value:

**VDS_FST_EXFAT**  


[**VDS_HEALTH**](/windows/desktop/api/Vds/ne-vds-vds_health) enumeration added values:

**VDS_H_REPLACED**  
**VDS_H_PENDING_FAILURE**  
**VDS_H_DEGRADED**  


[**VDS_HWPROVIDER_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_hwprovider_type) enumeration added values:

**VDS_HWT_SAS**  
**VDS_HWT_HYBRID**  


[**VDS_LUN_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_lun_flag) enumeration added values:

**VDS_LF_READ_CACHE_ENABLED**  
**VDS_LF_WRITE_CACHE_ENABLED**  
**VDS_LF_MEDIA_SCAN_ENABLED**  
**VDS_LF_CONSISTENCY_CHECK_ENABLED**  
**VDS_LF_SNAPSHOT**  


[**VDS_LUN_PLEX_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_lun_plex_type) enumeration added values:

**VDS_LPT_RAID2**  
**VDS_LPT_RAID3**  
**VDS_LPT_RAID4**  
**VDS_LPT_RAID5**  
**VDS_LPT_RAID6**  
**VDS_LPT_RAID03**  
**VDS_LPT_RAID05**  
**VDS_LPT_RAID10**  
**VDS_LPT_RAID15**  
**VDS_LPT_RAID30**  
**VDS_LPT_RAID50**  
**VDS_LPT_RAID53**  
**VDS_LPT_RAID60**  


[**VDS_LUN_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_lun_type) enumeration added values:

**VDS_LT_RAID2**  
**VDS_LT_RAID3**  
**VDS_LT_RAID4**  
**VDS_LT_RAID5**  
**VDS_LT_RAID6**  
**VDS_LT_RAID01**  
**VDS_LT_RAID03**  
**VDS_LT_RAID05**  
**VDS_LT_RAID10**  
**VDS_LT_RAID15**  
**VDS_LT_RAID30**  
**VDS_LT_RAID50**  
**VDS_LT_RAID51**  
**VDS_LT_RAID53**  
**VDS_LT_RAID60**  
**VDS_LT_RAID61**  


[**VDS_OBJECT_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_object_type) enumeration added values:

**VDS_OT_STORAGE_POOL**  
**VDS_OT_VDISK**  
**VDS_OT_OPEN_VDISK**  


[**VDS_PORT_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_port_status) enumeration added value:

**VDS_DRS_REMOVED**  


[**VDS_PROVIDER_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_provider_flag) enumeration added values:

**VDS_PF_SUPPORT_MIRROR**  
**VDS_PF_SUPPORT_RAID5**  


[**VDS_PROVIDER_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_provider_type) enumeration added values:

**VDS_PT_VIRTUALDISK**  
**VDS_PT_MAX**  


[**VDS_SERVICE_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_service_flag) enumeration added values:

**VDS_SVF_SUPPORT_MIRROR**  
**VDS_SVF_SUPPORT_RAID5**  


[**VDS_SUB_SYSTEM_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_sub_system_flag) enumeration added values:

**VDS_SF_SUPPORTS_LUN_NUMBER**  
**VDS_SF_SUPPORTS_MIRRORED_CACHE**  
**VDS_SF_READ_CACHING_CAPABLE**  
**VDS_SF_WRITE_CACHING_CAPABLE**  
**VDS_SF_MEDIA_SCAN_CAPABLE**  
**VDS_SF_CONSISTENCY_CHECK_CAPABLE**  


[**VDS_TRANSITION_STATE**](/windows/desktop/api/Vds/ne-vds-vds_transition_state) enumeration added value:

**VDS_TS_RESTRIPING**  


[**VDS_VERSION_SUPPORT_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_version_support_flag) enumeration added values:

**VDS_VSF_2_0**  
**VDS_VSF_2_1**  
**VDS_VSF_3_0**  


[**VDS_VOLUME_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_volume_status) enumeration added value:

**VDS_VS_OFFLINE**  


## Modifications to Existing VDS Structures

[**VDS_CONTROLLER_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_controller_notification) structure added **ulEvent** values:

VDS_NF_CONTROLLER_MODIFY  
VDS_NF_CONTROLLER_REMOVED  


[**VDS_DRIVE_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_drive_notification) structure added **ulEvent** value:

VDS_NF_DRIVE_REMOVED  


[**VDS_PORT_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_port_notification) structure added **ulEvent** values:

VDS_NF_PORT_MODIFY  
VDS_NF_PORT_REMOVED  


 

 
