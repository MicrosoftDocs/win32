---
title: CardAuthenticatePin function
description: authenticates a user by submitting a PIN to the smart card.
ms.assetid: 529d7bcc-0113-4983-81e7-0b6af310c000
keywords:
- CardAuthenticatePin function Security
topic_type:
- apiref
api_name:
- CardAuthenticatePin
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CardAuthenticatePin function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardAuthenticatePin** function, defined by a smart card module, [*authenticates*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-authentication-gly) a user by submitting a PIN to the [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardAuthenticatePin(
  _In_      PCARD_DATA pCardData,
  _In_      LPWSTR     pwszUserId,
  _In_      PBYTE      pbPin,
  _In_      DWORD      cbPin,
  _Out_opt_ PDWORD     pcAttemptsRemaining
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pwszUserId* \[in\]
</dt> <dd>

A pointer to a string that contains the user ID. This ID is associated with the PIN specified by the *pbPin* parameter.

This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="wszCARD_USER_EVERYONE"></span><span id="wszcard_user_everyone"></span><span id="WSZCARD_USER_EVERYONE"></span><dl> <dt>**wszCARD\_USER\_EVERYONE**</dt> <dt>L"anonymous"</dt> </dl> | The user is anonymous.<br/>                                                                                                                                                                                                                                    |
| <span id="wszCARD_USER_USER"></span><span id="wszcard_user_user"></span><span id="WSZCARD_USER_USER"></span><dl> <dt>**wszCARD\_USER\_USER**</dt> <dt>L"user"</dt> </dl>                      | The user is not an administrator.<br/>                                                                                                                                                                                                                         |
| <span id="wszCARD_USER_ADMIN"></span><span id="wszcard_user_admin"></span><span id="WSZCARD_USER_ADMIN"></span><dl> <dt>**wszCARD\_USER\_ADMIN**</dt> <dt>L"admin"</dt> </dl>                 | The user is an administrator. We recommend that administrators be authenticated by using the [**CardGetChallenge**](cardgetchallenge.md) and [**CardAuthenticateChallenge**](cardauthenticatechallenge.md) functions instead of by using this function.<br/> |



 

</dd> <dt>

*pbPin* \[in\]
</dt> <dd>

A pointer to a buffer that contains the PIN.

</dd> <dt>

*cbPin* \[in\]
</dt> <dd>

The size, in bytes, of the *pbPin* buffer.

</dd> <dt>

*pcAttemptsRemaining* \[out, optional\]
</dt> <dd>

On output, a pointer to a **DWORD** variable that contains the number of times that an incorrect PIN can be submitted before the card is locked.

If this function has already returned a zero as the value of this parameter and is called again, the function fails and returns **SCARD\_W\_CHV\_BLOCKED**.

If the value of this parameter is **NULL**, the smart card module ignores it.

Card modules that do not support a count of remaining authentication attempts should return a value of  1 for this parameter if the value of the parameter on input is not **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The value of the *pbPin* parameter is **NULL**.<br/>                           |
| <dl> <dt>**SCARD\_W\_WRONG\_CHV**</dt> <dt>2148532331 (0x8010006B)</dt> </dl>         | The PIN is incorrect.<br/>                                                     |
| <dl> <dt>**SCARD\_W\_CHV\_BLOCKED**</dt> <dt>2148532332 (0x8010006C)</dt> </dl>       | The card has been blocked after too many attempts that use the wrong PIN.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> </dl>

 

 





