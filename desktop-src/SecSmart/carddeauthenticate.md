---
title: CardDeauthenticate function
description: Reverses the effect of authenticating a user or administrator without resetting the smart card.
ms.assetid: '80b9d512-25ac-48d9-b5af-44a1d6982400'
keywords: ["CardDeauthenticate function Security"]
topic_type:
- apiref
api_name:
- CardDeauthenticate
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardDeauthenticate function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardDeauthenticate** function, defined by a smart card module, reverses the effect of authenticating a user or administrator without resetting the [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardDeauthenticate(
  _In_ PCARD_DATA pCardData,
  _In_ LPWSTR     pwszUserId,
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

A pointer to a null-terminated wide character string that contains the user ID for whom authentication is to be removed.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero value, and the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) (CSP) or smart card key storage provider (KSP) resets the smart card.

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
</dt> </dl>

 

 





