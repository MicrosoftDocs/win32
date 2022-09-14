---
description: The default queue callback routine handles notifications sent by SetupCommitFileQueue in a generic manner.
ms.assetid: 6f2b3b9f-86e5-42af-8adc-29a1c768d106
title: About the Default Queue Callback Routine
ms.topic: article
ms.date: 05/31/2018
---

# About the Default Queue Callback Routine

The default queue callback routine handles notifications sent by [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) in a generic manner. By using the default routine, you get a ready-made user interface to create common setup dialog boxes. It is recommended that you use the default queue callback routine, both for ease of use, and to ensure a consistent appearance and behavior of dialog boxes generated during the installation.

The default callback routine requires a context structure for internal record keeping. In addition, the queue passes additional information relevant to the current notification in a set of parameters, *Param1* and *Param2*.

For example, if the queue sends an SPFILENOTIFY\_NEEDMEDIA notification to the default callback routine, *Param1* points to a [**SOURCE\_MEDIA**](/windows/desktop/api/Setupapi/ns-setupapi-source_media_a) structure that contains information about the media needed, and *Param2* points to a character array that can receive new path information from the user.

The default callback routine uses this information to prompt the user to either insert the needed source media, specify a new path, skip copying the current file, or cancel the current operation. The default queue callback routine returns FILEOP\_NEWPATH, FILEOP\_DOIT , FILEOP\_SKIP, or FILEOP\_ABORT to the queue, depending on which action the user took.

For information on how the default queue callback routine handles each queue notification, see [File Queue Notifications](file-queue-notifications.md).

For information on custom queue callback routines, see [Creating a Custom Queue Callback Routine](creating-a-custom-queue-callback-routine.md).

 

 



