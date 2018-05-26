---
title: System.MessageStore.Folder object
description: Defines the properties for individual Windows Mail (formerly Outlook Express) folders as well as the properties for the Messages collection.
ms.assetid: 989794bd-6b4c-4112-8356-c5e2a5c5df8b
keywords:
- System.MessageStore.Folder object Windows Sidebar
- System.MessageStore.Folder object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.MessageStore.Folder
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.MessageStore.Folder object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties for individual Windows Mail (formerly Outlook Express) folders as well as the properties for the [**Messages**](system-messagestorefolder-messages.md) collection.

> [!Note]  
> Objects of type [**System.MessageStore.Message**](system-messagestore-message.md) can only be accessed through the [**Messages**](system-messagestorefolder-messages.md) collection. This collection is a member of **System.MessageStore.Folder**.

 

## Members

The **System.MessageStore.Folder** object has these types of members:

-   [Collections](#events)
-   [Properties](#properties)

### Collections

The **System.MessageStore.Folder** object has these collections.



| Collection                                             | Description                                                                                                  |
|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| [**Messages**](system-messagestorefolder-messages.md) | A collection of [**System.MessageStore.Message**](system-messagestore-message.md) object types. <br/> |



 

### Properties

The **System.MessageStore.Folder** object has these properties.



| Property                                                                              | Access type          | Description                                                              |
|:--------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------|
| [**messageCount**](system-messagestorefolder-messagecount.md)<br/>             | Read-only<br/> | Gets the number of messages in a Windows Mail folder. <br/>        |
| [**name**](system-messagestorefolder-name.md)<br/>                             | Read-only<br/> | Gets the Windows Mail folder name. <br/>                           |
| [**unreadMessageCount**](system-messagestorefolder-unreadmessagecount.md)<br/> | Read-only<br/> | Gets the number of unread messages in a Windows Mail folder. <br/> |



 

## Remarks

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



 

 





