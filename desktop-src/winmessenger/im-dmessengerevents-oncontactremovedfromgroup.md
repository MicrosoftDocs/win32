---
title: DMessengerEvents OnContactRemovedFromGroup event
description: Indicates that a contact has been removed from a group.
ms.assetid: '46c78edc-b6bf-4192-9c39-042a09b8b125'
keywords: ["OnContactRemovedFromGroup event Windows Messenger", "OnContactRemovedFromGroup event Windows Messenger , DMessengerEvents interface", "DMessengerEvents interface Windows Messenger , OnContactRemovedFromGroup event"]
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactRemovedFromGroup
api_location:
- Msgsc.dll
api_type:
- COM
---

# DMessengerEvents::OnContactRemovedFromGroup event

\[**OnContactRemovedFromGroup** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a contact has been removed from a group.

## Syntax


```C++
void OnContactRemovedFromGroup(
  [in] LONG         hr,
  [in] IDispatch    *pMGroup,
  [in] VARIANT_BOOL pMContact
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. Possible values are as follows:



| Value                                                                                                                                                              | Meaning                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                             | A user was successfully removed from the group. <br/>                |
| <dl> <dt></dt> <dt>MSGR\_E\_USER\_NOT\_FOUND</dt> </dl>         | The user specified to be removed does not exist. <br/>               |
| <dl> <dt></dt> <dt>MSGR\_E\_USER\_NOT\_GROUP\_MEMBER</dt> </dl> | The user specified to be removed does not belong to the group. <br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_GROUP\_DOES\_NOT\_EXIST</dt> </dl>  | The group specified could not be found. <br/>                        |



 

</dd> <dt>*pMGroup* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                               |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerGroup**](im-messengergroup.md) object that corresponds to the group from which the contact was removed. Using this pointer, clients can now code to its [**IMessengerGroup**](im-imessengergroup.md) interface. |
| **VB**  | A [**MessengerGroup**](im-messengergroup.md) object that corresponds to the group from which the contact was removed.                                                                                                                                                                                        |

 </dd> <dt>*pMContact* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                       |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object that corresponds to the group from which the contact was removed. Using this pointer, clients can now code to its [**IMessengerContact**](im-imessengercontact.md) interface. |
| **VB**  | A [**MessengerContact**](im-messengercontact.md) object that corresponds to the group from which the contact was removed.                                                                                                                                                                                            |

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| pMContact | 0           | VT\_DISPATCH |
| pMGroup   | 1           | VT\_DISPATCH |
| hr        | 2           | VT\_I4       |



 

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



 

 





