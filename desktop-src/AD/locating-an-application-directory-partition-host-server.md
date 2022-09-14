---
title: Locating an Application Directory Partition Host Server
description: This topic describes how to locate an application directory partition host server.
ms.assetid: 636e8bc2-136c-42be-aa64-1b059dedf775
ms.tgt_platform: multiple
keywords:
- Locating an Application Directory Partition Host Server AD
- Application Directory Partitions AD , Locating a Host Server
ms.topic: article
ms.date: 05/31/2018
---

# Locating an Application Directory Partition Host Server

The NetLogon service registers the following list of SRV records for an application directory partition:

-   \_ldap.\_tcp.\<partition name\>
-   \_ldap.\_tcp.\<site name\>.\_sites.\<partition name\>

To locate a domain controller that hosts a replica of a specified application directory partition, call the [**DsGetDcName**](/windows/desktop/api/DsGetDC/nf-dsgetdc-dsgetdcnamea) function with the *DomainName* parameter set to the DNS name of the application directory partition and the **DS\_ONLY\_LDAP\_NEEDED** flag set in the *Flags* parameter. For more information and a code example that shows, using the **DsGetDcName** function, how to locate a domain controller that hosts a replica of an application directory partition, see [Example Code for Locating an Application Directory Partition Host Server](example-code-for-locating-an-application-directory-partition-host-server.md).

 

 




