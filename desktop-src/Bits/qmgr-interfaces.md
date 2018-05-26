---
title: QMGR Interfaces
description: Use the following Queue Manager (QMGR) interfaces to download files and monitor jobs within the download queue.
ms.assetid: b5b59d4f-fa18-4225-8b6f-5d4033c61650
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# QMGR Interfaces

\[Queue Manager (QMGR) interfaces are available for use in the operating systems specified in a topic's Requirements section. They may be altered or unavailable in subsequent versions. Instead, use the [BITS interfaces](bits-interfaces.md).\]

Use the following Queue Manager (QMGR) interfaces to download files and monitor jobs within the download queue.



| Interface                                                                 | Description                                                                                                                                                   |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IBackgroundCopyCallback1**](/windows/win32/Qmgr/nn-qmgr-ibackgroundcopycallback1?branch=master)<br/>   | Implement to receive notification when events occur.<br/>                                                                                               |
| [**IBackgroundCopyGroup**](/windows/win32/Qmgr/nn-qmgr-ibackgroundcopygroup?branch=master)<br/>           | Use to manage the group. For example, add a job to the group, set the properties of the group, and start and stop the group in the download queue.<br/> |
| [**IBackgroundCopyJob1**](/windows/win32/Qmgr/nn-qmgr-ibackgroundcopyjob1?branch=master)<br/>             | Use to add files to the job and retrieve the job's status.<br/>                                                                                         |
| [**IBackgroundCopyQMgr**](/windows/win32/Qmgr/nn-qmgr-ibackgroundcopyqmgr?branch=master)<br/>             | Use to create a new group, retrieve an existing group, or enumerate all groups in the queue.<br/>                                                       |
| [**IEnumBackgroundCopyGroups**](/windows/win32/Qmgr/nn-qmgr-ienumbackgroundcopygroups?branch=master)<br/> | Use to retrieve a list of groups in the download queue.<br/>                                                                                            |
| [**IEnumBackgroundCopyJobs1**](/windows/win32/Qmgr/nn-qmgr-ienumbackgroundcopyjobs1?branch=master)<br/>   | Use to retrieve a list of jobs in the group.<br/>                                                                                                       |



 

 

 





