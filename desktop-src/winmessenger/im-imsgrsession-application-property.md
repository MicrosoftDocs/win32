---
title: IMsgrSession Application property
description: Obtains the application's GUID set by the inviter for this session from the registry.
ms.assetid: '018ff841-51ff-411e-a600-c726bc5eea9e'
keywords: ["Application property Windows Messenger", "Application property Windows Messenger , IMsgrSession interface", "IMsgrSession interface Windows Messenger , Application property"]
topic_type:
- apiref
api_name:
- IMsgrSession.Application
- IMsgrSession.get_Application
- IMsgrSession.put_Application
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrSession::Application property

\[**Application** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Obtains the application's GUID set by the inviter for this session from the registry.

This property is read/write.

## Syntax


```C++
HRESULT put_Application(
  [in]          BSTR bstrAppGUID
);

HRESULT get_Application(
  [out, retval] BSTR *pbstrAppGUID
);
```



## Property value

**BSTR** that specifies the application GUID. Maximum character length is 39 characters.

## Remarks

The application's GUID format is {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX} where X is a hexadecimal digit (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F) and alphanumeric characters are in uppercase.

Setting *bstrAppGUID* to a GUID of an application not previously registered from a call to [**RegisterApplication**](im-imsgrsessionmanager-registerapplication-method.md) will cause an error. This GUID must match one of the applications already registered.

The following table lists the error codes returned by this property.



| Error Code              | Meaning                                           |
|-------------------------|---------------------------------------------------|
| E\_INVALIDARG           | The value passed into the property was not valid. |
| E\_OUTOFMEMORY          | The application ID value is too long.             |
| SR\_APP\_NOT\_SPECIFIED | The application was not specified.                |
| SR\_SESSION\_NOT\_READY | The session is not ready.                         |



 

The following table lists the error codes returned by this method.



| Error Code                           | Meaning                                           |
|--------------------------------------|---------------------------------------------------|
| 0x8007000E                           | The application ID value is too long.             |
| 0x80070057                           | The value passed into the property was not valid. |
| SR\_SESSION\_NOT\_READY (0x81000605) | The session is not ready.                         |
| SR\_APP\_NOT\_SPECIFIED (0x81000610) | The application was not specified.                |



 

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

[**RegisterApplication**](im-imsgrsessionmanager-registerapplication-method.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





