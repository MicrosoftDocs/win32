---
description: Interfaces used with disk quotas.
ms.assetid: 422d93d9-f4aa-428d-94c1-fdf2dcf4c974
title: Disk Quota Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Disk Quota Interfaces

The following interfaces are used with disk quotas.



| Interface                                          | Description                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**IDiskQuotaControl**](/windows/win32/api/dskquota/nn-dskquota-idiskquotacontrol)     | Controls the disk quota facilities of a single NTFS file system volume.<br/>                             |
| [**IDiskQuotaEvents**](/windows/win32/api/dskquota/nn-dskquota-idiskquotaevents)       | Receives quota-related event notifications.<br/>                                                         |
| [**IDiskQuotaUser**](/windows/win32/api/dskquota/nn-dskquota-idiskquotauser)           | Represents a single user quota entry in the volume quota information file.<br/>                          |
| [**IDiskQuotaUserBatch**](/windows/win32/api/dskquota/nn-dskquota-idiskquotauserbatch) | Adds multiple quota user objects to a container that is then submitted for update in a single call.<br/> |
| [**IEnumDiskQuotaUsers**](/windows/win32/api/dskquota/nn-dskquota-ienumdiskquotausers) | Enumerates user quota entries on the volume.<br/>                                                        |



 

 

