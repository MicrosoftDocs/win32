---
title: DMessengerEvents OnContactPagerChange event
description: Indicates that a contact in the local client's Contact List has changed the pager information access permissions.
ms.assetid: '86f97c26-3936-4160-aaae-cfb87e7e072e'
keywords: ["OnContactPagerChange event Windows Messenger", "OnContactPagerChange event Windows Messenger , DMessengerEvents interface", "DMessengerEvents interface Windows Messenger , OnContactPagerChange event"]
topic_type:
- apiref
api_name:
- DMessengerEvents.OnContactPagerChange
api_location:
- Msgsc.dll
api_type:
- COM
---

# DMessengerEvents::OnContactPagerChange event

\[**OnContactPagerChange** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a contact in the local client's Contact List has changed the pager information access permissions.

## Syntax


```C++
void OnContactPagerChange(
  [in] LONG         hr,
  [in] IDispatch    *pContact,
  [in] VARIANT_BOOL pBoolBlock
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

Pointer to a [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the [**MessengerContact**](im-messengercontact.md) object where a change in block value was attempted.

</dd> <dt>

*pBoolBlock* \[in\]
</dt> <dd>

One of two possible values of the VARIANT\_BOOL constant enumeration defined by the COM. This value is potentially **NULL** or otherwise not useful if *hr* in the event returned any error code.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

To use this event in Windows Messenger, you must install an add-in component that supports paging.

This event returns only that the allowed or disallowed state of the information has changed. Only the allow-access flag is stored by the Microsoft .NET Messenger Service. The mobile information itself is stored on servers that are not directly under the control of Windows Messenger. The mobile device or pager information query is not performed through Windows Messenger APIs.

To be used when writing custom ::Invoke methods to handle these events.



| Parameter | vaArgs\[x\] | Variant Type |
|-----------|-------------|--------------|
| pBoolPage | 0           | VT\_BOOL     |
| pContact  | 1           | VT\_DISPATCH |
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



 

 





