---
description: The Virtual Disk Service (VDS) manages a wide range of storage configurations, from single-disk desktops to external storage arrays. The service exposes an application programming interface (API).
ms.assetid: 536aafd2-cc04-48cc-8ee7-920efbba2a5f
title: Virtual Disk Service
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Disk Service

\[Beginning with Windows 8 and Windows Server 2012, the Virtual Disk Service COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

## Purpose

The Virtual Disk Service (VDS) manages a wide range of storage configurations, from single-disk desktops to external storage arrays. The service exposes an application programming interface (API).

## Where applicable

Beginning with Windows 8 and Windows Server 8, the Virtual Disk Service COM interface is superseded by the Storage Management API, a WMI-based programming interface. For managing storage subsystems, (Windows) disks, partitions, and volumes, we strongly recommend using the Storage Management API. For more information, see the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).

For all usages except mirror boot volumes (using a mirror volume to host the operating system ), dynamic disks are deprecated. For data that requires resiliency against drive failure, use Storage Spaces, a resilient storage virtualization solution. For more information, see [Storage Spaces Technical Preview](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831739(v=ws.11)).

Application developers who use the interfaces described in this guide can query and configure a heterogeneous set of vendor-supplied and internally managed storage. VDS hides from applications the complexities associated with storage, making the service both vendor and technology neutral.

## Developer audience

This documentation is intended for application developers who are familiar with the storage capabilities of Microsoft Windows platforms and who are knowledgeable about COM development.

The guide is also intended for hardware subsystem manufacturers who develop and support VDS hardware provider programs.

## Run-time requirements

VDS is supported on Windows Server 2003, Windows Vista, and later. For information about run-time requirements for a particular programming element, see the Requirements section of the documentation for that element.

Running 32-bit VDS applications under WOW64 is supported, but 64-bit VDS providers must run as native applications on 64-bit Windows versions.

VDS is available in the Microsoft Windows Software Development Kit (SDK). You can install the SDK for Windows 7 and Windows Server 2008 R2 from the [Windows Download Center](https://www.microsoft.com/download/details.aspx?id=8279). This version of the Windows SDK can be used to develop VDS applications for Windows Server 2003, Windows Vista, and later. You can also download the [ISO version](https://www.microsoft.com/download/details.aspx?id=8442) of the SDK from the Windows Download Center.

## In this section



| Topic                                         | Description                                                                                            |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [About VDS](about-vds.md)<br/>         | Describes the VDS object model, storage-configuration strategies, and VDS notifications.<br/>    |
| [Using VDS](using-vds.md)<br/>         | Describes how to use VDS to query and configure storage devices.<br/>                            |
| [VDS Reference](vds-reference.md)<br/> | Describes VDS constants, data types, enumerations, interfaces, structures, and error codes.<br/> |



 

 

