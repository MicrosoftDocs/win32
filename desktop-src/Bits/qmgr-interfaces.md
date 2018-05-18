---
title: QMGR Interfaces
description: Use the following Queue Manager (QMGR) interfaces to download files and monitor jobs within the download queue.
ms.assetid: 'b5b59d4f-fa18-4225-8b6f-5d4033c61650'
---

# QMGR Interfaces

\[Queue Manager (QMGR) interfaces are available for use in the operating systems specified in a topic's Requirements section. They may be altered or unavailable in subsequent versions. Instead, use the [BITS interfaces](bits-interfaces.md).\]

Use the following Queue Manager (QMGR) interfaces to download files and monitor jobs within the download queue.



| Interface                                                                 | Description                                                                                                                                                   |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IBackgroundCopyCallback1**](ibackgroundcopycallback1.md)<br/>   | Implement to receive notification when events occur.<br/>                                                                                               |
| [**IBackgroundCopyGroup**](ibackgroundcopygroup.md)<br/>           | Use to manage the group. For example, add a job to the group, set the properties of the group, and start and stop the group in the download queue.<br/> |
| [**IBackgroundCopyJob1**](ibackgroundcopyjob1.md)<br/>             | Use to add files to the job and retrieve the job's status.<br/>                                                                                         |
| [**IBackgroundCopyQMgr**](ibackgroundcopyqmgr.md)<br/>             | Use to create a new group, retrieve an existing group, or enumerate all groups in the queue.<br/>                                                       |
| [**IEnumBackgroundCopyGroups**](ienumbackgroundcopygroups.md)<br/> | Use to retrieve a list of groups in the download queue.<br/>                                                                                            |
| [**IEnumBackgroundCopyJobs1**](ienumbackgroundcopyjobs1.md)<br/>   | Use to retrieve a list of jobs in the group.<br/>                                                                                                       |



 

 

 





