---
title: Contacts.count property
description: Gets the number of System.Contact items in the Contacts collection.
ms.assetid: 'c0b79861-7048-44a1-9bed-3f3a5389e82e'
keywords: ["count property Windows Sidebar", "count property Windows Sidebar , Contacts collection", "Contacts collection Windows Sidebar , count property"]
topic_type:
- apiref
api_name:
- Contacts.count
api_location:
- Sidebar.Exe
api_type:
- COM
---

# Contacts.count property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of [**System.Contact**](system-contact.md) items in the [**Contacts**](system-contactmanager-contacts.md) collection.

This property is read-only.

## Syntax


```JScript
icount = Contacts.count
```



## Property value

An **Integer** that receives the number of items.

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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**Contacts**](system-contactmanager-contacts.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**System.Contact**](system-contact.md)
</dt> <dt>

[**item**](system-contactmanager-contacts-item.md)
</dt> </dl>

 

 





