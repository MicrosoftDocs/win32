---
title: System.MessageStore.Message object
description: Defines the properties of each member of the Windows Mail (formerly Outlook Express) Messages collection.
ms.assetid: 5fe4dbf0-c178-401b-9541-e604c20b7441
keywords:
- System.MessageStore.Message object Windows Sidebar
- System.MessageStore.Message object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.MessageStore.Message
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.MessageStore.Message object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties of each member of the Windows Mail (formerly Outlook Express) [**Messages**](system-messagestorefolder-messages.md) collection.

## Members

The **System.MessageStore.Message** object has these types of members:

-   [Properties](#properties)

### Properties

The **System.MessageStore.Message** object has these properties.



| Property                                                         | Access type          | Description                                                       |
|:-----------------------------------------------------------------|:---------------------|:------------------------------------------------------------------|
| [**body**](system-messagestoremessage-body.md)<br/>       | Read-only<br/> | Gets the Windows Mail message body. <br/>                   |
| [**from**](system-messagestoremessage-from.md)<br/>       | Read-only<br/> | Gets the **From** field of a Windows Mail message. <br/>    |
| [**subject**](system-messagestoremessage-subject.md)<br/> | Read-only<br/> | Gets the **Subject** field of a Windows Mail message. <br/> |
| [**to**](system-messagestoremessage-to.md)<br/>           | Read-only<br/> | Gets the **To** field of a Windows Mail message. <br/>      |



 

## Remarks

Each **System.MessageStore.Message** in the [**Messages**](system-messagestorefolder-messages.md) collection corresponds to a message in a Windows Mail folder.

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail **Local Folders** collection. Subfolders and their content (such as messages) are not exposed.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





