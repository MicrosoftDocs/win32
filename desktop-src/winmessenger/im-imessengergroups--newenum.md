---
title: IMessengerGroups \_NewEnum property
description: Enumerates the MessengerGroup objects in a collection.
ms.assetid: e07cedb7-9d76-4a93-bdae-bb28df661695
keywords:
- _NewEnum property Windows Messenger
- _NewEnum property Windows Messenger , IMessengerGroups interface
- IMessengerGroups interface Windows Messenger , _NewEnum property
topic_type:
- apiref
api_name:
- IMessengerGroups._NewEnum
- IMessengerGroups.get__NewEnum
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

# IMessengerGroups::\_NewEnum property

\[**\_NewEnum** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Enumerates the [**MessengerGroup**](im-messengergroup.md) objects in a collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out, retval] IUnknown **ppUnknown
);
```



## Property value

Return value. Pointer to a pointer to the IUnknown interface on the copy.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                       |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *ppUnknown* is a **NULL** pointer.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Failed during copy. <br/>               |



## Remarks

**\_NewEnum** returns a copy of the current collection object. It is a standard method in any collection object. This avoids problems if multiple users are accessing the same remote object and assures that objects in the collections will not change during a traverse of the list.

If this method is called while the client is offline, the returned object is a working copy from an object perspective. However, if the copy is obtained while the client is offline, the Contact List will always have zero members and zero count. This should be avoided.

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

[**IMessengerGroups**](im-imessengergroups.md)
</dt> </dl>

 

 





