---
description: Interfaces used in disk management.
ms.assetid: c1f79e2e-834b-41dc-a15f-6dd1034d021b
title: Disk Management Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Disk Management Interfaces

The following interfaces are used in disk management.

## In this section



| Interface                                                     | Description                                                                                                    |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**IDiskQuotaControl**](/windows/win32/api/dskquota/nn-dskquota-idiskquotacontrol)<br/>     | Controls the disk quota facilities of a single NTFS file system volume.<br/>                             |
| [**IDiskQuotaEvents**](/windows/win32/api/dskquota/nn-dskquota-idiskquotaevents)<br/>       | Receives quota-related event notifications.<br/>                                                         |
| [**IDiskQuotaUser**](/windows/win32/api/dskquota/nn-dskquota-idiskquotauser)<br/>           | Represents a single user quota entry in the volume quota information file.<br/>                          |
| [**IDiskQuotaUserBatch**](/windows/win32/api/dskquota/nn-dskquota-idiskquotauserbatch)<br/> | Adds multiple quota user objects to a container that is then submitted for update in a single call.<br/> |
| [**IEnumDiskQuotaUsers**](/windows/win32/api/dskquota/nn-dskquota-ienumdiskquotausers)<br/> | Enumerates user quota entries on the volume.<br/>                                                        |



 

 

