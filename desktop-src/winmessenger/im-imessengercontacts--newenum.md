---
title: IMessengerContacts \_NewEnum property
description: Enumerates the MessengerContact objects in a collection.
ms.assetid: 236ecb35-b13d-4ab6-a406-027de59bde30
keywords:
- _NewEnum property Windows Messenger
- _NewEnum property Windows Messenger , IMessengerContacts interface
- IMessengerContacts interface Windows Messenger , _NewEnum property
topic_type:
- apiref
api_name:
- IMessengerContacts._NewEnum
- IMessengerContacts.get__NewEnum
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

# IMessengerContacts::\_NewEnum property

\[**\_NewEnum** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Enumerates the [**MessengerContact**](im-messengercontact.md) objects in a collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out, retval] IUnknown **ppUnknown
);
```



## Property value

Return value. Address of a pointer to the IUnknown interface on the copy.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                       |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *ppUnknown* is a **NULL** pointer.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Failed during copy. <br/>               |



## Remarks

**\_NewEnum** returns a copy of the current collection object. It is a standard method in any collection object. This avoids problems if multiple users are accessing the same remote object and assures that objects in the collections will not change during a traverse of the list.

If this method is called while the client is offline, the returned object is a working copy from an object perspective. However, if the copy is obtained while the client is offline, the contact list will always have zero members and zero count. This should be avoided.

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



## See also

<dl> <dt>

[**IMessengerContacts**](im-imessengercontacts.md)
</dt> </dl>

 

 





