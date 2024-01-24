---
description: Gets the status of the user's account.
title: DIDiskQuotaUser.AccountStatus property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DIDiskQuotaUser.AccountStatus
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: ff2234f7-4758-43c7-a3c2-8fb980b27c04

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DIDiskQuotaUser Object**](didiskquotauser-object.md)
</dt> </dl>

 

 




