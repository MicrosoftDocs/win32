---
description: Reenumerating and Refreshing
ms.assetid: 67d34946-47df-43e2-8ca7-628d0671b869
title: Reenumerating and Refreshing
ms.topic: article
ms.date: 05/31/2018
---

# Reenumerating and Refreshing

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

The reenumeration operation discovers newly connected and newly disconnected devices. The refresh operation updates the configuration information of existing devices.

**To reenumerate software provider objects**

-   Call the [**IVdsService::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdsservice-reenumerate) method. This method discovers all newly connected and disconnected disks and CD-ROM drives, and ensures that all disks have the proper owner. VDS owns raw disks or disks with failures; the basic provider owns basic disks; and the dynamic provider owns dynamic disks. This operation can involve scanning internal subsystem buses and waiting for time-outs.

**To reenumerate and refresh software provider objects**

-   Call the [**IVdsService::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdsservice-reenumerate) method and then call the [**IVdsService::Refresh**](/windows/desktop/api/Vds/nf-vds-ivdsservice-refresh) method. In addition to discovering newly connected and disconnected disks and CD-ROM drives, this combination of methods updates all disk, volume, and plex information in the VDS cache for disks that have not been recently connected or disconnected. Call **Refresh** alone to refresh the property information of existing objects in the cache. This operation can involve scanning internal subsystem buses and waiting for time-outs. Note that VDS updates the cache automatically whenever a change occurs that triggers a notification. Also, calling **Refresh** in response to a VDS notification could cause an endless loop of notifications to be sent. For these reasons, **Refresh** should be called only when it appears that the cache is not being updated properly.

**To reenumerate hardware subsystems**

-   Call the [**IVdsHwProvider::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdshwprovider-reenumerate) method. Depending on the provider, this operation can involve sending network packets and waiting for time-outs, rescanning SCSI buses and waiting for time-outs, and so on.

**To reenumerate hardware subsystem objects**

-   Call the [**IVdsSubSystem::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-reenumerate) method to inventory the objects (typically drives) in the subsystem. Depending on the subsystem, this operation can involve scanning internal subsystem buses and waiting for time-outs.

**To refresh hardware subsystems and subsystem objects**

-   Call the [**IVdsHwProvider::Refresh**](/windows/desktop/api/Vds/nf-vds-ivdshwprovider-refresh) method to refresh the VDS cache of information about existing subsystems that are managed by VDS hardware providers. Note that VDS updates the cache automatically whenever a change occurs that triggers a notification. Also, calling [**Refresh**](/windows/desktop/api/Vds/nf-vds-ivdsservice-refresh) in response to a VDS notification could cause an endless loop of notifications to be sent. For these reasons, **Refresh** should be called only when it appears that the cache is not being updated properly.

## Related topics

<dl> <dt>

[Using VDS](using-vds.md)
</dt> <dt>

[**IVdsService::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdsservice-reenumerate)
</dt> <dt>

[**IVdsService::Refresh**](/windows/desktop/api/Vds/nf-vds-ivdsservice-refresh)
</dt> <dt>

[**IVdsHwProvider::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdshwprovider-reenumerate)
</dt> <dt>

[**IVdsSubSystem::Reenumerate**](/windows/desktop/api/Vds/nf-vds-ivdssubsystem-reenumerate)
</dt> <dt>

[**IVdsHwProvider::Refresh**](/windows/desktop/api/Vds/nf-vds-ivdshwprovider-refresh)
</dt> </dl>

 

 
