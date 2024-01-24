---
description: Encapsulate the hard disk into a single file for use by the operating system as a virtual disk. Virtual disks can function as boot disks and can host native file systems (NTFS, FAT, exFAT, and UDFS) while supporting standard disk and file operations.
MS-HAID: vhd.portal
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Virtual Disk
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vhd.portal"></span>Virtual Disk

## <span id="purpose"></span>Purpose

The Virtual Hard Disk (VHD) format is a publicly-available image format specification that specifies a virtual hard disk encapsulated in a single file, capable of hosting native file systems while supporting standard disk and file operations. An example of how VHD files are used is the [Hyper-V](https://www.microsoft.com/windowsserver2008/en/us/hyperv.aspx) feature in Windows Server 2008, Virtual Server, and Windows Virtual PC. These products use VHDs to contain the Windows operating system image utilized by a virtual machine as its system boot disk.

## <span id="developer_audience_heading"></span>Developer audience

The Microsoft Windows Software Development Kit (SDK) integrates Native VHD support for working with VHDs, making it easier for developers and administrators to create, manage, and deploy Windows images in VHDs using the platform API support or management tools. It is not necessary to install separate applications or implement a VHD format parser to enable these operations. These APIs allow for generic use of VHDs independent of any other virtualization technologies.

## <span id="run_time_requirements_heading"></span>Run-time requirements

VHD is supported on Windows 7 and Windows Server 2008 R2.

## <span id="in_this_section"></span>In this section


| Topic | Description | 
|-------|-------------|
| <p><a href="about-vhd.md">About VHD</a></p> | <p>Describes the VHD format with API usage tips and suggestions.</p> | 
| <p><a href="vhd-reference.md">VHD Reference</a></p> | <p>Describes the VHD API functions, structures, and enumerations.</p> | 


 

## <span id="related_topics"></span>Related topics

[Virtual Disk Service](/windows/desktop/VDS/virtual-disk-service-portal)

 

 
