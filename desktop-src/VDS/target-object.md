---
description: Target Object
ms.assetid: e88d65ad-9b56-4620-a0f5-573c5e245b3e
title: Target Object
ms.topic: article
ms.date: 05/31/2018
---

# Target Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

A target object models an iSCSI target that is contained within an iSCSI subsystem.

Use the [**IVdsSubSystemIscsi::QueryTargets**](/windows/desktop/api/Vds/nf-vds-ivdssubsystemiscsi-querytargets) method to determine the iSCSI targets of the subsystem. Callers can get a pointer to a specific target by selecting the desired target object from the enumeration that is returned by the **QueryTargets** method. With a target object, you can set the target's friendly name and query for target properties, associated LUNs, and the subsystem that contains the target.

Host computers must log on to targets to access their associated LUNs. To perform a logon to a target, the target must have at least one associated portal in one of its portal groups. Input to and output from associated LUNs is handled through this logon session.

Target object properties include an object identifier, an iSCSI name, a friendly name, and a CHAP-enabled flag.

The following table lists related interfaces, enumerations, and structures.



| Type                                                                                      | Element                                                                                                                     |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object in VDS 1.1 and 2.0 iSCSI providers only | [**IVdsIscsiTarget**](/windows/desktop/api/Vds/nn-vds-ivdsiscsitarget).                                                                                 |
| Associated enumerations                                                                   | None.                                                                                                                       |
| Associated structures                                                                     | [**VDS\_ISCSI\_TARGET\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_iscsi_target_prop) and [**VDS\_TARGET\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_target_notification). |



 

## Related topics

<dl> <dt>

[Hardware Provider Objects](hardware-provider-objects.md)
</dt> <dt>

[**IVdsSubSystemIscsi::QueryTargets**](/windows/desktop/api/Vds/nf-vds-ivdssubsystemiscsi-querytargets)
</dt> </dl>

 

 
