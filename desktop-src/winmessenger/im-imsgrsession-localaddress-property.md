---
title: IMsgrSession LocalAddress property
description: Sets or retrieves the Internet Protocol (IP) address of the session.
ms.assetid: e2433f50-8d87-4b0d-ad39-7f3fe69833ea
keywords:
- LocalAddress property Windows Messenger
- LocalAddress property Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , LocalAddress property
topic_type:
- apiref
api_name:
- IMsgrSession.LocalAddress
- IMsgrSession.get_LocalAddress
- IMsgrSession.put_LocalAddress
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMsgrSession::LocalAddress property

\[**LocalAddress** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the Internet Protocol (IP) address of the session.

This property is read/write.

## Syntax


```C++
HRESULT put_LocalAddress(
  [in]          BSTR bstrLocalAddress
);

HRESULT get_LocalAddress(
  [out, retval] BSTR *pbstrLocalAddress
);
```



## Property value

**BSTR** that specifies the local IP address of the session. This address can be no longer than 30 characters.

## Remarks

Setting this property does not change the physical IP address of the computer. Instead, it modifies a data member within the [**MsgrSession**](im-msgrsession-object.md) object.

The following table lists the error codes returned by this property.



| Error Code     | Meaning                                             |
|----------------|-----------------------------------------------------|
| E\_INVALIDARG  | The parameter passed to the property was not valid. |
| E\_OUTOFMEMORY | The local address is too long.                      |



 

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

[**MsgrSession**](im-msgrsession-object.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





