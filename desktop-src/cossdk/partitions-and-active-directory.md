---
description: In addition to partitions, which contain one or more applications, COM+ also includes partition sets, which contain one or more partitions.
ms.assetid: 0b1a6daa-55e1-4a74-be01-e39473e3c0cc
title: Partitions and Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Partitions and Active Directory

In addition to partitions, which contain one or more applications, COM+ also includes *partition sets*, which contain one or more partitions. Created in Active Directory, partition sets allow users in a domain to access COM+ applications throughout the domain. During creation, each specific user or organizational unit (OU) is assigned, or mapped, to a partition set.

A single user or OU can access multiple partitions and their applications because there is a one-to-one correlation between a user identity or OU and a partition set. Without a partition set, a user or OU would need multiple user identities to access applications in different partitions.

To make COM+ applications available to domain users, an administrator must perform tasks both on the domain controller where Active Directory resides and on the server where the COM+ application is installed.

## On the Domain Controller

The administrator first creates a partition within Active Directory. Creating a COM+ partition is done either through the use of the Active Directory Users and Computers administrative tool or programmatically by using the Active Directory Services Interface (ADSI).

After the partition has been created within Active Directory, the administrator then creates a partition set. In creating a partition set, the administrator defines the partitions that are included in that set. Creating a COM+ partition set is done either through the use of the Active Directory Users and Computers administrative tool or programmatically by using the Active Directory Services Interface (ADSI).

Finally, the administrator maps domain users or organizational units (OUs) to the newly created partition set. This is done by displaying a user's **Properties** page, accessing the **COM+ Partition Sets** tab, and selecting a partition set from the list box.

## On the COM+ Application Server

The administrator creates a new partition, specifying the same partition name and partition ID (GUID) as that of the partition that was created within Active Directory on the domain controller. This is done using the **COM+ Partitions** folder within the Component Services administrative tool. To simplify this task, the Component Services tool allows the administrator to browse Active Directory to select the desired partition and its GUID.

When the domain partition has been created on the application server, a user's default partition becomes the default partition of the partition set in the Active Directory. Finally, the administrator can install the COM+ application into the newly created partition on the application server.

For more information about administering partitions for access by domain users, see the help associated with the Active Directory Users and Computers administrative tool.

## Mapping User Identities and OUs to Partition Sets

Users and OUs can be mapped to a partition sets. By mapping OUs to partition sets, an administrator can associate multiple users with a partition set at one time instead of having to map multiple user identities. A single user identity or OU can be mapped to one partition set only. In general, mapping user identities or OUs to partition sets does the following:

-   Ensures that applications are available to the appropriate users in the domain
-   Helps COM+ in determining the partition in which an application is located
-   Establishes a user's right to access a particular application

To associate partitions with partition sets within Active Directory and to map users and OUs to those partition sets, administrators use the Active Directory Users and Computers and Component Services administrative tools. When a partition is created within Active Directory, an administrator needs to locally configure that partition on the computer where the relevant COM+ application is to be installed. This local configuration of partitions created within Active Directory is done through the Component Services administrative tool.

If a domain user identity is not mapped to a partition set, the user is granted access by the user's OU, which is mapped to the partition. If the user's OU is not mapped to a partition set but the next highest OU in the hierarchy is mapped to that partition set, the user can access the partition.

## Related topics

<dl> <dt>

[Default Partitions](default-partitions.md)
</dt> <dt>

[Local Partitions](local-partitions.md)
</dt> <dt>

[Partition Properties](partition-properties.md)
</dt> <dt>

[The Global Partition](the-global-partition.md)
</dt> </dl>

 

 



