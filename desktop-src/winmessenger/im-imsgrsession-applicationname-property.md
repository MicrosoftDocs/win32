---
title: IMsgrSession ApplicationName property
description: Retrieves a value that indicates the application name.
ms.assetid: 4cae3448-8cad-4097-b094-9067e7a5c6c5
keywords:
- ApplicationName property Windows Messenger
- ApplicationName property Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , ApplicationName property
topic_type:
- apiref
api_name:
- IMsgrSession.ApplicationName
- IMsgrSession.get_ApplicationName
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

# IMsgrSession::ApplicationName property

\[**ApplicationName** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a value that indicates the application name.

This property is read-only.

## Syntax


```C++
HRESULT get_ApplicationName(
  [out, retval] BSTR *pbstrName
);
```



## Property value

Pointer to a variable of type **BSTR** that specifies the application name.

## Remarks

If the application does not have a name, an empty string ("") is returned.

The following table lists the error codes returned by this property.



| Error Code              | Meaning                                           |
|-------------------------|---------------------------------------------------|
| E\_INVALIDARG           | The value passed into the property was not valid. |
| E\_OUTOFMEMORY          | The application name is too long.                 |
| SR\_APP\_NOT\_SPECIFIED | The application was not specified.                |



 

The following table lists the error codes returned by this property.



| Error Code                           | Meaning                                  |
|--------------------------------------|------------------------------------------|
| 0x8007000E                           | The application name is too long.        |
| 0x80070057                           | One of the possible values is not valid. |
| SR\_APP\_NOT\_SPECIFIED (0x81000610) | The application was not specified.       |



 

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

 

 





