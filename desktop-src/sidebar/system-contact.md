---
title: System.Contact object
description: Defines the properties and methods of each member of the Contacts collection.
ms.assetid: 63c9ebc0-589b-4180-a14a-4e5a2fcfad3b
keywords:
- System.Contact object Windows Sidebar
- System.Contact object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Contact
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

# System.Contact object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and methods of each member of the [**Contacts**](system-contactmanager-contacts.md) collection.

## Members

The **System.Contact** object has these types of members:

-   [Properties](#properties)

### Properties

The **System.Contact** object has these properties.



| Property                                                       | Access type          | Description                                                              |
|:---------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------|
| [**city**](system-contact-city.md)<br/>                 | Read-only<br/> | Gets the city name associated with the contact. <br/>              |
| [**country**](system-contact-country.md)<br/>           | Read-only<br/> | Gets the country name associated with the contact. <br/>           |
| [**defaultEmail**](system-contact-defaultemail.md)<br/> | Read-only<br/> | Gets the default email address associated with the contact. <br/>  |
| [**filePath**](system-contact-filepath.md)<br/>         | Read-only<br/> | Gets the file path for the contact. <br/>                          |
| [**homePhone**](system-contact-homephone.md)<br/>       | Read-only<br/> | Gets the home phone number associated with the contact. <br/>      |
| [**mobilePhone**](system-contact-mobilephone.md)<br/>   | Read-only<br/> | Gets the mobile phone number associated with the contact. <br/>    |
| [**name**](system-contact-name.md)<br/>                 | Read-only<br/> | Gets the full name associated with the contact. <br/>              |
| [**POBox**](system-contact-pobox.md)<br/>               | Read-only<br/> | Gets the post office box number associated with the contact. <br/> |
| [**postalCode**](system-contact-postalcode.md)<br/>     | Read-only<br/> | Gets the postal code associated with the contact. <br/>            |
| [**state**](system-contact-state.md)<br/>               | Read-only<br/> | Gets the state (or equivalent) associated with the contact. <br/>  |
| [**street**](system-contact-street.md)<br/>             | Read-only<br/> | Gets the street address associated with the contact. <br/>         |
| [**workPhone**](system-contact-workphone.md)<br/>       | Read-only<br/> | Gets the work phone number associated with the contact. <br/>      |



 

## Remarks

Each **System.Contact** corresponds to a Windows Mail (formerly Outlook Express) .contact file that Windows creates for each individual Windows Contacts entry.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





