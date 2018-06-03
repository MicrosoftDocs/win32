---
title: IMessenger2 CreateGroup method
description: Creates a new group to the MessengerGroups collection object.
ms.assetid: 3879d150-9693-4ea7-9d8c-64a52e5e2db3
keywords:
- CreateGroup method Windows Messenger
- CreateGroup method Windows Messenger , IMessenger2 interface
- IMessenger2 interface Windows Messenger , CreateGroup method
topic_type:
- apiref
api_name:
- IMessenger2.CreateGroup
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

# IMessenger2::CreateGroup method

\[**CreateGroup** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Creates a new group to the [**MessengerGroups**](im-messengergroups.md) collection object.

## Syntax


```C++
HRESULT CreateGroup(
  [in]          BSTR      bstrName,
  [in]          VARIANT   vService,
  [out, retval] IDispatch **ppGroup
);
```



## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

Type: **BSTR**

A **BSTR** that specifies the name of the group to be created.

</dd> <dt>

*vService* \[in\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that can take as its value either a **VT\_BSTR** string or a **VT\_DISPATCH** pointer to an existing [**MessengerService**](im-messengerservice.md) object.

</dd> <dt>

*ppGroup* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

Return value. Pointer to a pointer to an [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                    | Description                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | Success.<br/>                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**MSGR\_E\_GROUPS\_NOT\_ENABLED**</dt> </dl>   | Client has not enabled groups, or the current service does not support groups.<br/>                                                                                                                                                                                                                                      |
| <dl> <dt>**MSGR\_E\_GROUP\_NAME\_TOO\_LONG**</dt> </dl> | The new name of the group exceeds the maximum number of characters.<br/>                                                                                                                                                                                                                                                 |
| <dl> <dt>**MSGR\_E\_BAD\_GROUP\_NAME**</dt> </dl>       | The new name of the group is invalid. Characters such as carriage returns, linefeeds, tabs, and nonprintable characters are not allowed. Spaces before and after the group name will be trimmed automatically.<br/>                                                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | *bstrName* or *vService* (if **VT\_BSTR**) is a **NULL** string or contains nothing but spaces.<br/> - or -<br/> *vService* (if **VT\_BSTR**) exceeds the maximum number of characters.<br/> - or -<br/> *bstrName* or *vService* (if **VT\_BSTR**) contains a carriage return or linefeed.<br/> |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl>      | *ppGroup* is a **NULL** pointer. <br/>                                                                                                                                                                                                                                                                                   |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>        | Client was not signed in to the primary service at the time this method was called.<br/>                                                                                                                                                                                                                                 |
| <dl> <dt>**E\_POINTER**</dt> </dl>                      | *bstrName* is **NULL**.<br/>                                                                                                                                                                                                                                                                                             |



 

## Remarks

Some services, such as Microsoft Exchange Instant Messaging Service (IM), do not support groups. Using this method on these services will return the error, **MSGR\_E\_GROUPS\_NOT\_ENABLED**.

The **CreateGroup** method will look for a group name (*bstrName*) in the local user list of groups for the service (*vService*). If not found, the method will attempt to create a new group. To check the success of the creation of a new group, use [**OnGroupAdded**](im-dmessengerevents-ongroupadded.md).

The service parameter (*vService*) can be a string that contains the service ID, not the name, of the service. The service ID can be obtained from [**MyServiceId**](im-imessenger-myserviceid.md) for the primary service or from [**PrimaryService**](im-imessengerservices-primaryservice.md) or [**ServiceID**](im-imessengercontact-serviceid.md).

> [!Note]  
> This method is not available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger2**](im-imessenger2.md)
</dt> <dt>

[**IMessengerGroups**](im-imessengergroups.md)
</dt> </dl>

 

 





