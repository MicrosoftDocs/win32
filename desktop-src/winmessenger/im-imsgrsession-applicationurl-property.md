---
title: IMsgrSession ApplicationURL property
description: Retrieves a value that indicates the application's URL from the registry.
ms.assetid: '795271d0-c57f-4066-8ee9-28bcc33f2c5c'
keywords: ["ApplicationURL property Windows Messenger", "ApplicationURL property Windows Messenger , IMsgrSession interface", "IMsgrSession interface Windows Messenger , ApplicationURL property"]
topic_type:
- apiref
api_name:
- IMsgrSession.ApplicationURL
- IMsgrSession.get_ApplicationURL
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrSession::ApplicationURL property

\[**ApplicationURL** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a value that indicates the application's URL from the registry.

This property is read-only.

## Syntax


```C++
HRESULT get_ApplicationURL(
  [out, retval] BSTR *pbstrURL
);
```



## Property value

Pointer to a variable of type **BSTR** that specifies the application's URL.

## Remarks

This property specifies the URL that the application can be downloaded from if it is not installed on the recipient's computer. By specifying a URL, both the inviter and recipient are able to run the application after installation.

The following table lists the error codes returned by this property.



| Error Code              | Meaning                                           |
|-------------------------|---------------------------------------------------|
| E\_INVALIDARG           | The value passed into the property was not valid. |
| SR\_FALSE               | The URL value is too long.                        |
| SR\_APP\_NOT\_SPECIFIED | The URL did not resolve.                          |



 

The following table lists the error codes returned by this property.



| Error Code | Meaning                                  |
|------------|------------------------------------------|
| 0x8007000E | The URL value is too long.               |
| 0x80070057 | One of the possible values is not valid. |



 

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

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





