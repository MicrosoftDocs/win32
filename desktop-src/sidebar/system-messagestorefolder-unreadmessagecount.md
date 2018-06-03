---
title: System.MessageStore.Folder.unreadMessageCount property
description: Gets the number of unread messages in a Windows Mail (formerly Outlook Express) folder.
ms.assetid: 5e5617a0-a381-4bca-99f2-2e44c1b99260
keywords:
- unreadMessageCount property Windows Sidebar
- unreadMessageCount property Windows Sidebar , System.MessageStore.Folder object
- System.MessageStore.Folder object Windows Sidebar , unreadMessageCount property
topic_type:
- apiref
api_name:
- System.MessageStore.Folder.unreadMessageCount
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

# System.MessageStore.Folder.unreadMessageCount property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of unread messages in a Windows Mail (formerly Outlook Express) folder.

This property is read-only.

## Syntax


```JScript
iunreadMessageCount = System.MessageStore.Folder.unreadMessageCount
```



## Property value

An **Integer** that receives the number of unread messages.

## Remarks

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail **Local Folders** collection. Subfolders and their content (such as messages) are not exposed.

## Examples

The following example demonstrates how to retrieve the number of unread messages in a given folder.


```JScript
// Create a Folders Collection and assign it to the variable collFolders.
var collFolders = System.MessageStore.Folders; 

// Select the folder from position 0 in the Folders Collection and assign it to the variable oFolder.
var oFolder = collFolders.item(0);

// Get the number of unread messages in the folder and assign it to the variable iUnreadMsgCount.
var iUnreadMsgCount = oFolder.unreadMessageCount;
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

[**messageCount**](system-messagestorefolder-messagecount.md)
</dt> <dt>

[**Folders**](system-messagestore-folders.md)
</dt> </dl>

 

 





