---
title: Contacts.item property
description: Gets a System.Contact from the Contacts collection.
ms.assetid: 760d6507-dff2-47c8-bdbe-6e251be12820
keywords:
- item property Windows Sidebar
- item property Windows Sidebar , Contacts collection
- Contacts collection Windows Sidebar , item property
topic_type:
- apiref
api_name:
- Contacts.item
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

# Contacts.item property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.Contact**](system-contact.md) from the [**Contacts**](system-contactmanager-contacts.md) collection.

This property is read-only.

## Syntax


```JScript
objitem = Contacts.item
```



## Property value

An **Object** that receives a [**System.Contact**](system-contact.md) at the specified index.

## Examples

The following example demonstrates how to access a contact in the [**Contacts**](system-contactmanager-contacts.md) collection and get a specific property for that contact.


```JScript
// Instantiate a Contacts object to search.
oContact = System.ContactManager.Contacts;

// Iterate through all contacts.
for (var i = 0; i < oContact.count; i++)
{
    var sSearchResult = oContact.item(i).defaultEmail;
    // Add search result to main display string.
    sOutput += sSearchResult;
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

[**System.Contact**](system-contact.md)
</dt> <dt>

[**Contacts**](system-contactmanager-contacts.md)
</dt> <dt>

[**count**](system-contactmanager-contacts-count.md)
</dt> </dl>

 

 





