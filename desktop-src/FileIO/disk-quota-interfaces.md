---
Description: Interfaces used with disk quotas.
ms.assetid: 422d93d9-f4aa-428d-94c1-fdf2dcf4c974
title: Disk Quota Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Disk Quota Interfaces

The following interfaces are used with disk quotas.



| Interface                                          | Description                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**IDiskQuotaControl**](https://msdn.microsoft.com/en-us/library/Aa365009(v=VS.85).aspx)     | Controls the disk quota facilities of a single NTFS file system volume.<br/>                             |
| [**IDiskQuotaEvents**](https://msdn.microsoft.com/en-us/library/Aa365031(v=VS.85).aspx)       | Receives quota-related event notifications.<br/>                                                         |
| [**IDiskQuotaUser**](https://msdn.microsoft.com/en-us/library/Aa365033(v=VS.85).aspx)           | Represents a single user quota entry in the volume quota information file.<br/>                          |
| [**IDiskQuotaUserBatch**](https://msdn.microsoft.com/en-us/library/Aa365034(v=VS.85).aspx) | Adds multiple quota user objects to a container that is then submitted for update in a single call.<br/> |
| [**IEnumDiskQuotaUsers**](https://msdn.microsoft.com/en-us/library/Aa365054(v=VS.85).aspx) | Enumerates user quota entries on the volume.<br/>                                                        |



 

 

 




