---
title: MpManagerStatusQuery function (MpClient.h)
description: Returns status information about various components of the malware protection manager. | MpManagerStatusQuery function (MpClient.h)
ms.assetid: E993FD8B-A35D-41C1-9522-1B9F0BC10B3D
keywords:
- MpManagerStatusQuery function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpManagerStatusQuery
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpManagerStatusQuery function

\[**MpManagerStatusQuery** is not supported and may be altered or unavailable in the future. Instead, use [**MpManagerStatusQueryEx**](mpmanagerstatusqueryex.md).\]

Returns status information about various components of the malware protection manager.

## Syntax


```C++
HRESULT WINAPI MpManagerStatusQuery(
  _In_  MPHANDLE       hMpHandle,
  _Out_ PMPSTATUS_INFO pStatusInfo
);
```



## Parameters

<dl> <dt>

*hMpHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to the malware protection manager interface. This handle is returned by the [**MpManagerOpen**](mpmanageropen.md) function.

</dd> <dt>

*pStatusInfo* \[out\]
</dt> <dd>

Type: **PMPSTATUS\_INFO**

Pointer to a structure that returns status information regarding last scans, active threats and various component status. See [**MPSTATUS\_INFO**](mpstatus-info.md).

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

[**MpManagerOpen**](mpmanageropen.md)
</dt> <dt>

[**MpManagerStatusQueryEx**](mpmanagerstatusqueryex.md)
</dt> <dt>

[**MPSTATUS\_INFO**](mpstatus-info.md)
</dt> </dl>

 

 





