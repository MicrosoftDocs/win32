---
Description: Gets the status of the users account.
title: DIDiskQuotaUser.AccountStatus property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DIDiskQuotaUser.AccountStatus property

Gets the status of the user's account.

This property is read-only.

## Syntax


```JScript
iAccountStatus = DIDiskQuotaUser.AccountStatus
```



## Property value

This property can take one of the following values.



| Status            | Value | Description                         |
|-------------------|-------|-------------------------------------|
| dqAcctResolved    | 0     | Account information is resolved.    |
| dqAcctUnavailable | 1     | Account information is unavailable. |
| dqAcctDeleted     | 2     | Account has been deleted.           |
| dqAcctInvalid     | 3     | Account is invalid.                 |
| dqAcctUnknown     | 4     | Account cannot be found.            |
| dqAcctUnresolved  | 5     | Account information is unresolved.  |



 

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DIDiskQuotaUser Object**](didiskquotauser-object.md)
</dt> </dl>

 

 




