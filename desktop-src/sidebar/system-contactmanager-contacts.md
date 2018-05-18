---
title: System.ContactManager.Contacts property
description: A collection of System.Contact objects.
ms.assetid: '4045adbd-bd41-459c-b6bf-5b11cf4a8e7c'
keywords: ["Contacts property Windows Sidebar", "Contacts property Windows Sidebar , System.ContactManager object", "System.ContactManager object Windows Sidebar , Contacts property"]
topic_type:
- apiref
api_name:
- System.ContactManager.Contacts
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.ContactManager.Contacts property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

A collection of [**System.Contact**](system-contact.md) objects.

> [!Note]  
> Objects of type [**System.Contact**](system-contact.md) can only be accessed through the **Contacts** collection. This collection is a member of [**System.ContactManager**](system-contactmanager.md).

 

This property is read-only.

## Syntax


```JScript
objContacts = System.ContactManager.Contacts
```



## Property value

A collection of [**System.Contact**](system-contact.md) objects.

## Remarks

Each [**System.Contact**](system-contact.md) corresponds to a Windows Mail (formerly Outlook Express) .contact file that Windows creates for each individual Windows Contacts entry.

## Examples

The following example demonstrates how to access a **Contacts** collection from [**System.ContactManager**](system-contactmanager.md), select a single [**Contact**](system-contact.md) from the collection, and retrieve the `city` property of that **Contact**.


```JScript
// collContact is a collection of System.Contact objects.
var collContact = System.ContactManager.Contacts; 

// oContact is a System.Contact object. 
// oContact is item 3 in the collContact collection.
var oContact = collContact.item(3);  

// strContactCity is the value of the city property of oContact.
var strContactCity = oContact.city;
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

[**System.ContactManager**](system-contactmanager.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**count**](system-contactmanager-contacts-count.md)
</dt> <dt>

[**item**](system-contactmanager-contacts-item.md)
</dt> <dt>

[**System.Contact**](system-contact.md)
</dt> </dl>

 

 





