---
title: MpScanControl function (MpClient.h)
description: Allows the control of a scan that was asynchronously initiated via MpScanStart.
ms.assetid: 00855686-8C46-4B58-829C-AEAB53888704
keywords:
- MpScanControl function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpScanControl
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpScanControl function

Allows the control of a scan that was asynchronously initiated via [**MpScanStart**](mpscanstart.md).

## Syntax


```C++
HRESULT WINAPI MpScanControl(
  _In_ MPHANDLE  hScanHandle,
  _In_ MPCONTROL ScanControl
);
```



## Parameters

<dl> <dt>

*hScanHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to an asynchronous scan operation. This handle is returned by the [**MpScanStart**](mpscanstart.md) function. This parameter can also be set to the malware protection manager interface handle returned by [**MpManagerOpen**](mpmanageropen.md) function to control a system initiated scan, in which case the caller must have administrative privilege.

</dd> <dt>

*ScanControl* \[in\]
</dt> <dd>

Type: **MPCONTROL**

Specifies a scan control option. This parameter must be one of the following control options:



| Value                                                                                                                                                                  | Meaning                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <span id="MPCONTROL_ABORT"></span><span id="mpcontrol_abort"></span><dl> <dt>**MPCONTROL\_ABORT**</dt> </dl>    | Abort the scan operation.<br/>         |
| <span id="MPCONTROL_PAUSE"></span><span id="mpcontrol_pause"></span><dl> <dt>**MPCONTROL\_PAUSE**</dt> </dl>    | Pause the scan operation.<br/>         |
| <span id="MPCONTROL_RESUME"></span><span id="mpcontrol_resume"></span><dl> <dt>**MPCONTROL\_RESUME**</dt> </dl> | Resume the paused scan operation.<br/> |



 

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

[**MpManagerOpen**](mpmanageropen.md)
</dt> <dt>

[**MpScanStart**](mpscanstart.md)
</dt> </dl>

 

 





