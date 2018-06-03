---
title: Messages.count property
description: Gets the number of System.MessageStore.Message items in the Messages collection.
ms.assetid: 0fd09708-0b6e-4fd4-b27c-a8f9334e9b29
keywords:
- count property Windows Sidebar
- count property Windows Sidebar , Messages collection
- Messages collection Windows Sidebar , count property
topic_type:
- apiref
api_name:
- Messages.count
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

# Messages.count property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of [**System.MessageStore.Message**](system-messagestore-message.md) items in the [**Messages**](system-messagestorefolder-messages.md) collection.

This property is read-only.

## Syntax


```JScript
icount = Messages.count
```



## Property value

An **Integer** that receives the number of items.

## Remarks

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail (formerly Outlook Express) **Local Folders** collection. Sub-folders and their content (such as messages) are not exposed.

## Examples

The following example demonstrates how to access properties for a message in the [**Messages**](system-messagestorefolder-messages.md) collection.


```JScript
var sFlyoutContent = "";
var collFolders = System.MessageStore.Folders; ;

// --------------------------------------------------------------------
// Display the flyout.
// iFolderIndex: The index of the selected folder.
// --------------------------------------------------------------------
function ShowFlyout(iFolderIndex)
{
    var iBodyLength;
    var oMessage = null;
    var collMessages = collFolders.item(iFolderIndex).Messages;
    sFlyoutContent = "<p>" + collMessages.count + " Messages:</p>";
    for (var loop = 0; loop < collMessages.count; loop++)
    {
        oMessage = collMessages.item(loop);
        // Preview a maximum of 100 characters.
        iBodyLength = 100;
        if (oMessage.body.length < 100)
        {
            iBodyLength = oMessage.body.length;
        }
        sFlyoutContent += oMessage.from + "<br />";
        sFlyoutContent += oMessage.subject + "<br />";
        sFlyoutContent += oMessage.to + "<br />";
        sFlyoutContent += oMessage.body.slice(0,iBodyLength) + "<hr />";
    }
    System.Gadget.Flyout.show = true;
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

[**item**](system-messagestorefolder-messages-item.md)
</dt> <dt>

[**System.MessageStore.Message**](system-messagestore-message.md)
</dt> <dt>

[**Messages**](system-messagestorefolder-messages.md)
</dt> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

[**Folders**](system-messagestore-folders.md)
</dt> </dl>

 

 





