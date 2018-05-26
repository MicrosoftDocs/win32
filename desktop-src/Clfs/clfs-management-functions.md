---
Description: The Common Log File System (CLFS) API includes the following functions.
ms.assetid: a8bcfdc6-3056-4f82-825b-f224100d87cb
title: CLFS Management Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CLFS Management Functions

The Common Log File System (CLFS) API includes the following functions.



| Function                                                                              | Description                                                                                                                  |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**DeregisterManageableLogClient**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-deregistermanageablelogclient?branch=master)<br/>     | Deregisters a client with the log manager.<br/>                                                                        |
| [**HandleLogFull**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-handlelogfull?branch=master)<br/>                                     | Called by a managed log client when an attempt to reserve or append to a log fails with a log full error message.<br/> |
| [**InstallLogPolicy**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-installlogpolicy?branch=master)<br/>                               | Installs a policy for a log.<br/>                                                                                      |
| [**LogTailAdvanceFailure**](/windows/win32/ClfsMgmtw32/nf-clfsmgmtw32-logtailadvancefailure?branch=master)<br/>                     | Called by a log client to indicate that it cannot comply with a request from the log manager to advance its tail.<br/> |
| [**QueryLogPolicy**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-querylogpolicy?branch=master)<br/>                                   | Allows you to obtain a policy that is installed for the specified log.<br/>                                            |
| [**ReadLogNotification**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-readlognotification?branch=master)<br/>                         | Retrieves notifications from the log manager.<br/>                                                                     |
| [**RegisterForLogWriteNotification**](/windows/win32/ClfsMgmtw32/nf-clfsmgmtw32-registerforlogwritenotification?branch=master)<br/> | Enables or disables log write notifications.<br/>                                                                      |
| [**RemoveLogPolicy**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-removelogpolicy?branch=master)<br/>                                 | Resets the specified policy to its default behavior.<br/>                                                              |
| [**RegisterManageableLogClient**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-registermanageablelogclient?branch=master)<br/>         | Registers a client with the log manager.<br/>                                                                          |
| [**SetLogFileSizeWithPolicy**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-setlogfilesizewithpolicy?branch=master)<br/>               | Adds or deletes containers from a log according to the installed policies.<br/>                                        |



 

 

 




