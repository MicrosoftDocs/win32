---
title: System.Contact.postalCode property
description: Gets the postal code associated with the contact.
ms.assetid: '3f44ad7f-55c6-4a13-a5be-99205ede5cc4'
keywords: ["postalCode property Windows Sidebar", "postalCode property Windows Sidebar , System.Contact object", "System.Contact object Windows Sidebar , postalCode property"]
topic_type:
- apiref
api_name:
- System.Contact.postalCode
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Contact.postalCode property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the postal code associated with the contact.

This property is read-only.

## Syntax


```JScript
strpostalCode = System.Contact.postalCode
```



## Property value

A **String** that receives the postal code.

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
    var sSearchResult = oContact.item(i).postalCode;
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

**Reference**
</dt> <dt>

[**System.Contact**](system-contact.md)
</dt> <dt>

[**System.ContactManager**](system-contactmanager.md)
</dt> </dl>

 

 





