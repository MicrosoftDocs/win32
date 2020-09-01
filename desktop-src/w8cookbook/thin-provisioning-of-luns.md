---
title: Thin provisioning of logical units
description: Thin provisioning of logical units
ms.assetid: D64ECA7B-62AC-4C14-BE4B-84DA2E20C16B
keywords:
- LUN
- LBA
ms.topic: article
ms.date: 05/31/2018
---

# Thin provisioning of logical units

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

Windows Thin Provisioning is an interface to the end-to-end storage provisioning solution. To deliver a highly available, scalable and user-friendly storage provisioning service requires robust implementations from the server host to the storage target device. The Windows thin provisioning feature provides a synchronous view of the thin provisioning storage devices to the system administrator, IT manager, and storage administrator through the thinly provisioned logical unit’s (LUN’s) identification, threshold notification, resource exhaustion handling, space reclamation, and logical block addressing (LBA) state retrieval. The Windows thin provisioning feature presents a robust storage provisioning service model that can be applied to client-server storage systems, virtualization storage, and cloud storage services. Microsoft will ensure the high quality of the thin provisioning feature by enforcing the Windows Thin Provisioning Hardware Certification Kit requirements for storage array products.

The Windows Thin Provisioning storage solution:

-   Allows storage administrators to create a larger LUN with fewer physical disk resources
-   Adds or removes physical disk resource without interrupting the storage provisioning service
-   Alerts users to the storage volume usage through the threshold setting
-   Supports storage provisioning through the shared storage pool configuration
-   Increases or decreases the size of the storage pool according to the demand and usage of storage space

Summary of the Windows Thin Provisioning features:

-   Thin Provisioning LUN identification
-   Handles for threshold notification, temporary resource exhaustion, and permanent resource exhaustion
-   Storage space reclamation
-   Mapping state queries of logical blocks

## Manifestation

Without the proper understanding of the Windows handles for thin provisioning LUN, the app could fail with unexpected behavior or for an unknown cause.

## Using thin provisioning LUNs

To use thinly provisioned LUNs in Windows 8 or Windows Server 2012, system and storage administrators should be aware of these matters:

-   Thin provisioning LUN identification; system administrators or end users can use Defrag and the Storage Optimizer utility to identify the media type of the storage device
-   When a threshold or a permanent resource exhaustion event is hit, Windows will log a system event to alert the system administrator
-   Storage space reclamation can be performed manually or automatically by file delete notification or the scheduler of the storage optimizer
-   Storage administrator should implement the threshold notification to alert system administrator or end user and avoid any unexpected storage service interruption

## Tests

-   Storage array must receive Windows 8 Thin Provisioning certificate to support Windows Thin Provisioning features
-   Windows Thin Provisioning Hardware Certification Kit for storage array will be a useful test tool to verify storage array’s capability for Windows Thin Provisioning feature support
-   Windows expects the Thin Provisioning LUN and Full Provisioning LUN to work in the same system without any issue

## Resources

-   [T10 SCSI Block Command Spec (SBC3r27)](https://www.t10.org/cgi-bin/ac.pl?t=f&f=sbc3r27.pdf)
-   [Hardware Dashboard Services](/windows-hardware/drivers/dashboard/)

 

 