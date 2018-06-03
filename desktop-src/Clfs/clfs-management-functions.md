---
Description: The Common Log File System (CLFS) API includes the following functions.
ms.assetid: a8bcfdc6-3056-4f82-825b-f224100d87cb
title: CLFS Management Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLFS Management Functions

The Common Log File System (CLFS) API includes the following functions.



| Function                                                                              | Description                                                                                                                  |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**DeregisterManageableLogClient**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-deregistermanageablelogclient)<br/>     | Deregisters a client with the log manager.<br/>                                                                        |
| [**HandleLogFull**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-handlelogfull)<br/>                                     | Called by a managed log client when an attempt to reserve or append to a log fails with a log full error message.<br/> |
| [**InstallLogPolicy**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-installlogpolicy)<br/>                               | Installs a policy for a log.<br/>                                                                                      |
| [**LogTailAdvanceFailure**](/windows/desktop/api/ClfsMgmtw32/nf-clfsmgmtw32-logtailadvancefailure)<br/>                     | Called by a log client to indicate that it cannot comply with a request from the log manager to advance its tail.<br/> |
| [**QueryLogPolicy**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-querylogpolicy)<br/>                                   | Allows you to obtain a policy that is installed for the specified log.<br/>                                            |
| [**ReadLogNotification**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-readlognotification)<br/>                         | Retrieves notifications from the log manager.<br/>                                                                     |
| [**RegisterForLogWriteNotification**](/windows/desktop/api/ClfsMgmtw32/nf-clfsmgmtw32-registerforlogwritenotification)<br/> | Enables or disables log write notifications.<br/>                                                                      |
| [**RemoveLogPolicy**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-removelogpolicy)<br/>                                 | Resets the specified policy to its default behavior.<br/>                                                              |
| [**RegisterManageableLogClient**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-registermanageablelogclient)<br/>         | Registers a client with the log manager.<br/>                                                                          |
| [**SetLogFileSizeWithPolicy**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-setlogfilesizewithpolicy)<br/>               | Adds or deletes containers from a log according to the installed policies.<br/>                                        |



 

 

 




