---
description: Setting Administrative Rights for a Partition
ms.assetid: d38e4a63-9ff9-4acb-bb7e-d6c96644bd32
title: Setting Administrative Rights for a Partition
ms.topic: article
ms.date: 05/31/2018
---

# Setting Administrative Rights for a Partition

Users assigned the Administrator role of the COM+ System Application are allowed to create, modify, and delete COM+ partitions. Within the Component Services administrative tool, administrative roles can be assigned to users by expanding the **Roles** folder of the COM+ System Application.

As of Windows Server 2003, the authentication capability for the COM+ System Application includes the value EOAC\_DISABLE\_AAA. This value, which disables activate-as-activator (AAA) activations, is used in the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) call when launching the System Application. Setting the authentication capability to EOAC\_DISABLE\_AAA allows an application that runs under a privileged account (such as LocalSystem) to help prevent its identity from being used to launch untrusted components.

## Related topics

<dl> <dt>

[Collecting Partition Metrics](collecting-partition-metrics.md)
</dt> <dt>

[Configuring the Partition Cache](configuring-the-partition-cache.md)
</dt> <dt>

[Grouping Applications into Partitions](grouping-applications-into-partitions.md)
</dt> <dt>

[Managing Local Partitions](managing-local-partitions.md)
</dt> <dt>

[Managing Partitions Within Active Directory](managing-partitions-within-active-directory.md)
</dt> </dl>

 

 
