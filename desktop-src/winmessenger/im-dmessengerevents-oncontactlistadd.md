---
title: DMessengerEvents OnContactListAdd event
description: Indicates the result of an attempt to add to the Messenger object's Contact List.
ms.assetid: '93961ca7-da55-445c-bf9e-c88958882f82'
keywords: ["OnContactListAdd event Windows Messenger", "OnContactListAdd event Windows Messenger , DMessengerEvents interface", "DMessengerEvents interface Windows Messenger , OnContactListAdd event"]
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactListAdd
api_location:
- Msgsc.dll
api_type:
- COM
---

# DMessengerEvents::OnContactListAdd event

\[**OnContactListAdd** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates the result of an attempt to add to the [**Messenger**](im-messenger.md) object's Contact List.

## Syntax


```C++
void OnContactListAdd(
  [in] LONG      hr,
  [in] IDispatch *pMContact
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. For a table of the MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

An error result for *hr* might result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.



| Value                                                                                                                                                         | Meaning                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                        | A contact was successfully added. <br/>                                                                          |
| <dl> <dt></dt> <dt>MSGR\_E\_LIST\_FULL</dt> </dl>          | The server has determined that the Contact List is already at capacity. This is a server-determined limit. <br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_ALREADY\_IN\_LIST</dt> </dl>   | The server has determined that the user to be added is already in the Contact List. <br/>                        |
| <dl> <dt></dt> <dt>MSGR\_E\_USER\_NOT\_FOUND</dt> </dl>    | The user specified to be added does not exist. <br/>                                                             |
| <dl> <dt></dt> <dt>MSGR\_E\_UNEXPECTED</dt> </dl>          | The server has returned an unexpected error code. <br/>                                                          |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_TOO\_BUSY</dt> </dl>   | The server is not processing requests or not accepting new connections. <br/>                                    |
| <dl> <dt></dt> <dt>MSGR\_E\_SERVER\_UNAVAILABLE</dt> </dl> | The server was able to be contacted, but was unavailable for unspecified reasons. <br/>                          |
| <dl> <dt></dt> <dt>E\_INVALIDARG</dt> </dl>                | An invalid value was passed into the *pMContact* parameter. <br/>                                                |



 

</dd> <dt>*pMContact* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object where a change in block value was attempted. |
| **VB**  | A [**MessengerContact**](im-messengercontact.md) object where a change in block values was attempted.                                                                              |

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event comes in response to a specific user action through the client UI. There is no API for adding a contact to the Contact List.

If you attempt to add a user who is already in a list, you will receive **MSGR\_E\_ALREADY\_IN\_LIST** in response. There is no initial check of client-side lists for the Microsoft .NET Messenger Service before submission as a protocol, although it is possible that other services might implement a client-side check that would issue an event locally in this situation and submit no protocol message for some of the error cases.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| pMContact | 0           | VT\_DISPATCH |
| pMGroup   | 1           | VT\_DISPATCH |
| hr        | 2           | VT\_I4       |



 

The same DISPID is defined on [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md), and so the event also occurs on the [**MessengerPriv**](im-messengerpriv-object.md) object.

> [!Note]  
> This event is available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**DMessengerEvents**](im-dmessengerevents.md)
</dt> <dt>

[**OnContactListRemove**](im-dmessengerevents-oncontactlistremove.md)
</dt> </dl>

 

 





