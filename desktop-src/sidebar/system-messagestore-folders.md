---
title: System.MessageStore.Folders property
description: A collection of System.MessageStore.Folder objects.
ms.assetid: 61b440e7-7067-40af-9be0-da992cfc6e0d
keywords:
- Folders property Windows Sidebar
- Folders property Windows Sidebar , System.MessageStore object
- System.MessageStore object Windows Sidebar , Folders property
topic_type:
- apiref
api_name:
- System.MessageStore.Folders
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

# System.MessageStore.Folders property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

A collection of [**System.MessageStore.Folder**](system-messagestore-folder.md) objects.

> [!Note]  
> Objects of type [**System.MessageStore.Folder**](system-messagestore-folder.md) can only be accessed through the **Folders** collection. This collection is a member of [**System.MessageStore**](system-messagestore.md).

 

This property is read-only.

## Syntax


```JScript
objFolders = System.MessageStore.Folders
```



## Property value

A collection of [**System.MessageStore.Folder**](system-messagestore-folder.md) objects.

## Remarks

**Folders** exposes the Windows Mail (formerly Outlook Express) **Local Folders** collection. Subfolders and their content (such as messages) are not exposed.

> [!Note]  
> See the [**Messages Collection**](system-messagestorefolder-messages.md) for information about accessing the `Messages` in a particular folder.

 

## Examples

The following example demonstrates how to use the **Folders Collection** and the [**System.MessageStore.Folder**](system-messagestore-folder.md) properties of each folder.


```JScript
// Create a Folders Collection and assign it to the variable collFolders.
var collFolders = System.MessageStore.Folders; 

// Get the total number of folders in the Folders Collection and assign it to the variable iCount.
var iCount = collFolders.count;

// Select the folder from position 0 in the Folders Collection and assign it to the variable oFolder.
var oFolder = collFolders.item(0);

// Get the name of the folder and assign it to the variable strName.
var strName = oFolder.name;

// Get the number of messages in the folder and assign it to the variable iMsgCount.
var iMsgCount = oFolder.messageCount;

// Get the number of unread messages in the folder and assign it to the variable iUnreadMsgCount.
var iUnreadMsgCount = oFolder.unreadMessageCount;

// Get the folder's Messages Collection and assign it to the variable collMsgs.
var collMsgs = oFolder.Messages;
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

**Reference**
</dt> <dt>

[**count**](system-messagestore-folders-count.md)
</dt> <dt>

[**item**](system-messagestore-folders-item.md)
</dt> <dt>

[**System.MessageStore**](system-messagestore.md)
</dt> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

[**Messages**](system-messagestorefolder-messages.md)
</dt> <dt>

[**System.MessageStore.Message**](system-messagestore-message.md)
</dt> </dl>

 

 





