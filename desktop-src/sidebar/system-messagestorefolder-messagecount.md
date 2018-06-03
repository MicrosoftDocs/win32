---
title: System.MessageStore.Folder.messageCount property
description: Gets the number of messages in a Windows Mail (formerly Outlook Express) folder.
ms.assetid: 4b85afa9-1d2f-4f48-86f5-83a25f3b72e6
keywords:
- messageCount property Windows Sidebar
- messageCount property Windows Sidebar , System.MessageStore.Folder object
- System.MessageStore.Folder object Windows Sidebar , messageCount property
topic_type:
- apiref
api_name:
- System.MessageStore.Folder.messageCount
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.MessageStore.Folder.messageCount property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of messages in a Windows Mail (formerly Outlook Express) folder.

This property is read-only.

## Syntax


```JScript
imessageCount = System.MessageStore.Folder.messageCount
```



## Property value

An **Integer** that receives the number of messages.

## Remarks

Eliminates the need to create a [**Messages**](system-messagestorefolder-messages.md) collection and use [**count**](system-messagestorefolder-messages-count.md) to get the number of messages in a folder.

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail **Local Folders** collection. Subfolders and their content (such as messages) are not exposed.

## Examples

The following example demonstrates how to retrieve the number of messages in a given folder.


```JScript
// Create a Folders Collection.
var collFolders = System.MessageStore.Folders; 

// Select the folder from position 0 in the Folders Collection.
var oFolder = collFolders.item(0);

// Get the number of messages in the folder.
var iMsgCount = oFolder.messageCount;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**name**](system-messagestorefolder-name.md)
</dt> <dt>

[**unreadMessageCount**](system-messagestorefolder-unreadmessagecount.md)
</dt> <dt>

[**Folders**](system-messagestore-folders.md)
</dt> </dl>

 

 





