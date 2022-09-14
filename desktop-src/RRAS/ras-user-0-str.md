---
title: RAS_USER_0 structure (Rassapi.h)
description: The RAS\_USER\_0 structure is used in the RasAdminUserSetInfo and RasAdminUserGetInfo functions to specify information about a user.
ms.assetid: a2d4a935-f46d-4bc2-ada8-beaa3ac74834
keywords:
- RAS_USER_0 structure RAS
- PRAS_USER_0 structure pointer RAS
topic_type:
- apiref
api_name:
- RAS_USER_0
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_USER\_0 structure

\[This version of the **RAS\_USER\_0** structure is not supported as of Windows Vista. Use the newer [**RAS\_USER\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_user_0) defined in mprapi.h instead.\]

The **RAS\_USER\_0** structure is used in the [**RasAdminUserSetInfo**](rasadminusersetinfo.md) and [**RasAdminUserGetInfo**](rasadminusergetinfo.md) functions to specify information about a user.

## Syntax


```C++
typedef struct _RAS_USER_0 {
  BYTE  bfPrivilege;
  WCHAR szPhoneNumber[RASSAPI_MAX_PHONENUMBER_SIZE + 1];
} RAS_USER_0, *PRAS_USER_0;
```



## Members

<dl> <dt>

**bfPrivilege**
</dt> <dd>

A set of bit flags that specify the RAS privileges of the user. This member can be a combination of the RASPRIV\_DialinPrivilege flag and one of the call-back flags. Use the RASPRIV\_CallbackType mask to identify the type of call-back privilege provided to the user. The following flags are defined.



| Value                                                                                                                                                                                                                                         | Meaning                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <span id="RASPRIV_NoCallback"></span><span id="raspriv_nocallback"></span><span id="RASPRIV_NOCALLBACK"></span><dl> <dt>**RASPRIV\_NoCallback**</dt> </dl>                             | The user has no call-back privilege.<br/>                                               |
| <span id="RASPRIV_AdminSetCallback"></span><span id="raspriv_adminsetcallback"></span><span id="RASPRIV_ADMINSETCALLBACK"></span><dl> <dt>**RASPRIV\_AdminSetCallback**</dt> </dl>     | The user account is configured to have the administrator set the call-back number.<br/> |
| <span id="RASPRIV_CallerSetCallback"></span><span id="raspriv_callersetcallback"></span><span id="RASPRIV_CALLERSETCALLBACK"></span><dl> <dt>**RASPRIV\_CallerSetCallback**</dt> </dl> | The remote user can specify a call-back phone number when dialing in.<br/>              |
| <span id="RASPRIV_DialinPrivilege"></span><span id="raspriv_dialinprivilege"></span><span id="RASPRIV_DIALINPRIVILEGE"></span><dl> <dt>**RASPRIV\_DialinPrivilege**</dt> </dl>         | The user has permission to dial in to this server.<br/>                                 |



 

Specify one of the call-back flags in the call to the [**RasAdminUserSetInfo**](rasadminusersetinfo.md) function.

</dd> <dt>

**szPhoneNumber**
</dt> <dd>

A null-terminated Unicode string that specifies the call-back phone number for the user.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Rassapi.h</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[RAS Server Administration Structures](ras-server-administration-structures.md)
</dt> <dt>

[**RasAdminUserGetInfo**](rasadminusergetinfo.md)
</dt> <dt>

[**RasAdminUserSetInfo**](rasadminusersetinfo.md)
</dt> </dl>

 

 





