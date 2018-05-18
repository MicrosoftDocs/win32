---
title: CardConstructDHAgreement function
description: Performs a secret agreement calculation for Diffie-Hellman key exchange by using the specified private key.
ms.assetid: 'ec3bed22-f16a-4fb4-912a-74fb70811c8a'
keywords: ["CardConstructDHAgreement function Security"]
topic_type:
- apiref
api_name:
- CardConstructDHAgreement
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardConstructDHAgreement function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardConstructDHAgreement** function, defined by a smart card module, performs a secret agreement calculation for Diffie-Hellman key exchange by using the specified [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly).

**Windows Server 2003, Windows XP, Windows 2000 Server and Windows 2000 Professional:** This function is not supported.

## Syntax


```C++
DWORD WINAPI CardConstructDHAgreement(
  _In_ PCARD_DATA              pCardData,
  _In_ PCARD_DH_AGREEMENT_INFO pAgreementInfo
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pAgreementInfo* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DH\_AGREEMENT\_INFO**](card-dh-agreement-info.md) structure that, on input, specifies the index of the container that contains the keys to exchange. On output, the structure contains a handle to the calculated secret agreement.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> </dl>

 

 





