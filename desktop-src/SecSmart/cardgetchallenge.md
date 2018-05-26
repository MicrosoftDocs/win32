---
title: CardGetChallenge function
description: Authenticates a user with a challenge and response.
ms.assetid: 7e9b4784-eb2a-4513-8e0e-24099f4528ad
keywords:
- CardGetChallenge function Security
topic_type:
- apiref
api_name:
- CardGetChallenge
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CardGetChallenge function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardGetChallenge** function, defined by a smart card module, authenticates a user with a challenge and response.

## Syntax


```C++
DWORD WINAPI CardGetChallenge(
  _In_  PCARD_DATA pCardData,
  _Out_ PBYTE      *ppbChallengeData,
  _Out_ PDWORD     pcbChallengeData
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*ppbChallengeData* \[out\]
</dt> <dd>

A pointer to a **PBYTE** value that receives the challenge data from the [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

</dd> <dt>

*pcbChallengeData* \[out\]
</dt> <dd>

A pointer to a **DWORD** value that specifies the size, in bytes, of the challenge data contained in the *ppbChallengeData* parameter.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

## Remarks

The smart card creates challenge data by using its administrative key and places this data in the *ppbChallengeData* parameter. The caller then computes the response to the challenge by using shared knowledge of that key and submits the response to the card by calling the [**CardAuthenticateChallenge**](cardauthenticatechallenge.md) function. If the response is correct, the user is authenticated.

This authentication technique is normally used for privileged operations such as unblocking a user's PIN. To help avoid possible spoofing of identity, card module implementations should require that identical challenge and response values are not used more than once.

If the next call to the smart card module is not a call to the [**CardAuthenticateChallenge**](cardauthenticatechallenge.md) function that uses the challenge data received in the *ppbChallengeData* buffer, this function should discard that data.

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

[**CardAuthenticateChallenge**](cardauthenticatechallenge.md)
</dt> </dl>

 

 





