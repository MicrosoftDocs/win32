---
title: Folders.item property
description: Gets a System.MessageStore.Folder object from the Folders collection.
ms.assetid: 773e4664-0b84-43e0-a1f6-5bd40cb7e56f
keywords:
- item property Windows Sidebar
- item property Windows Sidebar , Folders collection
- Folders collection Windows Sidebar , item property
topic_type:
- apiref
api_name:
- Folders.item
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

# Folders.item property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.MessageStore.Folder**](system-messagestore-folder.md) object from the [**Folders**](system-messagestore-folders.md) collection.

This property is read-only.

## Syntax


```JScript
objitem = Folders.item
```



## Property value

An **Object** that receives a [**System.MessageStore.Folder**](system-messagestore-folder.md) object from the specified index.

## Examples

The following example demonstrates how to access properties for folders in the [**Folders**](system-messagestore-folders.md) collection.


```JScript
// Member variables.
var collFolders = null;
var oFolder = null;

// --------------------------------------------------------------------
// Initialize the gadget.
// --------------------------------------------------------------------
function Init()
{
    var sMailInfo = ""; 
    
    // Get the collection of folders from Windows Mail.
    collFolders = System.MessageStore.Folders; 

    // Report the folder details.
    for (var loop = 0; loop < collFolders.count; loop++)
    {
        oFolder = collFolders.item(loop);
        sMailInfo += oFolder.name + "<br/>";
        sMailInfo += "Total messages: " + oFolder.messageCount;
        sMailInfo += " (" + oFolder.unreadMessageCount + " unread)<br/>";
    }    
    
    return sMailInfo;
}
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

[**Folders**](system-messagestore-folders.md)
</dt> <dt>

[**System.MessageStore**](system-messagestore.md)
</dt> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

[**Messages**](system-messagestorefolder-messages.md)
</dt> <dt>

[**System.MessageStore.Message**](system-messagestore-message.md)
</dt> </dl>

 

 





