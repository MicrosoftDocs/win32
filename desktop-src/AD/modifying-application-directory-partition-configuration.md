---
title: Modifying Application Directory Partition Configuration
description: An application directory partition can be modified by changing certain attributes of the crossRef object that represents the application directory partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c4db5b3f-7d80-46a0-8a3a-9b1eb3c9f7b1
ms.tgt_platform: multiple
keywords:
- Modifying Application Directory Partition Configuration AD
- Application Directory Partitions AD , Modifying Configuration
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Modifying Application Directory Partition Configuration

An application directory partition can be modified by changing certain attributes of the [**crossRef**](https://msdn.microsoft.com/library/ms681007) object that represents the application directory partition. To locate the [**crossRef**](https://msdn.microsoft.com/library/ms681007) object that represents a particular application directory partition, search the Partitions container for a **crossRef** object that has an [**nCName**](https://msdn.microsoft.com/library/ms678699) attribute value that is equal to the distinguished name of the application directory partition. The distinguished name of the **crossRef** object can then be used to bind to the **crossRef** object.

The following table lists attributes of the [**crossRef**](https://msdn.microsoft.com/library/ms681007) object that can be modified.

| Attribute                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**msDS-Replication-Notify-First-DSA-Delay**](https://msdn.microsoft.com/library/ms677479)           | Specifies the delay, in seconds, after an originating object change before the first replication partner is notified. For more information, see [Application Directory Partition Replication](application-directory-partition-replication.md).                                                                                                   |
| [**msDS-Replication-Notify-Subsequent-DSA-Delay**](https://msdn.microsoft.com/library/ms677480) | Specifies the delay, in seconds, between subsequent notifications to the second, third, and so on replication partners. For more information, see [Application Directory Partition Replication](application-directory-partition-replication.md).                                                                                                 |
| [**msDS-SDReferenceDomain**](https://msdn.microsoft.com/library/ms677815)                                             | Identifies the domain that the security subsystem uses to interpret local domain references in the [**nTSecurityDescriptor**](https://msdn.microsoft.com/library/ms679006) attributes of objects in that application directory partition. For more information, see [Application Directory Partition Security](application-directory-partition-security.md). |
| [**msDS-NC-Replica-Locations**](https://msdn.microsoft.com/library/ms677446)                                       | Contains the distinguished name of the [**nTDSDSA**](https://msdn.microsoft.com/library/ms683855) object for each domain controller that hosts a replica of the application directory partition. For more information, see [Adding or Deleting an Application Directory Partition Replica](adding-or-deleting-an-application-directory-partition-replica.md).            |



 

 

 




