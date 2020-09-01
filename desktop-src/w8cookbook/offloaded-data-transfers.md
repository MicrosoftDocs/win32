---
title: Offloaded data transfers
description: Offloaded data transfers
ms.assetid: 91EBE6D6-2DA7-48DA-AEB7-3FAFCA8341F5
keywords:
- odx
- copy offload
- offload
ms.topic: article
ms.date: 05/31/2018
---

# Offloaded data transfers

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

To advance the storage data movement, Microsoft has developed a new data transfer technology – offloaded data transfer (ODX). Instead of using buffered read and buffered write operations, Windows ODX starts the copy operation with an offload read and retrieves a token representing the data from the storage device, then uses an offload write command with the token to request data movement from the source disk to the destination disk. The copy manager of the storage devices performs the data movement according to the token. In the Windows 8, the IT manager and storage administrator are able to use the Windows ODX feature to interact with the storage device to move large files or data through the high-speed storage network. Windows ODX will significantly reduce client-server network traffic and CPU time usage during large data transfers because all the data movement is at the backend storage network. ODX can be used in virtual machine deployment, massive data migration, and tiered storage device support, and can lower the cost of physical hardware deployment through the ODX and thin provisioning storage features.

> [!Note]  
> This feature will only work on storage devices with SPC4 and SBC3 specification implementation.

 

## Functional details

-   The Windows ODX feature is embedded in the copy engine of the Windows operating system; during storage enumeration, Windows will query the ODX capability of the storage device
-   Copy source storage device and copy destination storage device should be managed under the same copy manager for copy offload support
-   If a copy offload operation fails, the storage device’s copy manager must return the proper additional sense data for the apps’ error handling
-   The Windows copy engine will fall back to the traditional copy operation if the copy offload operation fails

## Using ODX

-   The data transfer app must ensure both copy source LUN and copy destination LUN are ODX capable before calling the ODX API routines
-   In Windows explorer, users could use “drag” or “copy and paste” to perform copy offload
-   When the source LUN and destination LUN are mounted with the file system, the app must only call FSCTL\_Offload\_Read and FSCTL\_Offload\_Write to perform data transfer from the source LUN to the destination LUN
-   If a copy offload operation fails, the storage device’s copy manager must return the proper additional sense data for apps’ error handling
-   When the source LUN or destination LUN is not mounted with the file system and locked, the app must call IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES with DeviceDsmAction\_OffloadRead or DeviceDsmAction\_OffloadWrite action to perform copy offload
-   Storage management apps may use SCSI\_PASS\_THROUGH API to perform offloaded data transfers when both source and destination LUNs are not mounted with any file system and locked

## Tests

-   To ensure a robust user experience, verify the Windows ODX certification of the storage array
-   The storage device must comply with Windows Offloaded Data Transfers certification (used to be Logo) requirements to support ODX feature
-   Use the Windows Offloaded Data Transfers Hardware Certification Kit to verify the ODX feature support of the storage devices

## Resources

-   T10 XCOPY Lite Spec (11-059r8)
    -   [https://www.t10.org/cgi-bin/ac.pl?t=f&f=spc4r35b.pdf](https://www.t10.org/cgi-bin/ac.pl?t=f&f=spc4r35b.pdf)
    -   [https://www.t10.org/cgi-bin/ac.pl?t=f&f=sbc3r30.pdf](https://www.t10.org/cgi-bin/ac.pl?t=f&f=sbc3r30.pdf)
-   [Hardware Dashboard Services](/windows-hardware/drivers/dashboard/)
-   [SCSI\_PASS\_THROUGH Structure](/windows-hardware/drivers/ddi/ntddscsi/ns-ntddscsi-_scsi_pass_through)

 

 