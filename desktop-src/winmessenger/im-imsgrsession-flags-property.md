---
title: IMsgrSession Flags property
description: Retrieves a value that indicates the session flags.
ms.assetid: db42e968-1c6a-419f-b44f-7d30c684cbfc
keywords:
- Flags property Windows Messenger
- Flags property Windows Messenger , IMsgrSession interface
- IMsgrSession interface Windows Messenger , Flags property
topic_type:
- apiref
api_name:
- IMsgrSession.Flags
- IMsgrSession.get_Flags
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

# IMsgrSession::Flags property

\[**Flags** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a value that indicates the session flags.

This property is read-only.

## Syntax


```C++
HRESULT get_Flags(
  [out, retval] LONG *plFlags
);
```



## Property value

Pointer to a variable of type **LONG** that returns one or more of the values in the [**SESSION\_FLAGS**](im-session-flags-enum.md) enumeration.

## Remarks

The following table lists the error codes returned by this property.



| Error Code    | Meaning                                             |
|---------------|-----------------------------------------------------|
| E\_INVALIDARG | The parameter passed to the property was not valid. |



 

The following table lists the error codes returned by this property.



| Error Code | Meaning                                  |
|------------|------------------------------------------|
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

[**SESSION\_FLAGS**](im-session-flags-enum.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





