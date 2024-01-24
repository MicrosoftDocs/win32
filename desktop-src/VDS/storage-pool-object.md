---
description: A storage pool object models a storage pool in a storage subsystem.
ms.assetid: a6104742-3ef9-4570-9728-3e6580953117
title: Storage Pool Object
ms.topic: article
ms.date: 05/31/2018
---

# Storage Pool Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/windows-hardware/drivers/storage/windows-storage-management-api-portal).\]

A storage pool object models a storage pool in a storage subsystem.

A storage pool contains drive extents from one or more drives that are managed by the same hardware provider.

The following table lists related interfaces, enumerations, and structures.



| Type                                              | Element                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsStoragePool**](/windows/desktop/api/Vds/nn-vds-ivdsstoragepool)                                                                                                                                                                                                                                                               |
| Associated enumerations                           | [**VDS\_RAID\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_raid_type), [**VDS\_STORAGE\_POOL\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_storage_pool_status), and [**VDS\_STORAGE\_POOL\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_storage_pool_type).                                                                                                                                  |
| Associated structures                             | [**VDS\_HINTS2**](/windows/desktop/api/Vds/ns-vds-vds_hints2), [**VDS\_POOL\_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-vds_pool_attributes), [**VDS\_POOL\_CUSTOM\_ATTRIBUTES**](/windows/desktop/api/Vds/ns-vds-vds_pool_custom_attributes), [**VDS\_STORAGE\_POOL\_DRIVE\_EXTENT**](/windows/desktop/api/Vds/ns-vds-vds_storage_pool_drive_extent), and [**VDS\_STORAGE\_POOL\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_storage_pool_prop). |



 

 

 
