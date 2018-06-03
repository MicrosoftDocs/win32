---
title: CardChangeAuthenticator function
description: Changes the authentication data associated with a smart card and a specified user type.
ms.assetid: 401daea7-35d7-46e4-a9b3-8efd379e5923
keywords:
- CardChangeAuthenticator function Security
topic_type:
- apiref
api_name:
- CardChangeAuthenticator
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

# CardChangeAuthenticator function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardChangeAuthenticator** function, defined by a smart card module, changes the authentication data associated with a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly) and a specified user type.

## Syntax


```C++
DWORD WINAPI CardChangeAuthenticator(
  _In_      PCARD_DATA pCardData,
  _In_      LPWSTR     pwszUserId,
  _In_      PBYTE      pbCurrentAuthenticator,
  _In_      DWORD      cbCurrentAuthenticator,
  _In_      PBYTE      pbNewAuthenticator,
  _In_      DWORD      cbNewAuthenticator,
  _In_      DWORD      cRetryCount,
  _In_      DWORD      dwFlags,
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

A pointer to a string that contains the user ID. The ID is associated with the authentication data specified by the *pbCurrentAuthenticator* parameter.

This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                            | Meaning                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <span id="wszCARD_USER_EVERYONE"></span><span id="wszcard_user_everyone"></span><span id="WSZCARD_USER_EVERYONE"></span><dl> <dt>**wszCARD\_USER\_EVERYONE**</dt> <dt>L"anonymous"</dt> </dl> | The user is an anonymous user.<br/>    |
| <span id="wszCARD_USER_USER"></span><span id="wszcard_user_user"></span><span id="WSZCARD_USER_USER"></span><dl> <dt>**wszCARD\_USER\_USER**</dt> <dt>L"user"</dt> </dl>                      | The user is not an administrator.<br/> |
| <span id="wszCARD_USER_ADMIN"></span><span id="wszcard_user_admin"></span><span id="WSZCARD_USER_ADMIN"></span><dl> <dt>**wszCARD\_USER\_ADMIN**</dt> <dt>L"admin"</dt> </dl>                 | The user is an administrator.<br/>     |



 

</dd> <dt>

*pbCurrentAuthenticator* \[in\]
</dt> <dd>

A pointer to a buffer that contains the current authentication data. This data represents either a PIN or a response to an authentication challenge, depending on the value of the *dwFlags* parameter.

</dd> <dt>

*cbCurrentAuthenticator* \[in\]
</dt> <dd>

The size, in bytes, of the *pbCurrentAuthenticator* buffer.

</dd> <dt>

*pbNewAuthenticator* \[in\]
</dt> <dd>

A pointer to a buffer that contains the new authentication data. This data represents either a PIN or a response to an authentication challenge, depending on the value of the *dwFlags* parameter.

</dd> <dt>

*cbNewAuthenticator* \[in\]
</dt> <dd>

The size, in bytes, of the *pbNewAuthenticator* buffer.

</dd> <dt>

*cRetryCount* \[in\]
</dt> <dd>

The number of incorrect attempts at authentication that are allowed before the smart card is blocked.

To leave the number of allowed attempts unchanged, set the value of this parameter to zero.

Card modules that do not support setting the number of allowed attempts should return **SCARD\_E\_INVALID\_PARAMETER** if this parameter is set to any value other than zero.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

The type of authentication that this function performs. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CARD_UNBLOCK_PIN_CHALLENGE_RESPONSE"></span><span id="card_unblock_pin_challenge_response"></span><dl> <dt>**CARD\_UNBLOCK\_PIN\_CHALLENGE\_RESPONSE**</dt> <dt>1</dt> </dl> | The authentication data in the *pbCurrentAuthenticator* and *pbNewAuthenticator* buffers are responses to a challenge returned by the [**CardGetChallenge**](cardgetchallenge.md) function.<br/> |
| <span id="CARD_UNBLOCK_PIN_PIN"></span><span id="card_unblock_pin_pin"></span><dl> <dt>**CARD\_UNBLOCK\_PIN\_PIN**</dt> <dt>2</dt> </dl>                                               | The authentication data in the *pbCurrentAuthenticator* and *pbNewAuthenticator* buffers are PIN data.<br/>                                                                                       |



 

</dd> <dt>

*pcAttemptsRemaining* \[out, optional\]
</dt> <dd>

On output, a pointer to a **DWORD** variable that contains the number of times that incorrect authentication data can be submitted before the card is locked.

If this function has already returned a zero as the value of this parameter and is called again, the function fails and returns **SCARD\_W\_CHV\_BLOCKED**.

If the value of this parameter is **NULL**, the smart card module ignores it.

Card modules that do not support a count of remaining authentication attempts should return a value of  1 for this parameter if the value of the parameter on input is not **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The smart card module does not support changing the authentication data to the specified form.<br/> |
| <dl> <dt>**SCARD\_W\_WRONG\_CHV**</dt> <dt>2148532331 (0x8010006B)</dt> </dl>         | The authentication data is incorrect.<br/>                                                          |
| <dl> <dt>**SCARD\_W\_CHV\_BLOCKED**</dt> <dt>2148532332 (0x8010006C)</dt> </dl>       | The card has been blocked after too many attempts that use the wrong authentication data.<br/>      |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**CardAuthenticatePin**](cardauthenticatepin.md)
</dt> <dt>

[**CardGetChallenge**](cardgetchallenge.md)
</dt> </dl>

 

 





