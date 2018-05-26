---
title: System.Contact.mobilePhone property
description: Gets the mobile phone number associated with the contact.
ms.assetid: 8651b6eb-8c83-47d0-bd42-b76c67174695
keywords:
- mobilePhone property Windows Sidebar
- mobilePhone property Windows Sidebar , System.Contact object
- System.Contact object Windows Sidebar , mobilePhone property
topic_type:
- apiref
api_name:
- System.Contact.mobilePhone
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

# System.Contact.mobilePhone property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the mobile phone number associated with the contact.

This property is read-only.

## Syntax


```JScript
strmobilePhone = System.Contact.mobilePhone
```



## Property value

A **String** that receives the mobile phone number.

## Remarks

Individual contacts are accessible through the [**Contacts**](system-contactmanager-contacts.md) collection of [**System.ContactManager**](system-contactmanager.md).

## Examples

The following example demonstrates how to access a contact in the [**Contacts**](system-contactmanager-contacts.md) collection and get a specific property for that contact.


```JScript
// Instantiate a Contacts object to search.
oContact = System.ContactManager.Contacts;

// Iterate through all contacts.
for (var i = 0; i < oContact.count; i++)
{
    var sSearchResult = oContact.item(i).mobilePhone;
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

[**System.ContactManager**](system-contactmanager.md)
</dt> </dl>

 

 





