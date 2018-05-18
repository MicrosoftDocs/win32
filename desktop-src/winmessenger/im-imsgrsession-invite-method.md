---
title: IMsgrSession Invite method
description: Invites a user to the current session.
ms.assetid: 'e3196196-b0f1-4f80-8bf6-b9b7e97164fa'
keywords: ["Invite method Windows Messenger", "Invite method Windows Messenger , IMsgrSession interface", "IMsgrSession interface Windows Messenger , Invite method"]
topic_type:
- apiref
api_name:
- IMsgrSession.Invite
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrSession::Invite method

\[**Invite** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Invites a user to the current session.

## Syntax


```C++
HRESULT Invite(
  [in] IDispatch *pUser,
  [in] BSTR      bstrAppData
);
```



## Parameters

<dl> <dt>

*pUser* \[in\]
</dt> <dd>

Type: **IDispatch\***

Pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) of a [**MessengerContact**](im-messengercontact.md) object representing the user that is invited to the session.

</dd> <dt>

*bstrAppData* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the application specific data. *bstrAppData* has a limit of 512 bytes.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                        |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | The invitation was sent successfully.<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | One of the values passed into the method was not valid.<br/> |
| <dl> <dt>**SR\_APP\_NOT\_SPECIFIED**</dt> </dl>  | The application was not specified.<br/>                      |
| <dl> <dt>**SR\_SESSION\_NOT\_READY**</dt> </dl>  | The session is not ready.<br/>                               |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl> | The invited user is not logged on.<br/>                      |
| <dl> <dt>**SR\_INVITED\_SELF**</dt> </dl>        | The inviter and invitee are the same user.<br/>              |



 

## Remarks

The following table lists the error codes returned by this method.



| Error Code                           | Meaning                                                 |
|--------------------------------------|---------------------------------------------------------|
| 0x80070057                           | One of the values passed into the method was not valid. |
| 0x8100031e                           | The invited user is not logged on.                      |
| SR\_SESSION\_NOT\_READY (0x81000605) | The session is not ready.                               |
| SR\_APP\_NOT\_SPECIFIED (0x81000610) | The application was not specified.                      |
| SR\_INVITED\_SELF (0x81000613)       | The inviter and invitee are the same user.              |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.0<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMsgrSession**](im-imsgrsession.md)
</dt> <dt>

[**Accept**](im-imsgrsession-accept-method.md)
</dt> <dt>

[**Cancel**](im-imsgrsession-cancel-method.md)
</dt> <dt>

[**Decline**](im-imsgrsession-decline-method.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





