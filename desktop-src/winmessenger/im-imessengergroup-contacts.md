---
title: IMessengerGroup Contacts property
description: Retrieves a list of contacts from the group's collection of users.
ms.assetid: 7a0605ea-5f8c-4130-a017-174cc478dba0
keywords:
- Contacts property Windows Messenger
- Contacts property Windows Messenger , IMessengerGroup interface
- IMessengerGroup interface Windows Messenger , Contacts property
topic_type:
- apiref
api_name:
- IMessengerGroup.Contacts
- IMessengerGroup.get_Contacts
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMessengerGroup::Contacts property

\[**Contacts** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a list of contacts from the group's collection of users.

This property is read-only.

## Syntax


```C++
HRESULT get_Contacts(
  [out, retval] IDispatch **ppMContacts
);
```



## Property value

Address of a pointer to an [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) of a [**MessengerContact**](im-messengercontact.md) object representing the users that are in the group's collection.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                         |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success.<br/>                             |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *ppMContacts* is a **NULL** pointer.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Error during list creation.<br/>          |



## Remarks

The following table lists the error codes returned by this property.



| Error Code | Meaning                     |
|------------|-----------------------------|
| 0x8007000E | Error during list creation. |



 

This property is available for scripting languages.

> [!Note]  
> This method is available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessengerGroup**](im-imessengergroup.md)
</dt> </dl>

 

 





