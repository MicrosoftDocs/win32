---
title: System.MessageStore.Folder.name property
description: Gets the Windows Mail (formerly Outlook Express) folder name.
ms.assetid: 'ff1dcee7-bc88-49d5-93e8-ed016017661d'
keywords: ["name property Windows Sidebar", "name property Windows Sidebar , System.MessageStore.Folder object", "System.MessageStore.Folder object Windows Sidebar , name property"]
topic_type:
- apiref
api_name:
- System.MessageStore.Folder.name
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.MessageStore.Folder.name property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Windows Mail (formerly Outlook Express) folder name.

This property is read-only.

## Syntax


```JScript
strname = System.MessageStore.Folder.name
```



## Property value

A **String** that receives the folder name.

## Remarks

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail **Local Folders** collection. Sub-folders and their content (such as messages) are not exposed.

## Examples

The following example demonstrates how to retrieve a folder name.


```JScript
// Create a Folders Collection.
var collFolders = System.MessageStore.Folders; 

// Select the folder from position 0 in the Folders Collection.
var oFolder = collFolders.item(0);

// Get the folder name.
var strFolderName = oFolder.name;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**unreadMessageCount**](system-messagestorefolder-unreadmessagecount.md)
</dt> <dt>

[**messageCount**](system-messagestorefolder-messagecount.md)
</dt> <dt>

[**Folders**](system-messagestore-folders.md)
</dt> </dl>

 

 





