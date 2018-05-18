---
title: System.Contact.POBox property
description: Gets the post office box number associated with the contact.
ms.assetid: 'de2cad67-a27e-4cb9-b060-a27971f0a541'
keywords: ["POBox property Windows Sidebar", "POBox property Windows Sidebar , System.Contact object", "System.Contact object Windows Sidebar , POBox property"]
topic_type:
- apiref
api_name:
- System.Contact.POBox
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Contact.POBox property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the post office box number associated with the contact.

This property is read-only.

## Syntax


```JScript
strPOBox = System.Contact.POBox
```



## Property value

A **String** that receives the post office box number.

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
    var sSearchResult = oContact.item(i).POBox;
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

 

 





