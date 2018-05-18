---
title: DMessengerEvents OnGroupNameChanged event
description: Indicates that the name of a group has been changed.
ms.assetid: 'b63f8cad-5392-41f3-8c13-86456ec2aadf'
keywords: ["OnGroupNameChanged event Windows Messenger", "OnGroupNameChanged event Windows Messenger , DMessengerEvents interface", "DMessengerEvents interface Windows Messenger , OnGroupNameChanged event"]
topic_type:
- apiref
api_name:
- DMessengerEvents.OnGroupNameChanged
api_location:
- Msgsc.dll
api_type:
- COM
---

# DMessengerEvents::OnGroupNameChanged event

\[**OnGroupNameChanged** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the name of a group has been changed.

## Syntax


```C++
void OnGroupNameChanged(
  [in] LONG      hr,
  [in] IDispatch *pMGroup
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. Possible values are as follows:



| Value                                                                                                                                                            | Meaning                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                           | A group name was successfully changed. <br/>           |
| <dl> <dt></dt> <dt>MSGR\_E\_GROUP\_NAME\_TOO\_LONG</dt> </dl> | The name of the group to be changed is too long. <br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_BAD\_GROUP\_NAME</dt> </dl>       | The name of the group to be changed is invalid. <br/>  |



 

</dd> <dt>*pMGroup* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                              |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerGroup**](im-messengergroup.md) object that corresponds to the group from wich the contact was removed. Using this pointer, clients can now code to its [**IMessengerGroup**](im-imessengergroup.md) interface. |
| **VB**  | A [**MessengerGroup**](im-messengergroup.md) object that corresponds to the group from wich the contact was removed.                                                                                                                                                                                        |

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| pMGroup   | 0           | VT\_DISPATCH |
| hr        | 1           | VT\_I4       |



 

The **OnGroupNameChanged** event is scriptable.

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



 

 





