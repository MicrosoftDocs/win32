---
description: Notifications are values that a setup function sends to a callback routine to specify a state or event. Two parameters, Param1 and Param2, are sent with the notification, and contain additional information relevant to the notification.
ms.assetid: '93434558-ae83-4ea2-9324-659e5873a8c3'
title: Notifications (Setup API)
ms.topic: article
ms.date: 05/31/2018
---

# Notifications (Setup API)

Notifications are values that a setup function sends to a callback routine to specify a state or event. Two parameters, *Param1* and *Param2*, are sent with the notification, and contain additional information relevant to the notification.

The callback routine processes the notification and returns an unsigned integer to the setup function. Depending on the setup function, you can use this value to specify an operation or user selection, or you may ignore it.

The setup functions send notifications to callback routines using the following syntax.

``` syntax
MsgHandler(          //the specified callback routine
    Context,         //context used by the callback routine
    Notification,    //notification code
    Param1,          //additional notification information
    Param2           //additional notification information
);
```

The *Context* parameter is a void pointer to a context variable or structure that the callback routine can use to store information that must persist between subsequent calls to the callback routine.

Because the callback routine specifies the context's implementation, and it is never referenced or altered by the setup functions, the context is not documented in the reference material for the notification messages that follow.

The *Notification* parameter specifies an unsigned integer value for an event or state that causes the setup function to call the callback routine.

*Param1* and *Param2* are optional parameters that can contain additional information relevant to the notification. These parameters are unsigned integers. If *Param1* or *Param2* return information that is not an unsigned integer, it is cast to an unsigned integer and must be recast to its original data type before it can be used by the callback routine.

> [!Note]  
> The following notifications represent every notification used by the setup functions. Individual functions use a subset of these notifications. In other words, not every notification is used by every function.

 

The following notifications are used by the setup functions.



| Notification                                                                     | Description                                                                                   |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**SPFILENOTIFY\_COPYERROR**](spfilenotify-copyerror.md)                        | An error occurred during a file copy operation.                                               |
| [**SPFILENOTIFY\_DELETEERROR**](spfilenotify-deleteerror.md)                    | An error occurred during a file deletion operation.                                           |
| [**SPFILENOTIFY\_ENDCOPY**](spfilenotify-endcopy.md)                            | A file copy operation has ended.                                                              |
| [**SPFILENOTIFY\_ENDDELETE**](spfilenotify-enddelete.md)                        | A file deletion operation has ended.                                                          |
| [**SPFILENOTIFY\_ENDQUEUE**](spfilenotify-endqueue.md)                          | The queue has finished committing.                                                            |
| [**SPFILENOTIFY\_ENDREGISTRATION**](spfilenotify-endregistration.md)            | The registration or unregistration of the file has finished.                                  |
| [**SPFILENOTIFY\_ENDRENAME**](spfilenotify-endrename.md)                        | A file rename operation has ended.                                                            |
| [**SPFILENOTIFY\_ENDSUBQUEUE**](spfilenotify-endsubqueue.md)                    | A subqueue (either copy, rename or delete) has ended.                                         |
| [**SPFILENOTIFY\_FILEEXTRACTED**](spfilenotify-fileextracted.md)                | The file has been extracted from the cabinet.                                                 |
| [**SPFILENOTIFY\_FILEINCABINET**](spfilenotify-fileincabinet.md)                | A file is encountered in the cabinet.                                                         |
| [**SPFILENOTIFY\_FILEOPDELAYED**](spfilenotify-fileopdelayed.md)                | The file was in use, and the current operation has been delayed until the system is rebooted. |
| [**SPFILENOTIFY\_LANGMISMATCH**](spfilenotify-langmismatch.md)                  | The language of the current operation does not match the system language.                     |
| [**SPFILENOTIFY\_NEEDMEDIA**](spfilenotify-needmedia.md)                        | New source media is required.                                                                 |
| [**SPFILENOTIFY\_NEEDNEWCABINET**](spfilenotify-neednewcabinet.md)              | The current file is continued in the next cabinet.                                            |
| [**SPFILENOTIFY\_QUEUESCAN**](spfilenotify-queuescan.md)                        | A node in the file queue has been scanned.                                                    |
| [**SPFILENOTIFY\_QUEUESCAN\_EX**](spfilenotify-queuescan-ex.md)                 | A node in the file queue has been scanned.                                                    |
| [**SPFILENOTIFY\_QUEUESCAN\_SIGNERINFO**](spfilenotify-queuescan-signerinfo.md) | A node in the file queue has been scanned.                                                    |
| [**SPFILENOTIFY\_RENAMEERROR**](spfilenotify-renameerror.md)                    | An error occurred during a file rename operation.                                             |
| [**SPFILENOTIFY\_STARTCOPY**](spfilenotify-startcopy.md)                        | A file copy operation has started.                                                            |
| [**SPFILENOTIFY\_STARTDELETE**](spfilenotify-startdelete.md)                    | A file delete operation has started.                                                          |
| [**SPFILENOTIFY\_STARTQUEUE**](spfilenotify-startqueue.md)                      | The queue has started to commit.                                                              |
| [**SPFILENOTIFY\_STARTREGISTRATION**](spfilenotify-startregistration.md)        | The registration or unregistration of the file has started.                                   |
| [**SPFILENOTIFY\_STARTRENAME**](spfilenotify-startrename.md)                    | A file rename operation has started.                                                          |
| [**SPFILENOTIFY\_STARTSUBQUEUE**](spfilenotify-startsubqueue.md)                | A subqueue (either copy, rename or delete) has started.                                       |
| [**SPFILENOTIFY\_TARGETEXISTS**](spfilenotify-targetexists.md)                  | A copy of the specified file already exists on the target.                                    |
| [**SPFILENOTIFY\_TARGETNEWER**](spfilenotify-targetnewer.md)                    | A newer version of the specified file exists on the target.                                   |



 

 

 



