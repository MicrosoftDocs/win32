---
title: CardChangeAuthenticatorEx function
description: Changes the authentication data associated with a smart card and a specified user type, using a specified personal identification number (PIN).
ms.assetid: 7d4fa201-1553-4e78-8972-54530decf978
keywords:
- CardChangeAuthenticatorEx function Smart Card
topic_type:
- apiref
api_name:
- CardChangeAuthenticatorEx
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CardChangeAuthenticatorEx function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardChangeAuthenticatorEx** function, defined by a smart card module, changes the authentication data associated with a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly) and a specified user type, using a specified personal identification number (PIN)

## Syntax


```C++
DWORD WINAPI CardChangeAuthenticatorEx(
  _In_      PCARD_DATA pCardData,
  _In_      DWORD      dwFlags,
  _In_      PIN_ID     dwAuthenticatingPinId,
  _In_      PBYTE      pbAuthenticatingPinData,
  _In_      DWORD      cbAuthenticatingPinData,
  _In_      PIN_ID     dwTargetPinId,
  _In_      PBYTE      pbTargetData,
  _In_      DWORD      cbTargetData,
  _In_      DWORD      cRetryCount,
  _Out_opt_ PDWORD     pcAttemptsRemaining
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

The type of authentication that this function performs. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CARD_UNBLOCK_PIN_CHALLENGE_RESPONSE"></span><span id="card_unblock_pin_challenge_response"></span><dl> <dt>**CARD\_UNBLOCK\_PIN\_CHALLENGE\_RESPONSE**</dt> <dt>1</dt> </dl> | The authentication data in the *pbCurrentAuthenticator* and *pbNewAuthenticator* buffers are responses to a challenge returned by the [**CardGetChallenge**](cardgetchallenge.md) function.<br/> |
| <span id="CARD_UNBLOCK_PIN_PIN"></span><span id="card_unblock_pin_pin"></span><dl> <dt>**CARD\_UNBLOCK\_PIN\_PIN**</dt> <dt>2</dt> </dl>                                               | The authentication data in the *pbCurrentAuthenticator* and *pbNewAuthenticator* buffers are PIN data.<br/>                                                                                       |



 

</dd> <dt>

*dwAuthenticatingPinId* \[in\]
</dt> <dd>

The PIN to be authenticated.

</dd> <dt>

*pbAuthenticatingPinData* \[in\]
</dt> <dd>

A pointer to a byte buffer containing the PIN data to be authenticated.

</dd> <dt>

*cbAuthenticatingPinData* \[in\]
</dt> <dd>

The length, in bytes, of the PIN data pointed to by the *pbAuthenticatingPinData* parameter

</dd> <dt>

*dwTargetPinId* \[in\]
</dt> <dd>

A pointer to the PIN to be updated.

</dd> <dt>

*pbTargetData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the new PIN identifier.

</dd> <dt>

*cbTargetData* \[in\]
</dt> <dd>

The length, in bytes, of the PIN in the buffer pointed to by the *pbTargetData* parameter.

</dd> <dt>

*cRetryCount* \[in\]
</dt> <dd>

The number of incorrect attempts at authentication that are allowed before the smart card is blocked.

To leave the number of allowed attempts unchanged, set the value of this parameter to zero.

Card modules that do not support setting the number of allowed attempts should return **SCARD\_E\_INVALID\_PARAMETER** if this parameter is set to any value other than zero.

</dd> <dt>

*pcAttemptsRemaining* \[out, optional\]
</dt> <dd>

On output, a pointer to a **DWORD** variable that contains the number of times that incorrect authentication data can be submitted before the card is locked.

If this function has already returned a zero as the value of this parameter and is called again, the function fails and returns **SCARD\_W\_CHV\_BLOCKED**.

If the value of this parameter is **NULL**, the smart card module ignores it.

Card modules that do not support a count of remaining authentication attempts should return a value of  1 for this parameter if the value of the parameter on input is not **NULL**.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





