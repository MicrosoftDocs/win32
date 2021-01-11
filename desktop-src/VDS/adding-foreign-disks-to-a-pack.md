---
description: Adding Foreign Disks to a Pack
ms.assetid: 4018c742-1d23-47b9-a787-69bf8847b54a
title: Adding Foreign Disks to a Pack
ms.topic: article
ms.date: 05/31/2018
---

# Adding Foreign Disks to a Pack

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

Most commonly, a foreign disk is a dynamic disk that is allocated on one computer and physically moved to another computer. However, any disk that belongs to a pack other than the online pack is considered to be a foreign disk that belongs to a foreign disk pack.

A foreign pack has the **VDS\_PKF\_FOREIGN** flag set in the **ulFlags** member of the [**VDS\_PACK\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_pack_prop) structure. Foreign packs are always offline.

The following procedure describes how to import one or more foreign disks.

**To import one or more foreign disks**

1.  Move disks to the new computer.
2.  On the new computer, use the [**IVdsService::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdsservice-reenumerate) method to install the foreign disks.
3.  Select the online pack to be the target pack that receives the foreign disks. If no online pack exists, use the [**IVdsSwProvider::CreatePack**](/windows/desktop/api/Vds/nf-vds-ivdsswprovider-createpack) method to create a new empty pack.
4.  Use the [**IVdsPack::MigrateDisks**](/windows/desktop/api/Vds/nf-vds-ivdspack-migratedisks) method to import the disks to the new dynamic pack.
5.  Use the [**IVdsSwProvider::QueryPacks**](/windows/desktop/api/Vds/nf-vds-ivdsswprovider-querypacks) method to enumerate the packs and [**IVdsPack::GetProperties**](/windows/desktop/api/Vds/nf-vds-ivdspack-getproperties) to determine which pack is now the online pack.

If you create a new empty target pack, the foreign disks are not actually migrated to that pack. Instead, the foreign pack is marked online, the **VDS\_PKF\_FOREIGN** flag for the pack is cleared (so the pack is no longer foreign), and the target pack that you created is discarded.

> [!Note]  
> Use the [**IVdsPack::AddDisk**](/windows/desktop/api/Vds/nf-vds-ivdspack-adddisk) method to add unallocated disks—disks not claimed by a provider—to a pack. An unallocated disk cannot be foreign.

 

## Related topics

<dl> <dt>

[Using VDS](using-vds.md)
</dt> <dt>

[**IVdsService::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdsservice-reenumerate)
</dt> <dt>

[**IVdsSwProvider::CreatePack**](/windows/desktop/api/Vds/nf-vds-ivdsswprovider-createpack)
</dt> <dt>

[**IVdsPack::MigrateDisks**](/windows/desktop/api/Vds/nf-vds-ivdspack-migratedisks)
</dt> <dt>

[**IVdsPack::AddDisk**](/windows/desktop/api/Vds/nf-vds-ivdspack-adddisk)
</dt> </dl>

 

 
