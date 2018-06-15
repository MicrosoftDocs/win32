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
| [**IDiskQuotaControl**](https://msdn.microsoft.com/en-us/library/Aa365009(v=VS.85).aspx)<br/>     | Controls the disk quota facilities of a single NTFS file system volume.<br/>                             |
| [**IDiskQuotaEvents**](https://msdn.microsoft.com/en-us/library/Aa365031(v=VS.85).aspx)<br/>       | Receives quota-related event notifications.<br/>                                                         |
| [**IDiskQuotaUser**](https://msdn.microsoft.com/en-us/library/Aa365033(v=VS.85).aspx)<br/>           | Represents a single user quota entry in the volume quota information file.<br/>                          |
| [**IDiskQuotaUserBatch**](https://msdn.microsoft.com/en-us/library/Aa365034(v=VS.85).aspx)<br/> | Adds multiple quota user objects to a container that is then submitted for update in a single call.<br/> |
| [**IEnumDiskQuotaUsers**](https://msdn.microsoft.com/en-us/library/Aa365054(v=VS.85).aspx)<br/> | Enumerates user quota entries on the volume.<br/>                                                        |



 

 

 




