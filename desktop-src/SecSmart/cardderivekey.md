---
title: CardDeriveKey function
description: Creates a session key by using the information in the specified CARD\_DERIVE\_KEY structure.
ms.assetid: '44c487e4-7406-41de-a957-97a87038b135'
keywords: ["CardDeriveKey function Security"]
topic_type:
- apiref
api_name:
- CardDeriveKey
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardDeriveKey function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardDeriveKey** function, defined by a smart card module, creates a [*session key*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-session-key-gly) by using the information in the specified [**CARD\_DERIVE\_KEY**](card-derive-key.md) structure.

## Syntax


```C++
DWORD WINAPI CardDeriveKey(
  _In_ PCARD_DATA       pCardData,
  _In_ PCARD_DERIVE_KEY pAgreementInfo
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pAgreementInfo* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DERIVE\_KEY**](card-derive-key.md) structure that specifies the *key derivation function* (KDF) to use to derive the key.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The **pwszKDF** member of the [**CARD\_DERIVE\_KEY**](card-derive-key.md) structure specified by the *pAgreementInfo* parameter contains a KDF that the smart card module does not support.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



 

 





