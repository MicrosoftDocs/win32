---
description: Portal Object
ms.assetid: 6655bbae-07d3-416b-9e45-ddcbe3433f40
title: Portal Object
ms.topic: article
ms.date: 05/31/2018
---

# Portal Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

A portal object models an iSCSI portal that is contained within an iSCSI subsystem.

Use the [**IVdsSubSystemIscsi::QueryPortals**](/windows/desktop/api/Vds/nf-vds-ivdssubsystemiscsi-queryportals) method to determine the iSCSI portals of the subsystem. Callers can get a pointer to a specific portal by selecting the desired portal object from the enumeration that is returned by the **QueryPortals** method. With a portal object, you can set the portal status and query for portal properties, associated portal groups, and the subsystem that contains the portal.

A portal object can only be associated with at most one portal group of a specified target.

Portals serve as one of the endpoints of MPIO paths in iSCSI hardware providers, upon which load balancing policies can be imposed.

Portal object properties include an object identifier, an IP address and port, and the portal status.

The following table lists related interfaces, enumerations, and structures.



| Type                                                                                      | Element                                                                                                                 |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object in VDS 1.1 and 2.0 iSCSI providers only | [**IVdsIscsiPortal**](/windows/desktop/api/Vds/nn-vds-ivdsiscsiportal).                                                                             |
| Associated enumerations                                                                   | [**VDS\_ISCSI\_PORTAL\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_iscsi_portal_status).                                                          |
| Associated structures                                                                     | [**VDS\_ISCSI\_PORTAL\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_iscsi_portal_prop) and [**VDS\_PORT\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_port_notification). |



 

## Related topics

<dl> <dt>

[Hardware Provider Objects](hardware-provider-objects.md)
</dt> <dt>

[**IVdsSubSystemIscsi::QueryPortals**](/windows/desktop/api/Vds/nf-vds-ivdssubsystemiscsi-queryportals)
</dt> </dl>

 

 
