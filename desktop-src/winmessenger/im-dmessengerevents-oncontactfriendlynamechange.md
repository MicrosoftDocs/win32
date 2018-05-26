---
title: DMessengerEvents OnContactFriendlyNameChange event
description: Indicates that a contact in the clients Contact List has changed the friendly name.
ms.assetid: 4b8250af-aff7-4a4c-98c3-b0e352e1570a
keywords:
- OnContactFriendlyNameChange event Windows Messenger
- OnContactFriendlyNameChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnContactFriendlyNameChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactFriendlyNameChange
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

# DMessengerEvents::OnContactFriendlyNameChange event

\[**OnContactFriendlyNameChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a contact in the client's Contact List has changed the friendly name.

## Syntax


```C++
void OnContactFriendlyNameChange(
  [in] LONG      hr,
  [in] IDispatch *pMContact,
  [in] BSTR      bstrPrevFriendlyName
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**.

An error result for *hr* may result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.

</dd> <dt>*pMContact* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                    |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object that corresponds to a contact whose friendly name has changed. Using this pointer, clients can now code to its [**IMessengerContact**](im-imessengercontact.md) interface. |
| **VB**  | A [**MessengerContact**](im-messengercontact.md) object corresponding to a contact whose friendly name has changed.                                                                                                                                                                                               |

 </dd> <dt>

*bstrPrevFriendlyName* \[in\]
</dt> <dd>

A **BSTR** that contains the user's previous friendly name.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

After receiving this event, the following call should be issued immediately to get the new friendly name of the *pMContact* object pointer or contact sent by the event.

``` syntax
pMContact->get_FriendlyName
```

The previous friendly name would be permanently lost if it were not returned in the events. It can be used to qualify the code that might traverse a list or UI in a client to make sure that the old friendly name has been removed.

The friendly name is set by the client that corresponds to the remote contact. If the friendly name was changed while the local client was offline, the event is issued upon sign-in.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter            | vaArgs\[x\] | Variant Type |
|----------------------|-------------|--------------|
| bstrPrevFriendlyName | 0           | VT\_BSTR     |
| pMContact            | 1           | VT\_DISPATCH |
| hr                   | 2           | VT\_I4       |



 

> [!Note]  
> This event is available for scripting languages only in a trusted zone.

 

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



## See also

<dl> <dt>

[**DMessengerEvents**](im-dmessengerevents.md)
</dt> <dt>

[**OnMyFriendlyNameChange**](im-dmessengerevents-onmyfriendlynamechange.md)
</dt> </dl>

 

 





