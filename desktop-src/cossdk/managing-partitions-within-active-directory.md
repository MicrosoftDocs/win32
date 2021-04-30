---
description: As an alternative to managing Active Directory partitions through the Active Directory Users and Computers administrative tool, you can manage COM+ partitions programmatically through the use of a set of COM+ objects within Active Directory System Interface (ADSI).
ms.assetid: 915b4643-cbda-433a-a383-65a6b0fd0874
title: Managing Partitions Within Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Managing Partitions Within Active Directory

As an alternative to managing Active Directory partitions through the Active Directory Users and Computers administrative tool, you can manage COM+ partitions programmatically through the use of a set of COM+ objects within Active Directory System Interface (ADSI).

Regardless of the administrative technique you choose for managing COM+ partitions, there is a general sequence of steps that administrators must follow:

1.  Create the new COM+ partitions within Active Directory for your domain.
2.  Create COM+ partition sets within Active Directory, and map them to your newly created COM+ partitions.
3.  Configure your Active Directory partitions on your local machine, using the appropriate COM+ object. When you configure an Active Directory partition on a local machine, a **COM+ Applications** folder is automatically created in that partition folder.
4.  Install your COM+ applications in the appropriate COM+ partitions.

All of the preceding steps can be done programmatically, using a set of Active Directory interfaces called ADSI. The objects available for managing partitions that are available within ADSI are as follows:

-   DS\_USERPARTITIONSETLINK\_NAME
-   DS\_PARTITIONLINK\_NAME
-   DS\_OBJECTID\_NAME
-   DS\_DEFAULTPARTITIONLINK\_NAME
-   DS\_USERLINK\_NAME
-   DS\_PARTITIONSET\_NAME
-   DS\_PARTITION\_NAME

For information on creating and managing COM+ partitions through the use of the Active Directory Users and Computers and Component Services administrative tools, see the online help available from within each tool.

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

[Setting Administrative Rights for a Partition](setting-administrative-rights-for-a-partition.md)
</dt> </dl>

 

 



