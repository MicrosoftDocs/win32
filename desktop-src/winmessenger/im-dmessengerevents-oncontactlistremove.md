---
title: DMessengerEvents OnContactListRemove event
description: Indicates the result of an attempt to remove a contact from the Messenger object's Contact List.
ms.assetid: 4ee09b71-8f16-44d9-a2cf-78196d1b6c4c
keywords:
- OnContactListRemove event Windows Messenger
- OnContactListRemove event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnContactListRemove event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactListRemove
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

# DMessengerEvents::OnContactListRemove event

\[**OnContactListRemove** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates the result of an attempt to remove a contact from the [**Messenger**](im-messenger.md) object's Contact List.

## Syntax


```C++
void OnContactListRemove(
  [in] LONG      hr,
  [in] IDispatch *pMContact
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**.

An error result for *hr* might result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters. For a table of MSGR\_E\* constants, see [**MSGRConstants**](im-msgrconstants.md).

Possible values are as follows:



| Value                                                                                                                                                         | Meaning                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                        | A user was successfully removed from the Contact List. <br/>                  |
| <dl> <dt></dt> <dt>MSGR\_E\_USER\_NOT\_FOUND</dt> </dl>    | The contact specified to be removed was not found in the Contact List. <br/>  |
| <dl> <dt></dt> <dt>MSGR\_E\_UNEXPECTED</dt> </dl>          | The server has returned an unexpected error code. <br/>                       |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_TOO\_BUSY</dt> </dl>   | The server is not processing requests or not accepting new connections. <br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_UNAVAILABLE</dt> </dl> | The server was contacted, but was unavailable for unspecified reasons. <br/>  |



 

</dd> <dt>*pMContact* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                              |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object that corresponds to the removed contact. Using this pointer, clients can now code to its [**IMessengerContact**](im-imessengercontact.md) interface. |
| **VB**  | A [**MessengerContact**](im-messengercontact.md) object that corresponds to the removed contact.                                                                                                                                                                                            |

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event comes in response to the [**Remove**](im-imessengercontacts-remove.md) method. If **Remove** did not return S\_OK, no notification is received. For example, attempting to remove a user without specifying a string for username is prevented by the **Remove** method, which returns E\_FAIL even before submission to the protocol and generates no event.

The Microsoft .NET Messenger Service always submits remove requests to the server and does not check local lists first. Other services may check local lists first and issue this event locally without submitting to the protocol for some of the error cases.

Removing a [**MessengerContact**](im-messengercontact.md) object from the Contact List does not release it from memory or otherwise deallocate it. Clients can deallocate the **MessengerContact** object as soon as it is removed from the Contact List or later after the client has shut down. A **MessengerContact** object that is not in the Contact List is still a valid object (for example, it could be used as the VARIANT argument in a [**InstantMessage**](im-imessenger-instantmessage.md) call). After the object or contact is out of the Contact List, no status updates will be received from the server about this contact. As a result, when launching an instant message as described, the client will not be able to determine whether that contact is online until the message is sent.

This event is also issued whenever an attempt is made to remove a contact from the Contact List through user action in the UI or through other internal method calls.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| pMContact | 0           | VT\_DISPATCH |
| hr        | 1           | VT\_I4       |



 

> [!Note]  
> This event is available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





