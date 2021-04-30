---
title: MpManagerStatusQueryEx function (MpClient.h)
description: Returns status information about various components of the malware protection manager. | MpManagerStatusQueryEx function (MpClient.h)
ms.assetid: 98088AB9-C7CF-46A1-B444-2C0EF882AA66
keywords:
- MpManagerStatusQueryEx function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpManagerStatusQueryEx
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpManagerStatusQueryEx function

Returns status information about various components of the malware protection manager.

## Syntax


```C++
HRESULT WINAPI MpManagerStatusQueryEx(
  _In_  MPHANDLE       hMpHandle,
  _In_  DWORD          dwFlag,
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

*dwFlag* \[in\]
</dt> <dd>

Type: **DWORD**

Controls which query information is returned. Some information is expensive and may not be needed.



| Value                                                                                                                                                                                                         | Meaning                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <span id="MP_STATUS_QUERY_FLAGS_NONE"></span><span id="mp_status_query_flags_none"></span><dl> <dt>**MP\_STATUS\_QUERY\_FLAGS\_NONE**</dt> </dl>       | Default.<br/>                            |
| <span id="MP_STATUS_QUERY_FLAG_NOSTATE"></span><span id="mp_status_query_flag_nostate"></span><dl> <dt>**MP\_STATUS\_QUERY\_FLAG\_NOSTATE**</dt> </dl> | Do not query for state information.<br/> |



 

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

[**MPSTATUS\_INFO**](mpstatus-info.md)
</dt> </dl>

 

 





