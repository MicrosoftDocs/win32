---
title: IMsgrSession RemoteAddress property
description: Retrieves a value that indicates the Internet Protocol (IP) address of the other party in the session.
ms.assetid: 0500bde6-865f-481a-8364-2b8b1ea73b46
keywords:
- RemoteAddress property Windows Messenger
- RemoteAddress property Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , RemoteAddress property
topic_type:
- apiref
api_name:
- IMsgrSession.RemoteAddress
- IMsgrSession.get_RemoteAddress
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

# IMsgrSession::RemoteAddress property

\[**RemoteAddress** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a value that indicates the Internet Protocol (IP) address of the other party in the session.

This property is read-only.

## Syntax


```C++
HRESULT get_RemoteAddress(
  [out, retval] BSTR *pbstrRemoteAddress
);
```



## Property value

Pointer to a **BSTR** that indicates the IP address of the other session participant.

## Remarks

The **get\_RemoteAddress** should be called after [**State**](im-imsgrsession-state-property.md) becomes SS\_CONNECTED.

The following table lists the error codes returned by this property.



| Error Code     | Meaning                                             |
|----------------|-----------------------------------------------------|
| E\_INVALIDARG  | The parameter passed to the property was not valid. |
| E\_OUTOFMEMORY | The IP address is too long.                         |
| S\_FALSE       | The IP address was not retrieved.                   |



 

The following table lists the error codes returned by this property.



| Error Code | Meaning                                  |
|------------|------------------------------------------|
| 0x8007000E | The IP address is too long.              |
| 0x80070057 | One of the possible values is not valid. |



 

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

 

 





