---
title: DMessengerEvents OnMyFriendlyNameChange event
description: Indicates that the local clients friendly name has been changed or that a change was attempted.
ms.assetid: f51c9bc2-12c4-4e81-9d74-9eddf72e2b0d
keywords:
- OnMyFriendlyNameChange event Windows Messenger
- OnMyFriendlyNameChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnMyFriendlyNameChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnMyFriendlyNameChange
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

# DMessengerEvents::OnMyFriendlyNameChange event

\[**OnMyFriendlyNameChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that the local client's friendly name has been changed or that a change was attempted.

## Syntax


```C++
void OnMyFriendlyNameChange(
  [in] LONG hr,
  [in] BSTR bstrPrevFriendlyName
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as **LONG**. S\_OK is the only result returned currently.

</dd> <dt>

*bstrPrevFriendlyName* \[in\]
</dt> <dd>

A **BSTR** that contains the current client user's previous friendly name.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The Windows Messenger API does not have a method to put or set the client's friendly name information. This event fires only if the friendly name is changed through internal APIs or user action on the UI.

After receiving this event, the following call should be issued immediately to get the new friendly name of the current client user.

``` syntax
pOMessengerObject->get_FriendlyName
```

The previous friendly name might be permanently lost if it were not returned in the events. It can be used to check the client UI to be sure it is removed.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter            | vaArgs\[x\] | Variant Type |
|----------------------|-------------|--------------|
| bstrPrevFriendlyName | 0           | VT\_BSTR     |
| hr                   | 1           | VT\_14       |



 

> [!Note]  
> This event is not available for scripting languages.

 

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

[**FriendlyName**](im-imessengercontact-friendlyname.md)
</dt> <dt>

[**OnContactFriendlyNameChange**](im-dmessengerevents-oncontactfriendlynamechange.md)
</dt> </dl>

 

 





