---
title: Messages.item property
description: Gets a System.MessageStore.Message object from the Messages collection.
ms.assetid: 0eb64fb3-cb33-4e73-a040-757a771a7196
keywords:
- item property Windows Sidebar
- item property Windows Sidebar , Messages collection
- Messages collection Windows Sidebar , item property
topic_type:
- apiref
api_name:
- Messages.item
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Messages.item property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.MessageStore.Message**](system-messagestore-message.md) object from the [**Messages**](system-messagestorefolder-messages.md) collection.

This property is read-only.

## Syntax


```JScript
objitem = Messages.item
```



## Property value

An **Object** that receives a [**System.Machine.CPU**](system-machine-cpu.md) object from the specified index.

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

[**count**](system-messagestorefolder-messages-count.md)
</dt> <dt>

[**System.MessageStore.Message**](system-messagestore-message.md)
</dt> <dt>

[**Messages**](system-messagestorefolder-messages.md)
</dt> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

[**Folders**](system-messagestore-folders.md)
</dt> </dl>

 

 





