---
description: COMREPL does its work in three phases.
ms.assetid: e9ba8db6-ff6f-4e49-b91b-465e3fa77f27
title: Replication Phases
ms.topic: article
ms.date: 05/31/2018
---

# Replication Phases

COMREPL does its work in three phases. The replication process is divided into distinct phases for the following two reasons:

-   To separate work done to prepare the source from work that is done on each target
-   To delay modification of the target until all data has been acquired from the source

The replication phases are as follows.



| Phase         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Prepare phase | Exports all the installed applications locally on the source computer. This phase does not touch the configuration of any targets.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Copy phase    | Copies data to a target computer. All applications exported on the source are copied to the target. This is a file copy operation. (See [File Management](file-management.md).) This step also acquires some data from the source computer that is not encapsulated within exported application files (for example, application identities). This data is held in memory within COMREPL. This phase does not touch the configuration of any target computers.                                                                               |
| Install phase | Installs source catalog on a target computer. When this step is initiated, all data required to reconfigure the target is within application files in the target's file system or is held as instance data within COMREPL. This phase will delete all the installed applications on the target (except the applications described in [What Gets Replicated](what-gets-replicated.md)) prior to installing the applications copied from the source. COMREPL installs on multiple targets concurrently by using an install thread per target. |



 

## Related topics

<dl> <dt>

[File Management](file-management.md)
</dt> <dt>

[Logging and Error Reporting](logging-and-error-reporting.md)
</dt> <dt>

[Using COMREPL](using-comrepl.md)
</dt> <dt>

[What Gets Replicated](what-gets-replicated.md)
</dt> </dl>

 

 



