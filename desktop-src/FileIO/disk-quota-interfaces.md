---
Description: Interfaces used with disk quotas.
ms.assetid: 422d93d9-f4aa-428d-94c1-fdf2dcf4c974
title: Disk Quota Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Disk Quota Interfaces

The following interfaces are used with disk quotas.



| Interface                                          | Description                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**IDiskQuotaControl**](/windows/win32/Dskquota/?branch=master)     | Controls the disk quota facilities of a single NTFS file system volume.<br/>                             |
| [**IDiskQuotaEvents**](/windows/win32/Dskquota/?branch=master)       | Receives quota-related event notifications.<br/>                                                         |
| [**IDiskQuotaUser**](/windows/win32/Dskquota/?branch=master)           | Represents a single user quota entry in the volume quota information file.<br/>                          |
| [**IDiskQuotaUserBatch**](/windows/win32/Dskquota/?branch=master) | Adds multiple quota user objects to a container that is then submitted for update in a single call.<br/> |
| [**IEnumDiskQuotaUsers**](/windows/win32/Dskquota/?branch=master) | Enumerates user quota entries on the volume.<br/>                                                        |



 

 

 




