---
title: DMessengerEvents OnMyPropertyChange event
description: Indicates that an uncategorized element of the local clients property information has been changed or that a change was attempted.
ms.assetid: 68b44749-c8ad-4366-9a3d-f25f022741d3
keywords:
- OnMyPropertyChange event Windows Messenger
- OnMyPropertyChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnMyPropertyChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnMyPropertyChange
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

# DMessengerEvents::OnMyPropertyChange event

\[**OnMyPropertyChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that an uncategorized element of the local client's property information has been changed or that a change was attempted.

## Syntax


```C++
void OnMyPropertyChange(
  [in] LONG             hr,
  [in] MCONTACTPROPERTY ePropType,
  [in] VARIANT          vPropVal
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**.

**Note**   An error result for *hr* might result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.

</dd> <dt>

*ePropType* \[in\]
</dt> <dd>

A value in the [**MCONTACTPROPERTY**](im-mcontactproperty.md) enumeration.

</dd> <dt>

*vPropVal* \[in\]
</dt> <dd>

A **VARIANT** that contains the current client user's new property information.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The Windows Messenger API does not have a method to put or set the client's property information. This event fires only if the friendly name is changed through internal APIs or user action on the UI. To get the current client user properties, establish a [**MessengerContact**](im-messengercontact.md) object that corresponds to the current client user and call [**Property**](im-imessengercontact-property.md) on that object.

This method exists primarily for as yet undefined properties. The current properties (**Phone** and **FriendlyName** ) have **get\_** methods for accessing the property in the **Messenger** object and their own specific change events.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| vPropVal  | 0           | VT\_BSTR     |
| ePropType | 1           | VT\_14       |
| hr        | 2           | VT\_14       |



 

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

[**OnContactPropertyChange**](im-dmessengerevents-oncontactpropertychange.md)
</dt> <dt>

[**MyPhoneNumber**](im-imessenger-myphonenumber.md)
</dt> </dl>

 

 





