---
title: Enumerating Replicas of an Application Directory Partition
description: This topic shows how to enumerate the replicas for an application directory partition.
ms.assetid: a1d6865b-ec77-4687-9da7-7fc717568bda
ms.tgt_platform: multiple
keywords:
- Enumerating Replicas of an Application Directory Partition AD
- Application Directory Partitions AD , Enumerating Replicas of
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Replicas of an Application Directory Partition

When a replica of an application directory partition is added, the distinguished name of the [**nTDSDSA**](/windows/desktop/ADSchema/c-ntdsdsa) object for the domain controller that will contain the replica is added to the [**msDS-NC-Replica-Locations**](/windows/desktop/ADSchema/a-msds-nc-replica-locations) attribute of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object. The **crossRef** object used represents the application directory partition.

**To enumerate the replicas for an application directory partition**

1.  Search the Partitions container for a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that has an [**nCName**](/windows/desktop/ADSchema/a-ncname) attribute value that is equal to the distinguished name of the application directory partition.
2.  Use each value of the [**msDS-NC-Replica-Locations**](/windows/desktop/ADSchema/a-msds-nc-replica-locations) attribute of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object to bind to the [**nTDSDSA**](/windows/desktop/ADSchema/c-ntdsdsa) object of the server.
3.  Obtain the ADsPath for the parent of each [**nTDSDSA**](/windows/desktop/ADSchema/c-ntdsdsa) object. This is an object that represents the domain controller server. Use the ADsPath to bind to the server object.
4.  Obtain the [**dNSHostName**](/windows/desktop/ADSchema/a-dnshostname) attribute value of the server object. This is a single-value property that contains the DNS name of the server.

Due to replication latency and scheduled KCC run delays, it is possible the actual active replicas for an application directory partition may not match the list of domain controllers indicated by the [**msDS-NC-Replica-Locations**](/windows/desktop/ADSchema/a-msds-nc-replica-locations) attribute of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object. A more accurate, but less efficient way to determine the actual active replicas of an application directory partition is to search for all [**nTDSDSA**](/windows/desktop/ADSchema/c-ntdsdsa) objects in the forest that have a [**msDS-hasMasterNCs**](/windows/desktop/ADSchema/a-msds-hasmasterncs) attribute that contains the distinguished name of the application directory partition. The **msDS-hasMasterNCs** attribute contains the distinguished names of all writable directory partitions that the domain controller hosts, including application directory partitions.

 

 