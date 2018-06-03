---
title: CardRSADecrypt function
description: Performs an RSA decryption of the specified data by using the specified private key.
ms.assetid: f66dafe1-7de9-4474-a166-3867819a50ff
keywords:
- CardRSADecrypt function Security
topic_type:
- apiref
api_name:
- CardRSADecrypt
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

# CardRSADecrypt function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardRSADecrypt** function, defined by a smart card module, performs an [*RSA*](https://msdn.microsoft.com/library/windows/desktop/ms721604#-security-rsa-gly) decryption of the specified data by using the specified [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly). The decryption operation must be for a single data buffer of the same size as the key modulus.

## Syntax


```C++
DWORD WINAPI CardRSADecrypt(
  _In_    PCARD_DATA             pCardData,
  _Inout_ PCARD_RSA_DECRYPT_INFO pInfo
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pInfo* \[in, out\]
</dt> <dd>

A pointer to a [**CARD\_RSA\_DECRYPT\_INFO**](card-rsa-decrypt-info.md) structure that specifies the data to decrypt and the private key to use for the decryption. On output, the structure contains the decrypted data.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                          | Description                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INSUFFICIENT\_BUFFER**</dt> <dt>2148532231 (0x80100007)</dt> </dl> | The **pbData** member of the *pInfo* parameter is not of sufficient size.<br/> |



 

## Remarks

Card modules that support only elliptic curve cryptography (ECC), do not implement this function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



 

 





