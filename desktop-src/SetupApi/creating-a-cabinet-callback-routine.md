---
description: Because the Setup API does not supply a default cabinet callback routine, you need to supply a routine. The callback routine that the SetupIterateCabinet function requires must have the same form as those pointed to by FileCallback.
ms.assetid: 45a2690e-1db6-4a09-a141-9e68ebc2a6d8
title: Creating a Cabinet Callback Routine
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Cabinet Callback Routine

Because the Setup API does not supply a default cabinet callback routine, you need to supply a routine. The callback routine that the [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta) function requires must have the same form as those pointed to by [FileCallback](/windows/win32/api/setupapi/nc-setupapi-psp_file_callback_a).

Following is the syntax that [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta) uses to send a notification to the callback routine.

``` syntax
MsgHandler(          //the specified callback routine
    Context,         //context used by the callback routine
    Notification,    //cabinet notification
    Param1,          //additional notification information
    Param2           //additional notification information
);
```

The *Context* parameter is a void pointer to a context variable or structure that can be used by the callback routine to store information that needs to persist between subsequent calls to the callback routine.

This context's implementation is specified by the callback routine, and it is never referenced or altered by [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta).

The *Notification* parameter is an unsigned integer and will be one of the following values.



| Notification                                                        | Description                                        |
|---------------------------------------------------------------------|----------------------------------------------------|
| [**SPFILENOTIFY\_FILEEXTRACTED**](spfilenotify-fileextracted.md)   | The file has been extracted from the cabinet.      |
| [**SPFILENOTIFY\_FILEINCABINET**](spfilenotify-fileincabinet.md)   | A file is encountered in the cabinet.              |
| [**SPFILENOTIFY\_NEEDNEWCABINET**](spfilenotify-neednewcabinet.md) | The current file is continued in the next cabinet. |



 

The final two parameters, *Param1* and *Param2*, are also unsigned integers and contain additional information relevant to the notification. For more information about the notifications sent by [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta), see [Cabinet File Notifications](cabinet-file-notifications.md).

A SP\_FILE\_NOTIFY\_CALLBACK routine returns an unsigned integer. The cabinet callback routine should return one of the following values depending on the notification.

For the SPFILENOTIFY\_FILEINCABINET notification, [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta) expects one of the following values to be returned by the callback routine.



| Value         | Meaning                   |
|---------------|---------------------------|
| FILEOP\_ABORT | Abort cabinet processing. |
| FILEOP\_DOIT  | Extract the current file. |
| FILEOP\_SKIP  | Skip the current file.    |



 

For SPFILENOTIFY\_NEEDNEWCABINET and SPFILENOTIFY\_FILEEXTRACTED notifications, **SetupIterateCabinet** expects one of the following values to be returned by the callback routine.



| Value      | Meaning                                                                                                                                                                                                                           |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NO\_ERROR  | No error was encountered, continue processing the cabinet.                                                                                                                                                                        |
| ERROR\_XXX | An error of the specified type occurred. The [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta) function will return **FALSE**, and the specified error code will be returned by a call to [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror). |



 

If the callback routine returns FILEOP\_DOIT, the routine must also provide a full target path. For more information see [**SPFILENOTIFY\_FILEINCABINET**](spfilenotify-fileincabinet.md).

 

 
