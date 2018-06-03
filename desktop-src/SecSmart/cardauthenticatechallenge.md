---
title: CardAuthenticateChallenge function
description: Submits a response to a challenge issued by a smart card to authenticate a user.
ms.assetid: b1856322-f691-4cdb-a5a1-fce4dcdbdb69
keywords:
- CardAuthenticateChallenge function Security
topic_type:
- apiref
api_name:
- CardAuthenticateChallenge
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

# CardAuthenticateChallenge function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardAuthenticateChallenge** function, defined by a smart card module, submits a response to a challenge issued by a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly) to [*authenticate*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-authentication-gly) a user.

## Syntax


```C++
DWORD WINAPI CardAuthenticateChallenge(
  _In_      PCARD_DATA pCardData,
  _In_      PBYTE      pbResponseData,
  _In_      DWORD      cbResponseData,
  _Out_opt_ PDWORD     pcAttemptsRemaining
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pbResponseData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the response to the corresponding challenge received as the *ppbChallengeData* parameter of a previous call to the [**CardGetChallenge**](cardgetchallenge.md) function.

</dd> <dt>

*cbResponseData* \[in\]
</dt> <dd>

The size, in bytes, of the *pbResponseData* buffer.

</dd> <dt>

*pcAttemptsRemaining* \[out, optional\]
</dt> <dd>

A pointer to the count of remaining authentication attempts. The counter contains the number of times that an incorrect PIN can be submitted before the card is blocked.

If this function has already returned zero through this parameter and is called again, the function fails and returns **SCARD\_W\_CHV\_BLOCKED**.

If the value of this parameter is **NULL**, the smart card module ignores it.

Card modules that do not support a count of remaining authentication attempts should return a value of  1 for this parameter.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                  | Description                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_W\_WRONG\_CHV**</dt> <dt>2148532331 (0x8010006B)</dt> </dl>   | The response is not the correct response to the specified challenge.<br/>                |
| <dl> <dt>**SCARD\_W\_CHV\_BLOCKED**</dt> <dt>2148532332 (0x8010006C)</dt> </dl> | The card has been blocked after too many attempts that use the wrong response data.<br/> |



 

## Remarks

This authentication technique is normally used for privileged operations such as unblocking a user's PIN. To help avoid possible identity spoofing, card module implementations should require that identical challenge and response values are not used more than once.

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

[**CardGetChallenge**](cardgetchallenge.md)
</dt> </dl>

 

 





