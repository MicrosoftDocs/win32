---
title: IMsgrSession Accept method
description: Recipient accepts the invitation.
ms.assetid: 69505005-1e15-4768-8764-2fe51193596b
keywords:
- Accept method Windows Messenger
- Accept method Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , Accept method
topic_type:
- apiref
api_name:
- IMsgrSession.Accept
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

# IMsgrSession::Accept method

\[**Accept** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Recipient accepts the invitation.

## Syntax


```C++
HRESULT Accept(
  [in] BSTR bstrAppData
);
```



## Parameters

<dl> <dt>

*bstrAppData* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the application-specific data. *bstrAppData* has a limit of 512 bytes.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                | Description                                                                                        |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | The invitation was accepted successfully.<br/>                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | The parameter passed to the method was not valid.<br/>                                       |
| <dl> <dt>**SR\_SESSION\_STATE\_INVALID**</dt> </dl> | The [**SESSION\_STATE**](im-session-state-enum.md) of the accepting user is not valid.<br/> |



 

## Remarks

Use this method to programmatically accept an invitation within an application.

The recipient may accept the invitation by setting *bstrAppData* to **NULL** within the application.

The parameter defined in this method is passed to the recipient's session in the form of a notification from the [**OnAccepted**](im-dmsgrsessionevents-onaccepted.md) event.

The following table lists the error codes returned by this method.



| Error Code                               | Meaning                                                    |
|------------------------------------------|------------------------------------------------------------|
| 0x80070057                               | The parameter passed to the method was not valid.          |
| SR\_SESSION\_STATE\_INVALID (0x81000614) | The **SESSION\_STATE** of the accepting user is not valid. |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.0<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMsgrSession**](im-imsgrsession.md)
</dt> <dt>

[**Cancel**](im-imsgrsession-cancel-method.md)
</dt> <dt>

[**Decline**](im-imsgrsession-decline-method.md)
</dt> <dt>

[**Invite**](im-imsgrsession-invite-method.md)
</dt> <dt>

[**OnAccepted**](im-dmsgrsessionevents-onaccepted.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





