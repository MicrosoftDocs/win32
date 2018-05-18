---
Description: 'The Common Log File System (CLFS) API includes the following functions.'
ms.assetid: 'a8bcfdc6-3056-4f82-825b-f224100d87cb'
title: CLFS Management Functions
---

# CLFS Management Functions

The Common Log File System (CLFS) API includes the following functions.



| Function                                                                              | Description                                                                                                                  |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**DeregisterManageableLogClient**](deregistermanageablelogclient.md)<br/>     | Deregisters a client with the log manager.<br/>                                                                        |
| [**HandleLogFull**](handlelogfull.md)<br/>                                     | Called by a managed log client when an attempt to reserve or append to a log fails with a log full error message.<br/> |
| [**InstallLogPolicy**](installlogpolicy.md)<br/>                               | Installs a policy for a log.<br/>                                                                                      |
| [**LogTailAdvanceFailure**](logtailadvancefailure.md)<br/>                     | Called by a log client to indicate that it cannot comply with a request from the log manager to advance its tail.<br/> |
| [**QueryLogPolicy**](querylogpolicy.md)<br/>                                   | Allows you to obtain a policy that is installed for the specified log.<br/>                                            |
| [**ReadLogNotification**](readlognotification.md)<br/>                         | Retrieves notifications from the log manager.<br/>                                                                     |
| [**RegisterForLogWriteNotification**](registerforlogwritenotification.md)<br/> | Enables or disables log write notifications.<br/>                                                                      |
| [**RemoveLogPolicy**](removelogpolicy.md)<br/>                                 | Resets the specified policy to its default behavior.<br/>                                                              |
| [**RegisterManageableLogClient**](registermanageablelogclient.md)<br/>         | Registers a client with the log manager.<br/>                                                                          |
| [**SetLogFileSizeWithPolicy**](setlogfilesizewithpolicy.md)<br/>               | Adds or deletes containers from a log according to the installed policies.<br/>                                        |



 

 

 




