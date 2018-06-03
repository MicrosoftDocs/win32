---
title: Rights
description: RMS SDK 2.1 defines the following rights.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0BBFA336-5D7C-4256-99C9-6A70EC6C4452
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_GENERIC_ALL
- IPC_GENERIC_READ
- IPC_GENERIC_WRITE
- IPC_GENERIC_EXTRACT
- IPC_GENERIC_EXPORT
- IPC_GENERIC_PRINT
- IPC_GENERIC_COMMENT
- IPC_READ_RIGHTS
- IPC_WRITE_RIGHTS
- IPC_EMAIL_FORWARD
- IPC_EMAIL_REPLY
- IPC_EMAIL_REPLYALL
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rights

Rights Management Services SDK 2.1 defines the following rights, which are enforced by your application.

> [!Note]  
> AD RMS-enabled applications can interpret these rights differently. This is intended as a general description for how these rights are typically used. Consult the documentation of the specific application for information about how these rights are enforced. For more information, see [AD RMS Policy Template Considerations](https://TechNet.Microsoft.Com/library/dd996658.aspx).

 

<dl> <dt>

<span id="IPC_GENERIC_ALL"></span><span id="ipc_generic_all"></span>**IPC\_GENERIC\_ALL**
</dt> <dd> <dl> <dt>

L"OWNER"
</dt> <dt>



Holders of this right have full access.


</dt> </dl> </dd> <dt>

<span id="IPC_GENERIC_READ"></span><span id="ipc_generic_read"></span>**IPC\_GENERIC\_READ**
</dt> <dd> <dl> <dt>

L"VIEW"
</dt> <dt>



Right to read content.


</dt> </dl> </dd> <dt>

<span id="IPC_GENERIC_WRITE"></span><span id="ipc_generic_write"></span>**IPC\_GENERIC\_WRITE**
</dt> <dd> <dl> <dt>

L"EDIT"
</dt> <dt>



Right to write content.


</dt> </dl> </dd> <dt>

<span id="IPC_GENERIC_EXTRACT"></span><span id="ipc_generic_extract"></span>**IPC\_GENERIC\_EXTRACT**
</dt> <dd> <dl> <dt>

L"EXTRACT"
</dt> <dt>



Right to extract content from a protected format and place it in an unprotected format. Typically, when this right is granted, the application will allow the user to copy and paste information from protected content.

> [!Note]  
> This right should not be used to decrypt files.

 


</dt> </dl> </dd> <dt>

<span id="IPC_GENERIC_EXPORT"></span><span id="ipc_generic_export"></span>**IPC\_GENERIC\_EXPORT**
</dt> <dd> <dl> <dt>

L"EXPORT"
</dt> <dt>



Right to extract content from a protected format and place it in different RMS-protected format. Typically, when this right is granted, the application will allow the user to use the "Save As" feature to save protected content to a new file. The content should be saved with RMS protection.


</dt> </dl> </dd> <dt>

<span id="IPC_GENERIC_PRINT"></span><span id="ipc_generic_print"></span>**IPC\_GENERIC\_PRINT**
</dt> <dd> <dl> <dt>

L"PRINT"
</dt> <dt>



Right to send protected content to a printer device.


</dt> </dl> </dd> <dt>

<span id="IPC_GENERIC_COMMENT"></span><span id="ipc_generic_comment"></span>**IPC\_GENERIC\_COMMENT**
</dt> <dd> <dl> <dt>

L"COMMENT"
</dt> <dt>



Right to add annotations or comments to the content.


</dt> </dl> </dd> <dt>

<span id="IPC_READ_RIGHTS"></span><span id="ipc_read_rights"></span>**IPC\_READ\_RIGHTS**
</dt> <dd> <dl> <dt>

L"VIEWRIGHTSDATA"
</dt> <dt>



Right to read the user rights list and restrictions.


</dt> </dl> </dd> <dt>

<span id="IPC_WRITE_RIGHTS"></span><span id="ipc_write_rights"></span>**IPC\_WRITE\_RIGHTS**
</dt> <dd> <dl> <dt>

L"EDITRIGHTSDATA"
</dt> <dt>



Right to write the user rights list and restrictions.


</dt> </dl> </dd> <dt>

<span id="IPC_EMAIL_FORWARD"></span><span id="ipc_email_forward"></span>**IPC\_EMAIL\_FORWARD**
</dt> <dd> <dl> <dt>

L"FORWARD"
</dt> <dt>



Email applications: the right to forward an email.


</dt> </dl> </dd> <dt>

<span id="IPC_EMAIL_REPLY"></span><span id="ipc_email_reply"></span>**IPC\_EMAIL\_REPLY**
</dt> <dd> <dl> <dt>

L"REPLY"
</dt> <dt>



Email applications: the right to reply to an email.


</dt> </dl> </dd> <dt>

<span id="IPC_EMAIL_REPLYALL"></span><span id="ipc_email_replyall"></span>**IPC\_EMAIL\_REPLYALL**
</dt> <dd> <dl> <dt>

L"REPLYALL"
</dt> <dt>



Email applications: the right to reply all to an email.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



 

 





