---
title: CardDeleteContext function
description: Ends communication between the Microsoft Base Smart Card Cryptographic Service Provider (CSP) or smart card key storage provider (KSP) and the smart card module and cleans up resources that were allocated by the smart card module.
ms.assetid: 67fde63f-ef6d-49e9-be5d-1a8b0f526e84
keywords:
- CardDeleteContext function Security
topic_type:
- apiref
api_name:
- CardDeleteContext
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CardDeleteContext function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardDeleteContext** function, defined by a smart card module, ends communication between the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) (CSP) or smart card [*key storage provider*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-storage-provider-gly) (KSP) and the smart card module and cleans up resources that were allocated by the smart card module.

## Syntax


```C++
DWORD WINAPI CardDeleteContext(
  _In_ PCARD_DATA pCardData
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure created during the corresponding call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> </dl>

 

 





