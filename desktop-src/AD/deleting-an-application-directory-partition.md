---
title: Deleting an Application Directory Partition
description: An application directory partition is deleted by deleting the crossRef object that represents the application directory partition.
ms.assetid: bc7986c1-5a11-440c-924e-dc525b5cb78f
ms.tgt_platform: multiple
keywords:
- Deleting an Application Directory Partition AD
- Application Directory Partitions AD , Deleting
ms.topic: article
ms.date: 05/31/2018
---

# Deleting an Application Directory Partition

An application directory partition is deleted by deleting the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that represents the application directory partition. When the deletion of the **crossRef** object replicates to a domain controller that has a replica of the application directory partition, the KCC will delete the local replica of the application directory partition. This eventually causes all replicas of the application directory partition to be deleted.

When the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object is deleted, the Active Directory server will delete the [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object that was created when the application directory partition was created, as well as deleting all objects in the application directory partition. None of the objects in the application directory partition are tombstoned when they deleted.

When an application directory partition is deleted, it is very difficult to restore it. To restore an application directory partition, it is necessary to restore a backup that has a replica of the application directory partition, find the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that represents the application directory partition and authoritatively restore the **crossRef** object.

**To delete an application directory partition and its replicas, perform the following steps**

1.  Search the Partitions container for a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that has an [**nCName**](/windows/desktop/ADSchema/a-ncname) attribute value that is equal to the distinguished name of the application directory partition.
2.  Delete the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object.

For more information, see [Example Code for Deleting an Application Directory Partition](example-code-for-deleting-an-application-directory-partition.md).

 

 