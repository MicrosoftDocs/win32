---
title: CardSignData function
description: Creates a digital signature for the specified block of data.
ms.assetid: 198c5e94-aede-4775-bcb8-92928b557fcc
keywords:
- CardSignData function Security
topic_type:
- apiref
api_name:
- CardSignData
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

# CardSignData function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardSignData** function, defined by a smart card module, creates a digital signature for the specified block of data.

## Syntax


```C++
DWORD WINAPI CardSignData(
  _In_    PCARD_DATA         pCardData,
  _Inout_ PCARD_SIGNING_INFO pInfo
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

A pointer to a [**CARD\_SIGNING\_INFO**](card-signing-info.md) structure that specifies the data to sign and the keys and hashing algorithm with which to sign the data. On output, the structure contains the signed data.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value.

## Remarks

This function can either pad the block of data on the smart card or pad the data by using the [**PFN\_CSP\_PAD\_DATA**](pfn-csp-pad-data.md) callback function.

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

 

 





