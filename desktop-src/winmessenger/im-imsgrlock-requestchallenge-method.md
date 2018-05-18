---
title: IMsgrLock RequestChallenge method
description: Initiates an authentication challenge-response transaction between a Messenger client and a Messenger service .
ms.assetid: '4da596ef-2fe5-4e77-84b2-54523a5cff28'
keywords: ["RequestChallenge method Windows Messenger", "RequestChallenge method Windows Messenger , IMsgrLock interface", "IMsgrLock interface Windows Messenger , RequestChallenge method"]
topic_type:
- apiref
api_name:
- IMsgrLock.RequestChallenge
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrLock::RequestChallenge method

\[**RequestChallenge** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Initiates an authentication challenge-response transaction between a Messenger client and a Messenger service .

## Syntax


```C++
HRESULT RequestChallenge(
  [in] long lCookie
);
```



## Parameters

<dl> <dt>

*lCookie* \[in\]
</dt> <dd>

Type: **long**

**LONG** that identifies the authentication transaction session.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                    | Description                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | The challenge was initiated successfully.<br/>                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                         | The challenge has failed due to a catastrophic error.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | The parameter passed to the method was not valid.<br/>                        |
| <dl> <dt>**MSGR\_E\_API\_NOTINITIALIZED**</dt> </dl>    | The Messenger client lock and key mechanism is not initialized.<br/>          |
| <dl> <dt>**MSGR\_E\_API\_LOCKED**</dt> </dl>            | The Messenger service  API is locked.<br/>                                    |
| <dl> <dt>**MSGR\_E\_API\_PENDING\_UNLOCK**</dt> </dl>   | The application timed out while waiting for the result of the challenge.<br/> |
| <dl> <dt>**MSGR\_E\_API\_UNLOCK\_FAILED**</dt> </dl>    | The application response to the challenge failed.<br/>                        |
| <dl> <dt>**MSGR\_E\_API\_ALREADY\_UNLOCKED**</dt> </dl> | The Messenger service  API is already unlocked.<br/>                          |



 

## Remarks

This method is by used by a Messenger client to gain access to the Messenger service APIs. When this method is called by a Messenger client, an authentication challenge from a Messenger service is invoked. When the Messenger service challenge is received by the Messenger client, the [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md) event is fired. The Messenger client can then proceed with the challenge-response authentication process by invoking the [**SendResponse**](im-imsgrlock-sendresponse-method.md) method. For more information, see the overview on the [Messenger Lock and Key API](im-lock-and-key-ovw.md).

The client application can only request a challenge response from the server once. Therefore, if this method is called a second time during a Messenger client session, an error code is returned.

The following table lists the error codes returned by this method.



| Error Code                                   | Meaning                                                                  |
|----------------------------------------------|--------------------------------------------------------------------------|
| MSGR\_E\_API\_NOTINITIALIZED (0x81000751)    | The Messenger client lock and key mechanism is not initialized.          |
| MSGR\_E\_API\_LOCKED (0x81000752)            | The Messenger service  API is locked.                                    |
| MSGR\_E\_API\_UNLOCK\_FAILED (0x81000753)    | The application response to the challenge failed.                        |
| MSGR\_E\_API\_ALREADY\_UNLOCKED (0x81000754) | The Messenger service  API is already unlocked.                          |
| MSGR\_E\_API\_PENDING\_UNLOCK (0x81000755)   | The application timed out while waiting for the result of the challenge. |
| 0x80004005                                   | The challenge has failed due to a catastrophic error.                    |
| 0x80000003                                   | The parameter passed to the method was not valid.                        |



 

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

[**IMsgrLock**](im-imsgrlock.md)
</dt> <dt>

[**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md)
</dt> <dt>

[**SendResponse**](im-imsgrlock-sendresponse-method.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





