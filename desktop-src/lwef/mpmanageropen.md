---
title: MpManagerOpen function (MpClient.h)
description: Establishes a connection to the malware protection manager on the local computer.
ms.assetid: 40513A74-AFCC-4E22-9B78-D46FEB575A00
keywords:
- MpManagerOpen function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpManagerOpen
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpManagerOpen function

Establishes a connection to the malware protection manager on the local computer.

## Syntax


```C++
HRESULT WINAPI MpManagerOpen(
  _In_  DWORD     dwReserved,
  _Out_ PMPHANDLE phMpHandle
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved for future use. Must be set to 0.

</dd> <dt>

*phMpHandle* \[out\]
</dt> <dd>

Type: **PMPHANDLE**

Handle to the malware protection manager interface. This handle must be closed with the [**MpHandleClose**](mphandleclose.md) function.

</dd> </dl>

## Return value

Type: **HRESULT**

If the function succeeds the return value is **S\_OK**. This function call is guaranteed to succeed even if an AntiMalware service is not running.

If the function fails then the return value is a failed **HRESULT** code. The caller can use the [**MpErrorMessageFormat**](mperrormessageformat.md) function to get a generic description of the error message.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MpClient.dll</dt> </dl> |



## See also

<dl> <dt>

[**MpErrorMessageFormat**](mperrormessageformat.md)
</dt> <dt>

[**MpHandleClose**](mphandleclose.md)
</dt> </dl>

 

 





