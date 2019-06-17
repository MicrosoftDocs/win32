---
Description: Windows Server 2008 R2.
ms.assetid: 4ab37529-8d56-47a3-ad3d-0197cabd4f87
title: "What's New in VDS in Windows Server 2008 R2 and Windows 7"
ms.topic: article
ms.date: 05/31/2018
---

# What's New in VDS in Windows Server 2008 R2 and Windows 7

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](https://docs.microsoft.com/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

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
</dl>

## New VDS Enumerations

<dl>

[**VDS_DISK_OFFLINE_REASON**](/windows/desktop/api/Vds/ne-vds-_vds_disk_offline_reason)  
[**VDS_FORMAT_OPTION_FLAGS**](/windows/desktop/api/Vds/ne-vds-_vds_format_option_flags)  
[**VDS_INTERCONNECT_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_interconnect_flag)  
[**VDS_RAID_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_raid_type)  
[**VDS_STORAGE_POOL_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_storage_pool_status)  
[**VDS_STORAGE_POOL_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_storage_pool_type)  
[**VDS_SUB_SYSTEM_SUPPORTED_RAID_TYPE_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_sub_system_supported_raid_type_flag)  
[**VDS_VDISK_STATE**](/windows/desktop/api/Vds/ne-vds-_vds_vdisk_state)  
</dl>

## New VDS Structures

<dl>

[**VDS_CREATE_VDISK_PARAMETERS**](/windows/desktop/api/Vds/ns-vds-_vds_create_vdisk_parameters)  
[**VDS_DISK_FREE_EXTENT**](/windows/desktop/api/Vds/ns-vds-_vds_disk_free_extent)  
[**VDS_DISK_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_disk_prop2)  
[**VDS_DRIVE_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_drive_prop2)  
[**VDS_HINTS2**](/windows/desktop/api/Vds/ns-vds-_vds_hints2)  
[**VDS_POOL_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-_vds_pool_attributes)  
[**VDS_POOL_CUSTOM_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-_vds_pool_custom_attributes)  
[**VDS_STORAGE_POOL_DRIVE_EXTENT**](/windows/desktop/api/Vds/ns-vds-_vds_storage_pool_drive_extent)  
[**VDS_STORAGE_POOL_PROP**](/windows/desktop/api/Vds/ns-vds-_vds_storage_pool_prop)  
[**VDS_SUB_SYSTEM_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_sub_system_prop2)  
[**VDS_VDISK_PROPERTIES**](/windows/desktop/api/Vds/ns-vds-_vds_vdisk_properties)  
[**VDS_VOLUME_PROP2**](/windows/desktop/api/Vds/ns-vds-_vds_volume_prop)  
</dl>

## Modifications to Existing VDS Enumerations

[**VDS_ASYNC_OUTPUT_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_async_output_type) enumeration added values:

<dl> **VDS_ASYNCOUT_CREATE_VDISK**  
**VDS_ASYNCOUT_ATTACH_VDISK**  
**VDS_ASYNCOUT_COMPACT_VDISK**  
**VDS_ASYNCOUT_MERGE_VDISK**  
**VDS_ASYNCOUT_EXPAND_VDISK**  
</dl>

[**VDS_CONTROLLER_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_controller_status) enumeration added value:

<dl> **VDS_CS_REMOVED**  
</dl>

[**VDS_DISK_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_disk_flag) enumeration added value:

<dl> **VDS_DF_BOOT_FROM_DISK**  
**VDS_DF_CURRENT_READ_ONLY**  
</dl>

[**VDS_DRIVE_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_drive_flag) enumeration added values:

<dl> **VDS_DRF_ASSIGNED**  
**VDS_DRF_UNASSIGNED**  
**VDS_DRF_HOTSPARE_IN_USE**  
**VDS_DRF_HOTSPARE_STANDBY**  
</dl>

[**VDS_DRIVE_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_drive_status) enumeration added value:

<dl> **VDS_DRS_REMOVED**  
</dl>

[**VDS_FILE_SYSTEM_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_file_system_type) enumeration added value:

<dl> **VDS_FST_EXFAT**  
</dl>

[**VDS_HEALTH**](/windows/desktop/api/Vds/ne-vds-_vds_health) enumeration added values:

<dl> **VDS_H_REPLACED**  
**VDS_H_PENDING_FAILURE**  
**VDS_H_DEGRADED**  
</dl>

[**VDS_HWPROVIDER_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_hwprovider_type) enumeration added values:

<dl> **VDS_HWT_SAS**  
**VDS_HWT_HYBRID**  
</dl>

[**VDS_LUN_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_lun_flag) enumeration added values:

<dl> **VDS_LF_READ_CACHE_ENABLED**  
**VDS_LF_WRITE_CACHE_ENABLED**  
**VDS_LF_MEDIA_SCAN_ENABLED**  
**VDS_LF_CONSISTENCY_CHECK_ENABLED**  
**VDS_LF_SNAPSHOT**  
</dl>

[**VDS_LUN_PLEX_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_lun_plex_type) enumeration added values:

<dl> **VDS_LPT_RAID2**  
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
</dl>

[**VDS_LUN_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_lun_type) enumeration added values:

<dl> **VDS_LT_RAID2**  
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
</dl>

[**VDS_OBJECT_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_object_type) enumeration added values:

<dl> **VDS_OT_STORAGE_POOL**  
**VDS_OT_VDISK**  
**VDS_OT_OPEN_VDISK**  
</dl>

[**VDS_PORT_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_port_status) enumeration added value:

<dl> **VDS_DRS_REMOVED**  
</dl>

[**VDS_PROVIDER_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_provider_flag) enumeration added values:

<dl> **VDS_PF_SUPPORT_MIRROR**  
**VDS_PF_SUPPORT_RAID5**  
</dl>

[**VDS_PROVIDER_TYPE**](/windows/desktop/api/Vds/ne-vds-_vds_provider_type) enumeration added values:

<dl> **VDS_PT_VIRTUALDISK**  
**VDS_PT_MAX**  
</dl>

[**VDS_SERVICE_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_service_flag) enumeration added values:

<dl> **VDS_SVF_SUPPORT_MIRROR**  
**VDS_SVF_SUPPORT_RAID5**  
</dl>

[**VDS_SUB_SYSTEM_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_sub_system_flag) enumeration added values:

<dl> **VDS_SF_SUPPORTS_LUN_NUMBER**  
**VDS_SF_SUPPORTS_MIRRORED_CACHE**  
**VDS_SF_READ_CACHING_CAPABLE**  
**VDS_SF_WRITE_CACHING_CAPABLE**  
**VDS_SF_MEDIA_SCAN_CAPABLE**  
**VDS_SF_CONSISTENCY_CHECK_CAPABLE**  
</dl>

[**VDS_TRANSITION_STATE**](/windows/desktop/api/Vds/ne-vds-_vds_transition_state) enumeration added value:

<dl> **VDS_TS_RESTRIPING**  
</dl>

[**VDS_VERSION_SUPPORT_FLAG**](/windows/desktop/api/Vds/ne-vds-_vds_version_support_flag) enumeration added values:

<dl> **VDS_VSF_2_0**  
**VDS_VSF_2_1**  
**VDS_VSF_3_0**  
</dl>

[**VDS_VOLUME_STATUS**](/windows/desktop/api/Vds/ne-vds-_vds_volume_status) enumeration added value:

<dl> **VDS_VS_OFFLINE**  
</dl>

## Modifications to Existing VDS Structures

[**VDS_CONTROLLER_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-_vds_controller_notification) structure added **ulEvent** values:

<dl> VDS_NF_CONTROLLER_MODIFY  
VDS_NF_CONTROLLER_REMOVED  
</dl>

[**VDS_DRIVE_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-_vds_drive_notification) structure added **ulEvent** value:

<dl> VDS_NF_DRIVE_REMOVED  
</dl>

[**VDS_PORT_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-_vds_port_notification) structure added **ulEvent** values:

<dl> VDS_NF_PORT_MODIFY  
VDS_NF_PORT_REMOVED  
</dl>

 

 



