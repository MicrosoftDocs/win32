---
title: DMessengerEvents OnContactPropertyChange event
description: Indicates that property information for a contact in the local clients Contact List has changed.
ms.assetid: ef9328ee-53ff-4f8b-a9ab-174a4485229e
keywords:
- OnContactPropertyChange event Windows Messenger
- OnContactPropertyChange event Windows Messenger , DMessengerEvents interface
- DMessengerEvents interface Windows Messenger , OnContactPropertyChange event
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactPropertyChange
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

# DMessengerEvents::OnContactPropertyChange event

\[**OnContactPropertyChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that property information for a contact in the local client's Contact List has changed.

## Syntax


```C++
void OnContactPropertyChange(
  [in] LONG             hr,
  [in] IDispatch        *pContact,
  [in] MCONTACTPROPERTY ePropType,
  [in] VARIANT          vPropVal
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **LONG**.

An error result for *hr* might result in all other event parameters being meaningless, **NULL**, or otherwise invalid. Always check for a successful *hr* before attempting to use the other event parameters.

</dd> <dt>

*pContact* \[in\]
</dt> <dd>

Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object that corresponds to the contact. Using this pointer, clients can now code to its [**IMessengerContact**](im-imessengercontact.md) interface.

A [**MessengerContact**](im-messengercontact.md) object that corresponds to the contact. </dd> <dt>

*ePropType* \[in\]
</dt> <dd>

A value in the [**MCONTACTPROPERTY**](im-mcontactproperty.md) enumeration.

</dd> <dt>*vPropVal* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                     |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | A **VARIANT** intended to transmit the value of future properties. Type checking will depend on the property, but should only be assumed to be a **VARIANT**. Clients should check the VT\_ value of the results and perform coercions, if desired. |
| **VB**  | A **VARIANT** intended to transmit the value of future properties. Type checking will depend on the property, but should only be assumed to be a **VARIANT**.                                                                                       |

 </dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event exists for later expansions of properties that can be associated with a contact but that will not require another iteration of the Windows Messenger interfaces. The current properties (**CanPage**, **Phone**, **FriendlyName**, **Blocked**) have their own **get\_** methods and specific change events. By the current definition of the [**MCONTACTPROPERTY**](im-mcontactproperty.md) enumeration, there are no additional properties.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type      |
|-----------|-------------|-------------------|
| vPropVal  | 0           | (Unknown VARIANT) |
| ePropType | 1           | VT\_I4            |
| pContact  | 2           | VT\_DISPATCH      |
| hr        | 3           | VT\_I4            |



 

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

[**Property**](im-imessengercontact-property.md)
</dt> <dt>

[**OnContactPhoneChange**](im-dmessengerevents-oncontactphonechange.md)
</dt> <dt>

[**OnContactPagerChange**](im-dmessengerevents-oncontactpagerchange.md)
</dt> <dt>

[**OnContactFriendlyNameChange**](im-dmessengerevents-oncontactfriendlynamechange.md)
</dt> <dt>

[**OnContactBlockChange**](im-dmessengerevents-oncontactblockchange.md)
</dt> </dl>

 

 





