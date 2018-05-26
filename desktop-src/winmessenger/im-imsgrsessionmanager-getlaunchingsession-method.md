---
title: IMsgrSessionManager GetLaunchingSession method
description: Retrieves the session information that started the application.
ms.assetid: 364efb30-b114-404a-98eb-848e6c9dc2c5
keywords:
- GetLaunchingSession method Windows Messenger
- GetLaunchingSession method Windows Messenger , IMsgrSessionManager interface
- IMsgrSessionManager interface Windows Messenger , GetLaunchingSession method
topic_type:
- apiref
api_name:
- IMsgrSessionManager.GetLaunchingSession
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

# IMsgrSessionManager::GetLaunchingSession method

\[**GetLaunchingSession** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the session information that started the application.

## Syntax


```C++
HRESULT GetLaunchingSession(
  [in]          LONG      lProcessID,
  [out, retval] IDispatch **ppSession
);
```



## Parameters

<dl> <dt>

*lProcessID* \[in\]
</dt> <dd>

Type: **LONG**

**LONG** that specifies the process ID of the process.

</dd> <dt>

*ppSession* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

Address of a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface that returns the [**MsgrSession**](im-msgrsession-object.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                         |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The session information was retrieved successfully.<br/>                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One of the parameters passed to the method was not valid.<br/>                |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | The session information cannot be retrieved due to a catastrophic error.<br/> |



 

## Remarks

Process IDs can be viewed from within the Task Manager.

The following table lists the error codes returned by this method.



| Error Code | Meaning                                                                  |
|------------|--------------------------------------------------------------------------|
| 0x80004005 | The session information cannot be retrieved due to a catastrophic error. |
| 0x80070057 | One of the parameters passed to the method was not valid.                |



 

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

[**IMsgrSessionManager**](im-imsgrsessionmanager.md)
</dt> <dt>

[**MsgrSession**](im-msgrsession-object.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





