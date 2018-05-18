---
title: IMsgrSession Cancel method
description: Inviter cancels the invitation.
ms.assetid: '0b66c54e-0163-4216-a96d-3a0b3198c8e7'
keywords: ["Cancel method Windows Messenger", "Cancel method Windows Messenger , IMsgrSession interface", "IMsgrSession interface Windows Messenger , Cancel method"]
topic_type:
- apiref
api_name:
- IMsgrSession.Cancel
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrSession::Cancel method

\[**Cancel** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Inviter cancels the invitation.

## Syntax


```C++
HRESULT Cancel(
  [in] long hr,
  [in] BSTR bstrAppData
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Type: **long**

**LONG** that specifies an error code that provides the reason for the session cancelation.

</dd> <dt>

*bstrAppData* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the application-specific data. *bstrAppData* has a limit of 512 bytes.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                 |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The invitation was canceled successfully.<br/>                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | The cancellation failed due to unspecified catastrophic reasons.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One of the parameters passed to the method was not valid.<br/>        |



 

## Remarks

The recipient can cancel the invitation by setting *bstrAppData* to **NULL** within the application.

The parameter defined in this method is passed to the recipient's session in the form of a notification from the [**OnCancelled**](im-dmsgrsessionevents-oncancelled.md) event.

The following table lists the error codes returned by this method.



| Error Code | Meaning                                                          |
|------------|------------------------------------------------------------------|
| 0x80004005 | The cancellation failed due to unspecified catastrophic reasons. |
| 0x80070057 | One of the parameters passed to the method was not valid.        |



 

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

[**Decline**](im-imsgrsession-decline-method.md)
</dt> <dt>

[**Invite**](im-imsgrsession-invite-method.md)
</dt> <dt>

[**OnCancelled**](im-dmsgrsessionevents-oncancelled.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





