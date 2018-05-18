---
title: CardUnblockPin function
description: Unblocks a smart card that has become blocked after exceeding the maximum number of incorrect PIN entry attempts. The function also authenticates a user to the smart card.
ms.assetid: 'e8d1a004-775d-4e8d-846a-10d2a4030b40'
keywords: ["CardUnblockPin function Security"]
topic_type:
- apiref
api_name:
- CardUnblockPin
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardUnblockPin function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardUnblockPin** function, defined by a smart card module, unblocks a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly) that has become blocked after exceeding the maximum number of incorrect PIN entry attempts. The function also authenticates a user to the smart card.

## Syntax


```C++
DWORD WINAPI CardUnblockPin(
  _In_ PCARD_DATA pCardData,
  _In_ LPWSTR     pwszUserId,
  _In_ PBYTE      pbAuthenticationData,
  _In_ DWORD      cbAuthenticationData,
  _In_ PBYTE      pbNewPinData,
  _In_ DWORD      cbNewPinData,
  _In_ DWORD      cRetryCount,
  _In_ DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pwszUserId* \[in\]
</dt> <dd>

A pointer to a string that contains the ID of the user associated with the PIN specified to unblock.

This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                            | Meaning                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <span id="wszCARD_USER_EVERYONE"></span><span id="wszcard_user_everyone"></span><span id="WSZCARD_USER_EVERYONE"></span><dl> <dt>**wszCARD\_USER\_EVERYONE**</dt> <dt>L"anonymous"</dt> </dl> | The user is an anonymous user.<br/>    |
| <span id="wszCARD_USER_USER"></span><span id="wszcard_user_user"></span><span id="WSZCARD_USER_USER"></span><dl> <dt>**wszCARD\_USER\_USER**</dt> <dt>L"user"</dt> </dl>                      | The user is not an administrator.<br/> |
| <span id="wszCARD_USER_ADMIN"></span><span id="wszcard_user_admin"></span><span id="WSZCARD_USER_ADMIN"></span><dl> <dt>**wszCARD\_USER\_ADMIN**</dt> <dt>L"admin"</dt> </dl>                 | The user is an administrator.<br/>     |



 

</dd> <dt>

*pbAuthenticationData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the authentication data. This data represents either a PIN or a response to an authentication challenge, depending on the value of the *dwFlags* parameter.

</dd> <dt>

*cbAuthenticationData* \[in\]
</dt> <dd>

The size, in bytes, of the data contained in the *pbAuthenticationData* buffer.

</dd> <dt>

*pbNewPinData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the new PIN to be set.

</dd> <dt>

*cbNewPinData* \[in\]
</dt> <dd>

The size, in bytes, of the data contained in the *pbNewPinData* buffer.

</dd> <dt>

*cRetryCount* \[in\]
</dt> <dd>

The number of incorrect attempts at authentication using the new PIN that are allowed before the smart card is blocked again.

To leave the number of allowed attempts unchanged, set the value of this parameter to –1. Card modules that do not support setting the number of allowed attempts should return **SCARD\_E\_INVALID\_PARAMETER** if this parameter is set to any value other than –1.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A **DWORD** value that represents the type of authentication that this function performs.

This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CARD_UNBLOCK_PIN_CHALLENGE_RESPONSE"></span><span id="card_unblock_pin_challenge_response"></span><dl> <dt>**CARD\_UNBLOCK\_PIN\_CHALLENGE\_RESPONSE**</dt> <dt>1</dt> </dl> | The authentication data in the *pbAuthenticationData* parameter is a response to a challenge from a previous call to the [**CardGetChallenge**](cardgetchallenge.md) function.<br/> |
| <span id="CARD_UNBLOCK_PIN_PIN"></span><span id="card_unblock_pin_pin"></span><dl> <dt>**CARD\_UNBLOCK\_PIN\_PIN**</dt> <dt>2</dt> </dl>                                               | The authentication data in the *pbAuthenticationData* parameter is a PIN.<br/>                                                                                                       |



 

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The value of the *pbAuthenticationData* parameter is **NULL**.<br/> |



 

## Remarks

This function both unblocks the PIN and authenticates the user.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
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

 

 





