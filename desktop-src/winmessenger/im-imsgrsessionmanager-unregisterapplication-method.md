---
title: IMsgrSessionManager UnRegisterApplication method
description: Removes an application from the Messenger client list.
ms.assetid: '6f317284-0fa1-47a9-965d-5206abb0a695'
keywords: ["UnRegisterApplication method Windows Messenger", "UnRegisterApplication method Windows Messenger , IMsgrSessionManager interface", "IMsgrSessionManager interface Windows Messenger , UnRegisterApplication method"]
topic_type:
- apiref
api_name:
- IMsgrSessionManager.UnRegisterApplication
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrSessionManager::UnRegisterApplication method

\[**UnRegisterApplication** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Removes an application from the Messenger client list.

## Syntax


```C++
HRESULT UnRegisterApplication(
  [in] BSTR bstrAppGUID
);
```



## Parameters

<dl> <dt>

*bstrAppGUID* \[in\]
</dt> <dd>

Type: **BSTR**

The GUID of the application to unregister. Maximum character length is 39.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                            |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | The application was unregistered successfully.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | One of the parameters passed to the method was not valid.<br/>                   |
| <dl> <dt>**SR\_APP\_NOT\_REGISTERED**</dt> </dl> | You are attempting to unregister an application that is not yet registered.<br/> |
| <dl> <dt>**REGDB\_E\_WRITEREGDB**</dt> </dl>     | The method failed to delete the information from the registry.<br/>              |



 

## Remarks

To register an application, use the [**RegisterApplication**](im-imsgrsessionmanager-registerapplication-method.md) method.

The following table lists the error codes returned by this method.



| Error Code                            | Meaning                                                                     |
|---------------------------------------|-----------------------------------------------------------------------------|
| 0x80040151                            | The method failed to delete the information from the registry.              |
| 0x80070057                            | The parameter passed to the method was not valid.                           |
| SR\_APP\_NOT\_REGISTERED (0x8100060e) | You are attempting to unregister an application that is not yet registered. |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMsgrSessionManager**](im-imsgrsessionmanager.md)
</dt> <dt>

[**RegisterApplication**](im-imsgrsessionmanager-registerapplication-method.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





