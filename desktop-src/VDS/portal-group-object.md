---
description: Portal Group Object
ms.assetid: e5892e96-b6ad-447a-9627-b44fc6f1b27a
title: Portal Group Object
ms.topic: article
ms.date: 05/31/2018
---

# Portal Group Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

A portal group object models an iSCSI portal group that is contained within an iSCSI target.

Use the [**IVdsIscsiTarget::QueryPortalGroups**](/windows/desktop/api/Vds/nf-vds-ivdsiscsitarget-queryportalgroups) method to determine the portal groups that are contained by a specific target. Use the [**IVdsIscsiPortal::QueryAssociatedPortalGroups**](/windows/desktop/api/Vds/nf-vds-ivdsiscsiportal-queryassociatedportalgroups) method to determine the portal groups that are associated with a specified portal. Callers can get a pointer to a specific portal group by selecting the desired portal group object from the enumeration that is returned by the **QueryPortalGroups** method or the **QueryAssociatedPortalGroups** method. With a portal group object, you can add or remove portals and query for portal group properties, associated portals, and the target that contains the portal group.

Portal group object properties include an [object identifier](vds-data-types.md) and the portal group tag. For more information about portal group tags, see the iSCSI specification at <https://go.microsoft.com/fwlink/p/?linkid=158752>.

The following table lists related interfaces, enumerations, and structures.



| Type                                                                                      | Element                                                                                                                                            |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object in VDS 1.1 and 2.0 iSCSI providers only | [**IVdsIscsiPortalGroup**](/windows/desktop/api/Vds/nn-vds-ivdsiscsiportalgroup).                                                                                              |
| Associated enumerations                                                                   | None.                                                                                                                                              |
| Associated structures                                                                     | [**VDS\_ISCSI\_PORTALGROUP\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_iscsi_portalgroup_prop) and [**VDS\_PORTAL\_GROUP\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_portal_group_notification). |



 

## Related topics

<dl> <dt>

[Hardware Provider Objects](hardware-provider-objects.md)
</dt> <dt>

[**IVdsIscsiPortal::QueryAssociatedPortalGroups**](/windows/desktop/api/Vds/nf-vds-ivdsiscsiportal-queryassociatedportalgroups)
</dt> <dt>

[**IVdsIscsiTarget::QueryPortalGroups**](/windows/desktop/api/Vds/nf-vds-ivdsiscsitarget-queryportalgroups)
</dt> </dl>

 

 
