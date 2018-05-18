---
title: System.MessageStore.Folder.Messages property
description: A collection of System.MessageStore.Message object types.
ms.assetid: '15bb10d0-1815-4818-98c2-abde036e560c'
keywords: ["Messages property Windows Sidebar", "Messages property Windows Sidebar , System.MessageStore.Folder object", "System.MessageStore.Folder object Windows Sidebar , Messages property"]
topic_type:
- apiref
api_name:
- System.MessageStore.Folder.Messages
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.MessageStore.Folder.Messages property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

A collection of [**System.MessageStore.Message**](system-messagestore-message.md) object types.

This property is read-only.

## Syntax


```JScript
objMessages = System.MessageStore.Folder.Messages
```



## Property value

A collection of [**System.MessageStore.Message**](system-messagestore-message.md) object types.

## Remarks

**Messages** represents the collection of Windows Mail (formerly Outlook Express) messages in a folder from the [**Folders**](system-messagestore-folders.md) collection.

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail **Local Folders** collection. Sub-folders and their content (such as messages) are not exposed.

## Examples

The following example demonstrates how to use the [**Folders**](system-messagestore-folders.md) and **Messages** collections to select a message and find the value of the `subject` property for that message.


```JScript
// Create a Folders Collection object and assign it to the variable collFolders.
var collFolders = System.MessageStore.Folders; 

// Select the folder from position 0 in the Folders Collection and assign it to the variable oFolder.
var oFolder = collFolders.item(0); 

// Get the Messages Collection from folder oFolder, and assign it to the variable collMsgs.
var collMsgs = oFolder.Messages; 

// Get the message from position 2 in the Messages Collection and assign it to the variable oMsg.
// oMsg is an instance of a System.MessageStoreMessage object.
var oMsg = collMsgs.item(2); 

// Access the "subject" property of the oMsg object and assign it to the string variable strSubjectLine.
var strSubjectLine = oMsg.subject;
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

**Reference**
</dt> <dt>

[**count**](system-messagestorefolder-messages-count.md)
</dt> <dt>

[**item**](system-messagestorefolder-messages-item.md)
</dt> <dt>

[**System.MessageStore.Message**](system-messagestore-message.md)
</dt> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

[**System.MessageStore**](system-messagestore.md)
</dt> <dt>

[**Folders**](system-messagestore-folders.md)
</dt> </dl>

 

 





