---
title: WsSetAutoFail function (WebServicesDebug.h)
description: Sets the next point to inject a failure. This is a DEBUG ONLY function.
ms.assetid: b453dbc5-01ff-486d-8767-254b74cc5b6e
keywords:
- WsSetAutoFail function Web Services for Windows
topic_type:
- apiref
api_name:
- WsSetAutoFail
api_location:
- WebServicesDebug.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WsSetAutoFail function

Sets the next point to inject a failure. This is a DEBUG ONLY function.

## Syntax


```C++
HRESULT WINAPI  WsSetAutoFail(
  _In_     ULONG     count,
  _In_opt_ WS_ERROR* error
);
```



## Parameters

<dl> <dt>

*count* \[in\]
</dt> <dd>

Specifies how many operations before failures begin to occur.

</dd> <dt>

*error* \[in, optional\]
</dt> <dd>

A pointer to a [WS\_ERROR](ws-error.md) object where additional information about the error should be stored if the function fails.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>WebServicesDebug.h</dt> </dl> |



 

 





