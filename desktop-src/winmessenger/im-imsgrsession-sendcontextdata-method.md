---
title: IMsgrSession SendContextData method
description: Sends application-specific context data.
ms.assetid: 5f27b2fa-9dd5-4c77-8e67-ab670509e462
keywords:
- SendContextData method Windows Messenger
- SendContextData method Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , SendContextData method
topic_type:
- apiref
api_name:
- IMsgrSession.SendContextData
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

# IMsgrSession::SendContextData method

\[**SendContextData** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sends application-specific context data.

## Syntax


```C++
HRESULT SendContextData(
  [in] BSTR bstrData
);
```



## Parameters

<dl> <dt>

*bstrData* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** specifying context data for the application. *bstrData* has a limit of 300 characters.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                     | Description                                                                          |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                            | The application-specific context data was sent successfully.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                    | The application-specific context data passed to the method was not valid.<br/> |
| <dl> <dt>**SR\_CONTEXT\_DATA\_OVER\_LIMIT**</dt> </dl>   | The amount of context data is too large to be sent.<br/>                       |
| <dl> <dt>**SR\_NOT\_VALID\_FOR\_APP\_INVITE**</dt> </dl> | The context data is not valid for an invitation.<br/>                          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                   | There is not enough memory available to send the context data.<br/>            |



 

## Remarks

**SendContextData** should only be used by applications connecting to exchange information required to establish a peer-to-peer connection. This method can be called up to five times after the applications have established their own communication.

The following table lists the error codes returned by this method.



| Error Code                                    | Meaning                                                                   |
|-----------------------------------------------|---------------------------------------------------------------------------|
| 0x8007000E                                    | There is not enough memory available to send the context data.            |
| 0x80070057                                    | The application-specific context data passed to the method was not valid. |
| SR\_NOT\_VALID\_FOR\_APP\_INVITE (0x8100060f) | The context data is not valid for an invitation.                          |
| SR\_CONTEXT\_DATA\_OVER\_LIMIT (0x81000611)   | The amount of context data is too large to be sent.                       |



 

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

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





