---
title: CardQueryCapabilities function
description: Retrieves information about the functionality provided by a smart card.
ms.assetid: 0089535f-f591-41da-818d-297f8d15bb19
keywords:
- CardQueryCapabilities function Security
topic_type:
- apiref
api_name:
- CardQueryCapabilities
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

# CardQueryCapabilities function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardQueryCapabilities** function, defined by a smart card module, retrieves information about the functionality provided by a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardQueryCapabilities(
  _In_    PCARD_DATA         pCardData,
  _Inout_ PCARD_CAPABILITIES pCardCapabilities
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pCardCapabilities* \[in, out\]
</dt> <dd>

A pointer to a [**CARD\_CAPABILITIES**](card-capabilities.md) structure that, on output, contains information about the capabilities of the smart card.

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

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CARD\_CAPABILITIES**](card-capabilities.md)
</dt> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> </dl>

 

 





