---
title: CspGetDHAgreement callback function
description: Is a callback function that is set by a caller before calling the CardAcquireContext function.
ms.assetid: fd167c7e-8523-4385-b6d1-a17422b24a88
keywords:
- CspGetDHAgreement callback function Smart Card
topic_type:
- apiref
api_name:
- CspGetDHAgreement
api_location:
- Cardmod.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CspGetDHAgreement callback function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The *CspGetDHAgreement* function is a callback function that is set by a caller before calling the [**CardAcquireContext**](cardacquirecontext.md) function. If the [**CARD\_DERIVE\_KEY**](card-derive-key.md) structure used for a call to [**CardDeriveKey**](cardderivekey.md) specifies a parameter of the type **KDF\_NCRYPT\_SECRET\_HANDLE**, the smart card module calls this function to get the handle on the smart card.

## Syntax


```C++
DWORD WINAPI CspGetDHAgreement(
  _In_  PCARD_DATA pCardData,
  _In_  PVOID      hSecretAgreement,
  _Out_ BYTE       *pbSecretAgreementIndex,
  _In_  DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*hSecretAgreement* \[in\]
</dt> <dd>

A pointer to the [**BCryptBuffer**](https://msdn.microsoft.com/library/windows/desktop/aa375368) structure that specifies the **KDF\_NCRYPT\_SECRET\_HANDLE** parameter used in the call to [**CardDeriveKey**](cardderivekey.md).

</dd> <dt>

*pbSecretAgreementIndex* \[out\]
</dt> <dd>

On output, specifies the index of the key container on the smart card that contains the secret handle.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



 

 





