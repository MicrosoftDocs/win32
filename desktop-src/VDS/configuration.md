---
description: Configuration Overview
ms.assetid: 5cdc21a1-ff55-4c36-8106-b045256778ce
title: Configuration Overview
ms.topic: article
ms.date: 05/31/2018
---

# Configuration Overview

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

If you are unfamiliar with the objects that are defined by VDS, see the [VDS Object Model](vds-object-model.md).

The configuration complexity of a virtual disk can range from very simple to finely tuned. No-care, free-from-care, and enterprise virtual disks define three typical configuration perspectives. Each perspective presents somewhat different requirements:

-   No-care virtual disks are lightly configured, perhaps only to automate the partitioning and formatting of new disks, or to temporarily create a mirrored volume for migrating data from one disk to another without downtime. Such disks are good for notebook computers and other systems with one or a few disks.
-   Free-from-care virtual disks provide storage that appears self-configuring, self-healing, and available; uses striped volumes and LUNs to achieve better performance; uses mirrored volumes and LUNs to achieve better availability; and uses packs to make the failure modes clean and contained. This configuration level is ideal when replacing old, small, slow system disks with new, large, fast disks is routine. It is also ideal for mirroring data with automated hot sparing—a single spare spindle can protect many spindles. For details, see [Hot Sparing](hot-sparing.md).

    Small-scale SANs depend on the flexibility and automation that is offered by this configuration level, as do Network Attached Storage (NAS) appliances. Free-from-care virtual disks simplify the task of consolidating application storage—for example, the storage for SQL and Exchange—without consolidating the servers.

-   Enterprise virtual disks contain very large or complex enterprise configurations with additional site-specific or application-specific requirements. Administrators tune the storage subsystem for a single application that might run only infrequently, such as a monthly batch reporting job on an order-taking transaction system. Enterprise virtual disks must scale, show the real-time activity of the storage subsystem, and satisfy the requirements of hands-on administrators.

For additional information about mirrors, stripes, and the other configuration options in VDS, see [Volume and LUN Binding](volume-and-lun-binding.md). An advanced configuration technique, called stacking, enables you to combine the configurations that are associated with existing volumes and LUNs. For details, see [Configuration Stacking](configuration-stacking.md).

## Related topics

<dl> <dt>

[Virtual Disk Service](virtual-disk-service-portal.md)
</dt> <dt>

[VDS Object Model](vds-object-model.md)
</dt> <dt>

[Hot Sparing](hot-sparing.md)
</dt> <dt>

[Volume and LUN Binding](volume-and-lun-binding.md)
</dt> <dt>

[Configuration Stacking](configuration-stacking.md)
</dt> </dl>

 

 
