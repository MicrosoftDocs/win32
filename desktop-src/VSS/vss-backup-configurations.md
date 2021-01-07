---
description: There are a number of conventionally supported backup types&\#8212;incremental, differential, and full&\#8212;that VSS is aware of, as well as a backup configuration peculiar to VSS.
ms.assetid: eddf29bc-221b-4b10-9842-a893b62fa846
title: VSS Backup Configurations
ms.topic: article
ms.date: 05/31/2018
---

# VSS Backup Configurations

There are a number of conventionally supported backup types—incremental, differential, and full—that VSS is aware of, as well as a backup configuration peculiar to VSS.

In defining a backup configuration, a requester and the writers on a system indicate how data will be written to a storage device, how the shadow copy mechanism will be deployed, and what information needs to be saved. Interaction between writers and requesters is determined by the type of backup a requester wants to perform and the kinds (or schemas) that each writer can support:

-   [VSS Backup State](vss-backup-state.md)
-   [Writer Backup Schema Support](writer-backup-schema-support.md)
-   [File Level Schema Support](file-level-schema-support.md)

 

 



