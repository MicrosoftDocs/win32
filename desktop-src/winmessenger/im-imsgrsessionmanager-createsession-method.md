---
title: IMsgrSessionManager CreateSession method
description: Creates a new MsgrSession object.
ms.assetid: '9e3e7247-3f4c-4e3a-8ed9-cd8303b344d9'
keywords: ["CreateSession method Windows Messenger", "CreateSession method Windows Messenger , IMsgrSessionManager interface", "IMsgrSessionManager interface Windows Messenger , CreateSession method"]
topic_type:
- apiref
api_name:
- IMsgrSessionManager.CreateSession
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrSessionManager::CreateSession method

\[**CreateSession** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Creates a new [**MsgrSession**](im-msgrsession-object.md) object.

## Syntax


```C++
HRESULT CreateSession(
  [out, retval] IDispatch **ppSession
);
```



## Parameters

<dl> <dt>

*ppSession* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

Sets Address of a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface that returns the new session object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The [**MsgrSession**](im-msgrsession-object.md) object was created successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The parameter passed to the method was not valid.<br/>                                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The [**MsgrSession**](im-msgrsession-object.md) object cannot be created.<br/>        |



 

## Remarks

The following table lists the error codes returned by this method.



| Error Code | Meaning                                                                                |
|------------|----------------------------------------------------------------------------------------|
| 0x8007000E | The **MsgrSession** object cannot be created because the system has run out of memory. |
| 0x80070057 | The parameter passed to the method was not valid.                                      |



 

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

[**MsgrSession**](im-msgrsession-object.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





