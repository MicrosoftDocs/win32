---
title: DMessengerEvents OnContactAddedToGroup event
description: Indicates that a contact has been added to a group.
ms.assetid: 008e3003-81c1-48de-816b-7e58886497db
keywords:
- OnContactAddedToGroup event Windows Messenger
- OnContactAddedToGroup event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnContactAddedToGroup event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactAddedToGroup
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

# DMessengerEvents::OnContactAddedToGroup event

\[**OnContactAddedToGroup** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a contact has been added to a group.

## Syntax


```C++
void OnContactAddedToGroup(
  [in] LONG      hr,
  [in] IDispatch *pMGroup,
  [in] IDispatch *pMContact
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. For a table of the MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

Possible values are as follows:



| Value                                                                                                                                                             | Meaning                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                            | A user was successfully blocked or unblocked. <br/>  |
| <dl> <dt></dt> <dt>MSGR\_E\_USER\_NOT\_FOUND</dt> </dl>        | The user specified to be added does not exist. <br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_GROUP\_DOES\_NOT\_EXIST</dt> </dl> | The group specified could not be found. <br/>        |



 

</dd> <dt>*pMGroup* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerGroup**](im-messengergroup.md) object indicating the group to which the contact was added. Using this pointer, clients can now code to its [**IMessengerGroup**](im-imessengergroup.md) interface. |
| **VB**  | A [**MessengerGroup**](im-messengergroup.md) object corresponding to the group to which the contact was added.                                                                                                                                                                                  |

 </dd> <dt>*pMContact* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                   |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object indicating the added contact. Using this pointer, clients can now code to its [**IMessengerContact**](im-imessengercontact.md) interface. |
| **VB**  | A [**MessengerContact**](im-messengercontact.md) object corresponding to the added contact.                                                                                                                                                                                      |

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

[**AddContact**](im-imessengergroup-addcontact.md)
</dt> </dl>

 

 





