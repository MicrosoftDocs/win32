---
title: IMsgrSession ContextData property
description: Retrieves a value that indicates the application-specific context data.
ms.assetid: fc72729c-d5fa-4396-92a4-e2a2459c3e0c
keywords:
- ContextData property Windows Messenger
- ContextData property Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , ContextData property
topic_type:
- apiref
api_name:
- IMsgrSession.ContextData
- IMsgrSession.get_ContextData
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

# IMsgrSession::ContextData property

\[**ContextData** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a value that indicates the application-specific context data.

This property is read-only.

## Syntax


```C++
HRESULT get_ContextData(
  [out, retval] BSTR *pbstrData
);
```



## Property value

Pointer to a **BSTR** that specifies the application-specific context data.

## Remarks

The following table lists the error codes returned by this property.



| Error Code     | Meaning                                                                  |
|----------------|--------------------------------------------------------------------------|
| E\_INVALIDARG  | The value passed to the property was not valid.                          |
| E\_OUTOFMEMORY | The context data was too long.                                           |
| S\_FALSE       | The context data was not retrieved successfully for unspecified reasons. |



 

The following table lists the error codes returned by this property.



| Error Code | Meaning                                  |
|------------|------------------------------------------|
| 0x8007000E | The context data was too long.           |
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

 

 





