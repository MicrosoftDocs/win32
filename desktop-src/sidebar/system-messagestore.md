---
title: System.MessageStore object
description: Defines the properties for the Windows Mail (formerly Outlook Express) Folders collection.
ms.assetid: 2825db2a-74e1-4820-9341-618d4e8b0d7b
keywords:
- System.MessageStore object Windows Sidebar
- System.MessageStore object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.MessageStore
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.MessageStore object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties for the Windows Mail (formerly Outlook Express) [**Folders**](system-messagestore-folders.md) collection.

> [!Note]  
> Objects of type [**System.MessageStore.Folder**](system-messagestore-folder.md) can only be accessed through the [**Folders**](system-messagestore-folders.md) collection. This collection is a member of **System.MessageStore**.

 

## Members

The **System.MessageStore** object has these types of members:

-   [Collections](#events)

### Collections

The **System.MessageStore** object has these collections.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Collection</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>Folders</strong>](system-messagestore-folders.md)</td>
<td style="text-align: left;">A collection of [<strong>System.MessageStore.Folder</strong>](system-messagestore-folder.md) objects. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.MessageStore.Folder</strong>](system-messagestore-folder.md) can only be accessed through the [<strong>Folders</strong>](system-messagestore-folders.md) collection. This collection is a member of <strong>System.MessageStore</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

[**Folders**](system-messagestore-folders.md) exposes the Windows Mail **Local Folders** collection. Subfolders and their content (such as messages) are not exposed.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





