---
description: To enable the transfer of application files, COMREPL automatically manages sets of file system folders on the source and target. These COMREPL folders are all rooted in %systemdir%\\com\\replication.
ms.assetid: 8c59577b-34ea-4675-aaea-a2732fd5ce14
title: File Management (Component Services)
ms.topic: article
ms.date: 05/31/2018
---

# File Management

To enable the transfer of application files, COMREPL automatically manages sets of file system folders on the source and target. These COMREPL folders are all rooted in %systemdir%\\com\\replication.

## Source folders



| Folder                   | Purpose                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ReplicaSource<br/> | Applications exported during the prepare phase are stored here.<br/> This folder is overwritten each time the prepare phase is executed against a given source computer. This folder is never explicitly deleted, so replication to targets can take place at any time after the source is prepared.<br/> Each application is stored in its own subfolder named <appName>+<appID>.<br/> |



 

## Target folders



| Folder                    | Purpose                                                                                                                                                                                                                                                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ReplicaNew<br/>     | The copy phase copies all files and subfolders from ReplicaSource on the source to ReplicaNew on the target. Any previous contents of ReplicaNew are deleted each time the copy phase is run against a given target.<br/> This folder exists only while the replication process is running. (See ReplicaCurrent.)<br/>           |
| ReplicaCurrent<br/> | The replicated applications currently installed on the target are stored here.<br/> When the install phase is started, the ReplicaNew folder is renamed to ReplicaCurrent. If there is an existing ReplicaCurrent folder, it is renamed to ReplicaOld. If there is an existing ReplicaOld folder, its contents are deleted.<br/> |
| ReplicaOld<br/>     | Saves the application files installed during the next to last replication. These files are saved for backup purposes only.<br/>                                                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Logging and Error Reporting](logging-and-error-reporting.md)
</dt> <dt>

[Replication Phases](replication-phases.md)
</dt> <dt>

[Using COMREPL](using-comrepl.md)
</dt> <dt>

[What Gets Replicated](what-gets-replicated.md)
</dt> </dl>

 

 




