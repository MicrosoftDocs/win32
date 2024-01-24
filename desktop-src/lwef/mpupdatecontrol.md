---
title: MpUpdateControl function (MpClient.h)
description: Allows the control of a signature update operation that was asynchronously initiated via MpUpdateStart.
ms.assetid: 2780E472-6E8D-4839-88EE-46E3448C6BF5
keywords:
- MpUpdateControl function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpUpdateControl
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpUpdateControl function

Allows the control of a signature update operation that was asynchronously initiated via [**MpUpdateStart**](mpupdatestart.md). Calling this function requires administrator privilege as it allows the cancellation of a system-wide signature update.

## Syntax


```C++
HRESULT WINAPI MpUpdateControl(
  _In_ MPHANDLE  hUpdateHandle,
  _In_ MPCONTROL UpdateControl
);
```



## Parameters

<dl> <dt>

*hUpdateHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to an asynchronous signature update operation. This handle is returned by the [**MpScanStart**](mpscanstart.md) function.

</dd> <dt>

*UpdateControl* \[in\]
</dt> <dd>

Type: **MPCONTROL**

Specifies the signature update control option. It must be the following value:



| Value                                                                                                                                                               | Meaning                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="MPCONTROL_ABORT"></span><span id="mpcontrol_abort"></span><dl> <dt>**MPCONTROL\_ABORT**</dt> </dl> | Abort the signature update operation.<br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If the function succeeds the return value is **S\_OK**.

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

[**MpScanStart**](mpscanstart.md)
</dt> </dl>

 

 





