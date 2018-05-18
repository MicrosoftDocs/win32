---
title: IMsgrSession Decline method
description: Recipient declines the invitation.
ms.assetid: 'dd586d45-6429-4c3f-a802-8c10247db9de'
keywords: ["Decline method Windows Messenger", "Decline method Windows Messenger , IMsgrSession interface", "IMsgrSession interface Windows Messenger , Decline method"]
topic_type:
- apiref
api_name:
- IMsgrSession.Decline
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrSession::Decline method

\[**Decline** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Recipient declines the invitation.

## Syntax


```C++
HRESULT Decline(
  [in] BSTR bstrAppData
);
```



## Parameters

<dl> <dt>

*bstrAppData* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the application data. *bstrAppData* has a limit of 512 bytes.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                | Description                                                    |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | The invitation was declined successfully.<br/>           |
| <dl> <dt>**SR\_NOT\_INVITEE**</dt> </dl>            | The invitation was sent to the wrong user.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | The value passed to the method was not valid.<br/>       |
| <dl> <dt>**SR\_SESSION\_STATE\_INVALID**</dt> </dl> | The session state of the invited user is not valid.<br/> |



 

## Remarks

The recipient can decline the invitation by setting *bstrAppData* to **NULL** within the application.

The parameter defined in this method is passed to the recipient's session in the form of a notification from the [**OnDeclined**](im-dmsgrsessionevents-ondeclined.md) event.

The following table lists the error codes returned by this method.



| Error Code                               | Meaning                                             |
|------------------------------------------|-----------------------------------------------------|
| 0x80070057                               | The value passed to the method was not valid.       |
| SR\_NOT\_INVITEE (0x8100060b)            | The invitation was sent to the wrong user.          |
| SR\_SESSION\_STATE\_INVALID (0x81000614) | The session state of the invited user is not valid. |



 

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

[**Invite**](im-imsgrsession-invite-method.md)
</dt> <dt>

[**OnDeclined**](im-dmsgrsessionevents-ondeclined.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





