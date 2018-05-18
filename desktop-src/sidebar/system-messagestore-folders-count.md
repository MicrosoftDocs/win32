---
title: Folders.count property
description: Gets the number of System.MessageStore.Folder items in the Folders collection.
ms.assetid: '34643941-a94e-4158-a680-8c78307c0485'
keywords: ["count property Windows Sidebar", "count property Windows Sidebar , Folders collection", "Folders collection Windows Sidebar , count property"]
topic_type:
- apiref
api_name:
- Folders.count
api_location:
- Sidebar.Exe
api_type:
- COM
---

# Folders.count property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of [**System.MessageStore.Folder**](system-messagestore-folder.md) items in the [**Folders**](system-messagestore-folders.md) collection.

This property is read-only.

## Syntax


```JScript
icount = Folders.count
```



## Property value

An **Integer** that receives the number of items.

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

[**item**](system-messagestore-folders-item.md)
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

 

 





