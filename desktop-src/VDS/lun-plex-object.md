---
description: LUN Plex Object
ms.assetid: db6eabaa-1b84-4613-ab2a-8d5904305e08
title: LUN Plex Object
ms.topic: article
ms.date: 05/31/2018
---

# LUN Plex Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

A LUN plex object models a LUN plex that is contained by a LUN. Only a mirrored LUN can have multiple plexes; all other LUN types have one plex. Each plex contains a copy of the data on the LUN. New plexes can be added to a LUN, and, with the exception of the original plex, existing plexes can be removed. VDS supports four LUN plex types: simple, spanned, striped, and striped with parity. For a description of each of these LUN types, see the [LUN Object](lun-object.md).

Use the [**IVdsLun::AddPlex**](/windows/desktop/api/Vds/nf-vds-ivdslun-addplex) method to add a plex to a LUN and the [**IVdsLun::RemovePlex**](/windows/desktop/api/Vds/nf-vds-ivdslun-removeplex) method to delete the plex. You can query for LUN plexes by invoking the [**IVdsLun::QueryPlexes**](/windows/desktop/api/Vds/nf-vds-ivdslun-queryplexes) method. You can get a pointer to a specific LUN plex by selecting the desired plex object from the enumeration that is returned by the **QueryPlexes** method. With a plex object, you can query for the drive extents and automagic hints, and apply new hints.

In addition to an object identifier, a name, and a serial number, LUN plex object properties include the plex type, size, status, health, transition state, and flags; an unmasking list and stripe size; and a rebuild priority setting.

The following table lists related interfaces, enumerations, and structures.



| Type                                              | Element                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsLunPlex**](/windows/desktop/api/Vds/nn-vds-ivdslunplex).                                                                                                                              |
| Associated enumerations                           | [**VDS\_LUN\_PLEX\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_lun_plex_flag), [**VDS\_LUN\_PLEX\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_lun_plex_status), and [**VDS\_LUN\_PLEX\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_lun_plex_type). |
| Associated structures                             | [**VDS\_LUN\_PLEX\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_lun_plex_prop).                                                                                                               |



 

## Related topics

<dl> <dt>

[Hardware Provider Objects](hardware-provider-objects.md)
</dt> <dt>

[LUN Object](lun-object.md)
</dt> </dl>

 

 
