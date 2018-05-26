---
title: IMessengerPrivate AddContact method
description: Adds a contact to the contact list with no prompting or notification UI.
ms.assetid: 8eb00cba-6a15-4b85-a82c-c45e67eca2bb
keywords:
- AddContact method Windows Messenger
- AddContact method Windows Messenger , IMessengerPrivate interface
- IMessengerPrivate interface Windows Messenger , AddContact method
topic_type:
- apiref
api_name:
- IMessengerPrivate.AddContact
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

# IMessengerPrivate::AddContact method

\[**AddContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Adds a contact to the contact list with no prompting or notification UI.

## Syntax


```C++
HRESULT AddContact(
  [in] BSTR    bstrSiginName,
  [in] VARIANT vService
);
```



## Parameters

<dl> <dt>

*bstrSiginName* \[in\]
</dt> <dd>

**BSTR** that defines the sign-in name of the contact to be added. The method will run regardless of whether this parameter is valid. The [**OnContactListAdd**](im-dmessengerprivateevents-oncontactlistadd.md) event will contain the results from this method call.

</dd> <dt>

*vService* \[in\]
</dt> <dd>

**VARIANT** that defines the service. For more information, see Remarks.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                             | Description                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | The contact was added to the contacts list. <br/>                                                                                                                                                             |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | The parameter *bstrSiginName* resolved to a null value.<br/>                                                                                                                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | The parameter *bstrSiginName* is not valid for this method.<br/>                                                                                                                                              |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl> | The service is not logged on.<br/>                                                                                                                                                                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | The method call has failed due to a catastrophic error.<br/>                                                                                                                                                  |
| <dl> <dt>**MSGR\_E\_API\_LOCKED**</dt> </dl>     | Windows Messenger 5.0 and later. The application has called the Microsoft .NET Messenger Service without unlocking it. For more information, see [Messenger Lock and Key API](im-lock-and-key-ovw.md). <br/> |



 

## Remarks

The *vService* parameter can be specified as a **BSTR** containing the ID (not the name) of the service, or it can also be a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) of a [**MessengerService**](im-messengerservice.md) object.

The *vService* parameter can be specified as a **BSTR** containing the ID (not the name) of the service.

The following table lists the error codes returned by this method.



|            |                                                                                                                                   |
|------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0x80000003 | The parameter *bstrSiginName* is not valid for this method.                                                                       |
| 0x80004003 | The parameter *bstrSiginName* resolved to a null value.                                                                           |
| 0x80004005 | The method call has failed due to a catastrophic error.                                                                           |
| 0x8100031e | The service is not logged on.                                                                                                     |
| 0x81000752 | Windows Messenger 5.0 and later. The application has called the Microsoft .NET Messenger Service without acquiring a ID/Key pair. |



 

> [!Note]  
> This method is not available for scripting languages.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMessengerPrivate**](im-imessengerprivate.md)
</dt> <dt>

[**EnableAlertEvents**](im-imessengerprivate-enablealertevents-method.md)
</dt> <dt>

[**OnContactListAdd**](im-dmessengerprivateevents-oncontactlistadd.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





