---
title: CardAcquireContext function
description: Initializes communication between the smart card module and either the Microsoft Base Smart Card Cryptographic Service Provider (CSP) or smart card key storage provider (KSP).
ms.assetid: 'b668f726-f817-4edc-8868-1130006c0b4e'
keywords: ["CardAcquireContext function Security"]
topic_type:
- apiref
api_name:
- CardAcquireContext
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardAcquireContext function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardAcquireContext** function, defined by a smart card module, initializes communication between the smart card module and either the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) (CSP) or smart card [*key storage provider*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-storage-provider-gly) (KSP).

## Syntax


```C++
DWORD WINAPI CardAcquireContext(
  _In_ PCARD_DATA pCardData,
  _In_ DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure. The **dwVersion** member of the **CARD\_DATA** structure must be initialized to the requested version of the structure to be returned by the smart card module.

On output, the structure contains a table of card module functions and information about the state of the smart card module. On successful output, the **dwVersion** member of the [**CARD\_DATA**](card-data.md) structure must be set to the actual version of the structure returned by the smart card module.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_UNKNOWN\_CARD**</dt> <dt>2148532237 (0x8010000D)</dt> </dl>      | The **pbAtr** member of the [**CARD\_DATA**](card-data.md) structure passed as the *pCardData* parameter does not refer to a valid smart card, or the smart card module does not recognize the specified smart card.<br/>                               |
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The **pbAtr**, **cbAtr**, or **pwszCardName** member of the [**CARD\_DATA**](card-data.md) structure passed as the *pCardData* parameter contains a **NULL** or a value that is not valid, or the *pCardData* parameter contains a **NULL** value.<br/> |



 

## Remarks

This function must be able to return multiple [**CARD\_DATA**](card-data.md) structures upon multiple calls.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Smart Card Modules](smart-card-modules.md)
</dt> <dt>

[**CARD\_DATA**](card-data.md)
</dt> </dl>

 

 





