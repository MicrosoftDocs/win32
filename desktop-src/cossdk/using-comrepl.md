---
description: Using COMREPL
ms.assetid: bf67b434-c082-472d-9eae-ae31969d9cb8
title: Using COMREPL
ms.topic: article
ms.date: 05/31/2018
---

# Using COMREPL

To launch the COMREPL command line utility, use the following steps:

1.  Add %windir%\\system32\\Com to the default environment path by typing the following in the command prompt:

    **set path = %PATH%;%windir%\\system32\\Com**

2.  Enter the following COMREPL command:

    **COMREPL** *sourceComputer* *targetComputerList* **\[/n \[/v\]\]**

    where:

    -   *sourceComputer* is the computer name of the source

    -   *targetComputerList* is the computer names of the targets separated by spaces

    -   **/n** suppresses confirmation prompt before starting replication

    -   **/v** echoes log file output to the console

## Notes

-   Because COM+ is not replicated (only configuration data and applications), all target computers must already have COM+ installed.
-   The user must pass role checks for the system application on both the source and the target computers.
-   No local machine accounts that may be used by roles are replicated.
-   The target computer(s) must be online.
-   The user is responsible for replicating all non-COM+ data (for example, database tables, data files, and so forth) to the target computer(s).
-   Clusters can participate in replication, but note that COMREPL replicates only to named computers.

## Related topics

<dl> <dt>

[File Management](file-management.md)
</dt> <dt>

[Logging and Error Reporting](logging-and-error-reporting.md)
</dt> <dt>

[Replication Phases](replication-phases.md)
</dt> <dt>

[What Gets Replicated](what-gets-replicated.md)
</dt> </dl>

 

 



