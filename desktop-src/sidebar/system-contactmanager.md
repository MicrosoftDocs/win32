---
title: System.ContactManager object
description: Defines the properties for the Contacts collection.
ms.assetid: 896e3d29-22e9-485a-8f1f-a5b5bc386fcd
keywords:
- System.ContactManager object Windows Sidebar
- System.ContactManager object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.ContactManager
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

# System.ContactManager object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties for the [**Contacts**](system-contactmanager-contacts.md) collection.

> [!Note]  
> Objects of type [**System.Contact**](system-contact.md) can only be accessed through the [**Contacts**](system-contactmanager-contacts.md) collection. This collection is a member of **System.ContactManager**.

 

## Members

The **System.ContactManager** object has these types of members:

-   [Collections](#events)

### Collections

The **System.ContactManager** object has these collections.



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
<td style="text-align: left;">[<strong>Contacts</strong>](system-contactmanager-contacts.md)</td>
<td style="text-align: left;">A collection of [<strong>System.Contact</strong>](system-contact.md) objects. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Contact</strong>](system-contact.md) can only be accessed through the [<strong>Contacts</strong>](system-contactmanager-contacts.md) collection. This collection is a member of <strong>System.ContactManager</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Each [**System.Contact**](system-contact.md) in the [**Contacts**](system-contactmanager-contacts.md) collection corresponds to a Windows Mail (formerly Outlook Express) .contact file that Windows creates for each individual Windows Contacts entry.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





