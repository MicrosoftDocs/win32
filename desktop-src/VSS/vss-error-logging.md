---
description: 'The following VSS error and state information is written to the Application Event Log:'
ms.assetid: d0b0f012-ad4f-4bd8-bb97-98f212bcbe81
title: VSS Error Logging
ms.topic: article
ms.date: 05/31/2018
---

# VSS Error Logging

The following VSS error and state information is written to the Application Event Log:

-   Requester errors produced using the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface
-   Writer errors produced in using the [**CVssWriter**](/windows/desktop/api/VsWriter/nl-vswriter-cvsswriter) class, including overriding methods
-   Default-provider-generated errors
-   VSS service errors generated in coordinating provider, writer, and requester activity (such as the generation of events)

These errors might have a number of causes, including a programming error in third-party code or VSS-related configuration errors.

VSS drivers and lower-level implementation functionality write errors to the System Log. Third-party software (requester, provider, writer) can choose the Application Log, the System Log, or both, to write error log entries.

It is recommended that high-level applications (such as user-mode code) use the Application Log. Lower-level applications, such as hardware interfaces and drivers, should use the System Log.

 

 



