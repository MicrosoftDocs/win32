---
title: IMessenger2 MyGroups property
description: Retrieves the Group list contained in the Messenger object. The retrieved list is a MessengerGroups collection object that can be manipulated with the IMessengerGroups interface.
ms.assetid: 3b556931-8f5f-4a79-81b7-572f721d3cc1
keywords:
- MyGroups property Windows Messenger
- MyGroups property Windows Messenger , IMessenger2 interface
- IMessenger2 interface Windows Messenger , MyGroups property
topic_type:
- apiref
api_name:
- IMessenger2.MyGroups
- IMessenger2.get_MyGroups
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

# IMessenger2::MyGroups property

\[**MyGroups** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the Group list contained in the [**Messenger**](im-messenger.md) object. The retrieved list is a [**MessengerGroups**](im-messengergroups.md) collection object that can be manipulated with the [**IMessengerGroups**](im-imessengergroups.md) interface.

This property is read-only.

## Syntax


```C++
HRESULT get_MyGroups(
  [out, retval] IDispatch **ppMGroups
);
```



## Property value

Return value. Pointer to a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface. In practice, this returns the [**IMessengerGroups**](im-imessengergroups.md) interface on the Contact List or [**MessengerGroups**](im-messengergroups.md) collection object.

## Error codes

Returns one of the following values.



| Name                                                                                                     | Meaning                                                  |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                         | Success.<br/>                                      |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>                | Error during list creation.<br/>                   |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl>    | *ppMGroups* is a **NULL** pointer. <br/>           |
| <dl> <dt>MSGR\_E\_GROUPS\_NOT\_ENABLED</dt> </dl> | The current service does not support groups. <br/> |



## Remarks

Some services, such as Microsoft Exchange Instant Messaging Service (IM), do not support groups. The use of this property on these services will return the error **MSGR\_E\_GROUPS\_NOT\_ENABLED**.

*ppMGroups* should be released when it is no longer needed. Retrieved lists can potentially have zero members in their collection.

If this property is called while the client is not signed in, the HRESULT will be S\_OK and a true object will be returned. However, the resulting [**MessengerGroups**](im-messengergroups.md) collection object will have zero members (that is, it contains no valid **MessengerGroups** objects).

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

[**IMessenger2**](im-imessenger2.md)
</dt> <dt>

[**IMessengerGroups**](im-imessengergroups.md)
</dt> </dl>

 

 





