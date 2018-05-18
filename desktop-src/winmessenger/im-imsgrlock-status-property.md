---
title: IMsgrLock Status property
description: Returns the Lock and Key status.
ms.assetid: 'a3691317-f5e9-44da-8db2-53a833e3e26b'
keywords: ["Status property Windows Messenger", "Status property Windows Messenger , IMsgrLock interface", "IMsgrLock interface Windows Messenger , Status property"]
topic_type:
- apiref
api_name:
- IMsgrLock.Status
- IMsgrLock.get_Status
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMsgrLock::Status property

\[**Status** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Returns the Lock and Key status.

This property is read-only.

## Syntax


```C++
HRESULT get_Status(
  [out, retval] LockStatus *peStatus
);
```



## Property value

A pointer to one of the possible values from the [**LockStatus**](im-lockstatus-enum.md) enumeration, which defines the current Lock and Key status.

## Remarks

The following table lists the error codes returned by this property.



| Error Code | Meaning                                                               |
|------------|-----------------------------------------------------------------------|
| E\_POINTER | The return value did not resolve to one of the **LockStatus** values. |



 

The following table lists the error codes returned by this property.



| Error Code | Meaning                                                               |
|------------|-----------------------------------------------------------------------|
| 0x80004003 | The return value did not resolve to one of the **LockStatus** values. |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMsgrLock**](im-imsgrlock.md)
</dt> <dt>

[**SendResponse**](im-imsgrlock-sendresponse-method.md)
</dt> <dt>

[**RequestChallenge**](im-imsgrlock-requestchallenge-method.md)
</dt> <dt>

[**LockStatus**](im-lockstatus-enum.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





