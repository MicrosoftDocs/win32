---
description: Deletes the user credential used for the connected identity.
ms.assetid: EB32832D-9A8C-4CEB-897A-7E9D24FF84DD
title: DeleteConnectedIdentity function (Indentitystore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeleteConnectedIdentity
api_type: 
- HeaderDef
api_location: 
- Indentitystore.h
---

# DeleteConnectedIdentity function

Deletes the user credential used for the connected identity.

## Syntax


```C++
SEC_ENTRY DeleteConnectedIdentity(
  _In_     PVOID  ProviderHandle,
  _In_opt_ HANDLE UserToken,
  _In_     PSID   UserSid,
  _In_     PWSTR  IdentityUserName
);
```



## Parameters

<dl> <dt>

*ProviderHandle* \[in\]
</dt> <dd>

Identity provider handle.

</dd> <dt>

*UserToken* \[in, optional\]
</dt> <dd>

Token of the connected user whose account is going to be converted to a local account. If *UserToken* is not **NULL**, the identity provider uses this token to load the user profile and clean up connected states. If *UserToken* is **NULL**, LSA is forcing the disconnection. The identity provider should clean up any global connected states on this user, but the provider does not have to clean up connected states in the user profile.

</dd> <dt>

*UserSid* \[in\]
</dt> <dd>

The primary SID of the connected user. If *UserToken* is not **NULL**, this parameter is the user SID of the token. If *UserToken* is **NULL**, this parameter is used to identify the connected user and clean up global connected states of that user.

</dd> <dt>

*IdentityUserName* \[in\]
</dt> <dd>

The user name of the identity.

</dd> </dl>

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, the function may return one of the following error codes.



| Return value                                                                                               | Description                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>STATUS\_INVALID\_PARAMETER</dt> </dl>      | A parameter is not valid.<br/>                                                                                                                        |
| <dl> <dt>STATUS\_NO\_SUCH\_USER</dt> </dl>          | The user identified by *UserSid* does not exist, is not currently connected, or there is no identity whose user name matches *IdentityUserName*.<br/> |
| <dl> <dt>STATUS\_INSUFFICIENT\_RESOURCES</dt> </dl> | There is not enough memory to process the request.<br/>                                                                                               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Indentitystore.h</dt> </dl> |



 

 




