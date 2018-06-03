---
title: DMessengerEvents OnGroupAdded event
description: Indicates that a new group has been created.
ms.assetid: 9c0847d4-b315-459d-9226-34f8165b3f79
keywords:
- OnGroupAdded event Windows Messenger
- OnGroupAdded event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnGroupAdded event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnGroupAdded
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

# DMessengerEvents::OnGroupAdded event

\[**OnGroupAdded** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a new group has been created.

## Syntax


```C++
void OnGroupAdded(
  [in] LONG      hr,
  [in] IDispatch *pMGroup
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**. Possible values are as follows:



| Value                                                                                                                                                            | Meaning                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt></dt> <dt>S\_OK</dt> </dl>                           | A group was successfully added. <br/>                   |
| <dl> <dt></dt> <dt>MSGR\_E\_GROUP\_ALREDY\_EXISTS</dt> </dl>  | The name of the group to be added already exists. <br/> |
| <dl> <dt></dt> <dt>MSGR\_E\_GROUP\_NAME\_TOO\_LONG</dt> </dl> | The name of the group to be added is too long. <br/>    |
| <dl> <dt></dt> <dt>MSGR\_E\_BAD\_GROUP\_NAME</dt> </dl>       | The name of the group to be added is invalid. <br/>     |



 

</dd> <dt>*pMGroup* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                               |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Pointer to a [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerGroup**](im-messengergroup.md) object that corresponds to the group from which the contact was removed. Using this pointer, clients can now code to its [**IMessengerGroup**](im-imessengergroup.md) interface. |
| **VB**  | A [**MessengerGroup**](im-messengergroup.md) object that corresponds to the group from wich the contact was removed.                                                                                                                                                                                         |

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| pMGroup   | 0           | VT\_DISPATCH |
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



## See also

<dl> <dt>

[**DMessengerEvents**](im-dmessengerevents.md)
</dt> <dt>

[**CreateGroup**](im-imessenger2-creategroup.md)
</dt> </dl>

 

 





