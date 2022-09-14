---
title: Virtual Disk Service is transitioning to Windows Storage Management API
description: Virtual Disk Service is transitioning to Windows Storage Management API
ms.assetid: AB2A7D08-03B2-4595-A8EC-805D111A0E89
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Disk Service is transitioning to Windows Storage Management API

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

Beginning with Windows 8 and Windows Server 2012, the Virtual Disk Service COM interface is superseded by the Storage Management API, a WMI-based programming interface. For managing storage subsystems, (Windows) disks, partitions, and volumes, we strongly recommend using the Storage Management API. For more info, see [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).

For all usages except mirror boot volumes (using a mirror volume to host the operating system), dynamic disks are deprecated. For data that requires resiliency against drive failure, use Storage Spaces, a resilient storage virtualization solution. For more info, see [Storage Spaces Technical Preview](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831739(v=ws.11)).

You can continue to use DiskPart, DiskRAID, and Disk Management during the deprecation period, but these tools will not work with Storage Spaces or with any other new Windows Management Instrumentation (WMI)-based Windows Storage Management APIs or in-box storage management utilities or clients.


| APIs | Storage Subsystems | Basic Disks | Dynamic Disks | Storage Spaces |
| --- | --- | --- | --- | --- |
| VDS | Yes | Yes | Yes | No |
| WMI | Yes | Yes | No | Yes |
| DiskPart | n/a | Yes | Yes | No |
| DiskRAID |  Yes | n/a | n/a | n/a |
| Disk Mgmt GUI | n/a | Yes | Yes | No |
| PowerShell | Yes | Yes | No | Yes |
| Storage Spaces Control Panel | n/a | No | No | Yes |


The result of this transition will be increased storage resiliency, availability, and scalability; a unified scripting and programming language, reduced storage management costs, and easier remote storage management.

## Manifestation

The DiskPart and DiskRAID utilities used in the VDS environment do not support the new Storage Spaces. Similarly, the new Storage PowerShell utility does not support the deprecated Dynamic Disks

## Mitigation

Microsoft strongly recommends that you base any new storage management apps on the Windows Storage Management API, and that you plan to transition existing apps that are based on the VDS infrastructure to the Windows Storage Management API during your standard updating cycles.

## Resources

-   [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal)
-   [Storage Cmdlets in Windows PowerShell](/powershell/module/storage/)
-   [Windows Management Instrumentation](../wmisdk/wmi-start-page.md)
-   [Windows PowerShell](https://msdn.microsoft.com/library/dd835506(v=VS.85).aspx)

 

 