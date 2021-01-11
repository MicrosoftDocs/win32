---
description: The RKeyCloseKeyService function is not supported.
ms.assetid: 3a3d41d4-d8ce-4ed8-a70b-dd3629ab7b44
title: RKeyCloseKeyService function (Rkeysvcc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RKeyCloseKeyService
api_type: 
- HeaderDef
api_location: 
- Rkeysvcc.h
---

# RKeyCloseKeyService function

The **RKeyCloseKeyService** function is not supported.

**Windows Server 2003:** The **RKeyCloseKeyService** function closes a key service handle opened by a previous call to the [**RKeyOpenKeyService**](rkeyopenkeyservice.md) function. Note that this behavior has changed with Windows Server 2003 with Service Pack 1 (SP1).

## Syntax


```C++
ULONG RKeyCloseKeyService(
  _In_    KEYSVCC_HANDLE hKeySvcCli,
  _Inout_ void           *pReserved
);
```



## Parameters

<dl> <dt>

*hKeySvcCli* \[in\]
</dt> <dd>

A [**KEYSVCC\_HANDLE**](keysvcc-handle.md) handle previously opened by [**RKeyOpenKeyService**](rkeyopenkeyservice.md). This value cannot be **NULL**.

</dd> <dt>

*pReserved* \[in, out\]
</dt> <dd>

Reserved. Set this value to **NULL**.

</dd> </dl>

## Return value

If the function is successful, the return value is S\_OK.

If the function fails, the return value is a **ULONG** that indicates the error.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Rkeysvcc.h</dt> </dl> |



## See also

<dl> <dt>

[**RKeyOpenKeyService**](rkeyopenkeyservice.md)
</dt> <dt>

[**RKeyPFXInstall**](rkeypfxinstall.md)
</dt> </dl>

 

 




