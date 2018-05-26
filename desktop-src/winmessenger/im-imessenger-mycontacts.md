---
title: IMessenger MyContacts property
description: Retrieves the contact list contained in the client or Messenger object. The retrieved list is a MessengerContacts collection object that can be manipulated with the IMessengerContacts interface.
ms.assetid: 675561a5-63f8-4db9-8459-f31266ee928c
keywords:
- MyContacts property Windows Messenger
- MyContacts property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , MyContacts property
topic_type:
- apiref
api_name:
- IMessenger.MyContacts
- IMessenger.get_MyContacts
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessenger::MyContacts property

\[**MyContacts** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the contact list contained in the client or [**Messenger**](im-messenger.md) object. The retrieved list is a [**MessengerContacts**](im-messengercontacts.md) collection object that can be manipulated with the [**IMessengerContacts**](im-imessengercontacts.md) interface.

This property is read-only.

## Syntax


```C++
HRESULT get_MyContacts(
  [out, retval] IDispatch **ppMContacts
);
```



## Property value

Return value. Pointer to a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface. Returns the [**IMessengerContacts**](im-imessengercontacts.md) interface on the contact list or [**MessengerContacts**](im-messengercontacts.md) collection object.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                          |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. See Remarks.<br/>                 |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *ppMContacts* is a **NULL** pointer. <br/> |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Error during list creation.<br/>           |



## Remarks

*ppMContacts* should be released when it is no longer needed. Retrieved lists can potentially have zero members in their collection. If multiple services are enabled, this method combines the lists of several services.

If this method is called while the client is not signed in, S\_OK will still be the HRESULT and a true object will be returned. However, the resulting [**MessengerContacts**](im-messengercontacts.md)collection object will have zero members.

> [!Note]  
> This property is available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





