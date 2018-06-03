---
title: System.MessageStore.Message.subject property
description: Gets the Subject field of a Windows Mail (formerly Outlook Express) message.
ms.assetid: 6c7349cd-3540-45bf-b6aa-8895d740bb19
keywords:
- subject property Windows Sidebar
- subject property Windows Sidebar , System.MessageStore.Message object
- System.MessageStore.Message object Windows Sidebar , subject property
topic_type:
- apiref
api_name:
- System.MessageStore.Message.subject
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

# System.MessageStore.Message.subject property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the **Subject** field of a Windows Mail (formerly Outlook Express) message.

This property is read-only.

## Syntax


```JScript
strsubject = System.MessageStore.Message.subject
```



## Property value

A **String** that receives the Subject field.

## Remarks

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail **Local Folders** collection. Subfolders and their content (such as messages) are not exposed.

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

[**System.MessageStore.Message**](system-messagestore-message.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**body**](system-messagestoremessage-body.md)
</dt> <dt>

[**from**](system-messagestoremessage-from.md)
</dt> <dt>

[**to**](system-messagestoremessage-to.md)
</dt> <dt>

[**System.MessageStore**](system-messagestore.md)
</dt> <dt>

[**Folders**](system-messagestore-folders.md)
</dt> <dt>

[**System.MessageStore.Folder**](system-messagestore-folder.md)
</dt> <dt>

[**Messages**](system-messagestorefolder-messages.md)
</dt> </dl>

 

 





