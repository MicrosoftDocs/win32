---
Description: Interfaces used in disk management.
ms.assetid: c1f79e2e-834b-41dc-a15f-6dd1034d021b
title: Disk Management Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Disk Management Interfaces

The following interfaces are used in disk management.

## In this section



| Interface                                                     | Description                                                                                                    |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**IDiskQuotaControl**](/windows/desktop/api/Dskquota/)<br/>     | Controls the disk quota facilities of a single NTFS file system volume.<br/>                             |
| [**IDiskQuotaEvents**](/windows/desktop/api/Dskquota/)<br/>       | Receives quota-related event notifications.<br/>                                                         |
| [**IDiskQuotaUser**](/windows/desktop/api/Dskquota/)<br/>           | Represents a single user quota entry in the volume quota information file.<br/>                          |
| [**IDiskQuotaUserBatch**](/windows/desktop/api/Dskquota/)<br/> | Adds multiple quota user objects to a container that is then submitted for update in a single call.<br/> |
| [**IEnumDiskQuotaUsers**](/windows/desktop/api/Dskquota/)<br/> | Enumerates user quota entries on the volume.<br/>                                                        |



 

 

 




