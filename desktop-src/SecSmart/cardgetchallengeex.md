---
title: CardGetChallengeEx function
description: Authenticates a user in a with a specified role with a challenge and response.
ms.assetid: 7ca346cf-4408-4398-9790-0eb9aeca9749
keywords:
- CardGetChallengeEx function Smart Card
topic_type:
- apiref
api_name:
- CardGetChallengeEx
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CardGetChallengeEx function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardGetChallengeEx** function, defined by a smart card module, authenticates a user in a with a specified role with a challenge and response

## Syntax


```C++
DWORD WINAPI CardGetChallengeEx(
  _In_  PCARD_DATA pCardData,
  _In_  PIN_ID     PinId,
  _Out_ PBYTE      *ppbChallengeData,
  _In_  PDWORD     pcbChallengeData,
  _In_  DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*PinId* \[in\]
</dt> <dd>

The PIN identifier of the role to be authenticated.



| Value                                                                                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ROLE_EVERYONE"></span><span id="role_everyone"></span><dl> <dt>**ROLE\_EVERYONE**</dt> <dt>0</dt> </dl> | Specifies any requester, including unauthenticated or anonymous users.<br/>                                                                                                                                                                                                                                     |
| <span id="ROLE_USER"></span><span id="role_user"></span><dl> <dt>**ROLE\_USER**</dt> <dt>1</dt> </dl>             | Specifies a user client of the card, who proves his identity to the card by use of a PIN.<br/>                                                                                                                                                                                                                  |
| <span id="ROLE_ADMIN"></span><span id="role_admin"></span><dl> <dt>**ROLE\_ADMIN**</dt> <dt>2</dt> </dl>          | Specifies the card issuer or other party with an administrative relationship to the card or data on the card. Uses a special PIN or KEY which may or may not be unique to the card or user, to perform administrative tasks that the user cannot perform without use of this data, such as PIN unblocking.<br/> |



 

</dd> <dt>

*ppbChallengeData* \[out\]
</dt> <dd>

A pointer to a pointer to a buffer that receives the challenge data returned from the card.

</dd> <dt>

*pcbChallengeData* \[in\]
</dt> <dd>

The number of bytes of challenge data in the buffer pointed to by the *ppbChallengeData* parameter.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. Must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                            | Description                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>0x80100004L</dt> </dl> | One or more of the supplied parameters could not be properly interpreted.<br/> |



 

## Remarks

This authentication technique is normally used to establish the context for privileged operations such as unblocking a user's PIN. For security reasons, implementers of card minidrivers are advised to produce a design in which the challenge and response values are not invariant so that these values cannot be replayed.

The caller may elect not to use the challenge value. It is significant only if an authentication is attempted by using it. It is discarded if the next command to the card is not an authentication attempt using it (see [**CardAuthenticateChallenge**](cardauthenticatechallenge.md)). The smart card's internal operating system should be designed to enforce this behavior.

The challenge buffer is allocated by the card minidriver and freed by the caller by using PFN\_CSP\_FREE.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





