---
title: PFN\_CSP\_PAD\_DATA function pointer
description: Pads a data buffer for use in a cryptographic operation when the smart card itself does not perform data padding.
ms.assetid: 04c5d7fa-96cb-4d1c-a150-d8d0aa0a95a3
keywords:
- PFN_CSP_PAD_DATA function pointer Security
topic_type:
- apiref
api_name:
- PFN_CSP_PAD_DATA
api_location:
- Cardmod.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PFN\_CSP\_PAD\_DATA function pointer

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **PFN\_CSP\_PAD\_DATA** function pads a data buffer for use in a cryptographic operation when the smart card itself does not perform data padding.

## Syntax


```C++
typedef DWORD ( WINAPI *PFN_CSP_PAD_DATA)(
  _In_  PCARD_SIGNING_INFO pSigningInfo,
  _In_  DWORD              cbMaxWidth,
  _Out_ DWORD              *pcbPaddedBuffer,
  _Out_ PBYTE              *ppbPaddedBuffer
);
```



## Parameters

<dl> <dt>

*pSigningInfo* \[in\]
</dt> <dd>

A pointer to the [**CARD\_SIGNING\_INFO**](card-signing-info.md) structure that specifies the data to pad and the hashing algorithm used to sign the data.

</dd> <dt>

*cbMaxWidth* \[in\]
</dt> <dd>

The maximum size, in bytes, of the padded buffer.

</dd> <dt>

*pcbPaddedBuffer* \[out\]
</dt> <dd>

A pointer to a **DWORD** value that specifies the size, in bytes, of the *ppbPaddedBuffer* array.

</dd> <dt>

*ppbPaddedBuffer* \[out\]
</dt> <dd>

The address of a pointer to an array of byte values that, on output, contains the padded data. When you have finished using the *ppbPaddedBuffer* array, free it by calling the [**PFN\_CSP\_FREE**](pfn-csp-free.md) function.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value.

## Remarks

Currently, only PKCS \#1 version 1.1 padding is supported.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> </dl>

 

 





