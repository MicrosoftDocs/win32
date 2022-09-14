---
title: MpThreatEnumerate function (MpClient.h)
description: Returns information about the next threat in the enumeration list. This function can be called repeatedly until the enumeration of all the threats is complete.
ms.assetid: 33244F4F-4FB7-4FA7-BC56-B9A30ABC3644
keywords:
- MpThreatEnumerate function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpThreatEnumerate
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpThreatEnumerate function

Returns information about the next threat in the enumeration list. This function can be called repeatedly until the enumeration of all the threats is complete.

## Syntax


```C++
HRESULT WINAPI MpThreatEnumerate(
  _In_  MPHANDLE       hThreatEnumHandle,
  _Out_ PMPTHREAT_INFO *ppThreatInfo
);
```



## Parameters

<dl> <dt>

*hThreatEnumHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to a threat enumeration context returned by [**MpThreatOpen**](mpthreatopen.md).

</dd> <dt>

*ppThreatInfo* \[out\]
</dt> <dd>

Type: **PMPTHREAT\_INFO\***

Returns a pointer to a threat information structure, [**MPTHREAT\_INFO**](mpthreat-info.md). The structure contains information such as threat id, name, and severity.

</dd> </dl>

## Return value

Type: **HRESULT**

If the function succeeds the return value is **S\_OK**.

If there are no more items to return the return value is **S\_FALSE**.

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

[**MpThreatOpen**](mpthreatopen.md)
</dt> <dt>

[**MPTHREAT\_INFO**](mpthreat-info.md)
</dt> </dl>

 

 





