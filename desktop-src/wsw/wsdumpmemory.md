---
title: WsDumpMemory function (WebServicesDebug.h)
description: This function dumps all memory allocations to the console.
ms.assetid: 84a4f1e7-7d62-48c2-a8a3-ee4573bde5e4
keywords:
- WsDumpMemory function Web Services for Windows
topic_type:
- apiref
api_name:
- WsDumpMemory
api_location:
- WebServicesDebug.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WsDumpMemory function

This function dumps all memory allocations to the console.

> [!Note]  
> This function is for DEBUG ONLY.

 

## Syntax


```C++
HRESULT WINAPI  WsDumpMemory(
  _In_opt_ WS_ERROR* error
);
```



## Parameters

<dl> <dt>

*error* \[in, optional\]
</dt> <dd>

A pointer to a [WS\_ERROR](ws-error.md) object where additional information about the error should be stored if the function fails.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>WebServicesDebug.h</dt> </dl> |



 

 





