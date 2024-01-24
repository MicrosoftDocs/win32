---
title: MpThreatQuery function (MpClient.h)
description: Used to query static (such as severity and category) or localized (such as category description and advice) information about a particular threat.
ms.assetid: A06854B2-8444-46A4-A53F-FD5FEAFF47B7
keywords:
- MpThreatQuery function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpThreatQuery
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpThreatQuery function

Used to query static (such as severity and category) or localized (such as category description and advice) information about a particular threat.

## Syntax


```C++
HRESULT WINAPI MpThreatQuery(
  _In_      MPHANDLE                 hMpHandle,
  _In_      MPTHREAT_ID              ThreatID,
  _Out_     PMPTHREAT_INFO           *ppThreatInfo,
  _Out_opt_ PMPTHREAT_LOCALIZED_INFO *ppThreatLocalizedInfo
);
```



## Parameters

<dl> <dt>

*hMpHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to the malware protection manager interface. This handle is returned by the [**MpManagerOpen**](mpmanageropen.md) function.

</dd> <dt>

*ThreatID* \[in\]
</dt> <dd>

Type: **MPTHREAT\_ID**

Threat identifier for which information is requested.

</dd> <dt>

*ppThreatInfo* \[out\]
</dt> <dd>

Type: **PMPTHREAT\_INFO\***

Returns a pointer to a threat information structure, [**MPTHREAT\_INFO**](mpthreat-info.md). The structure contains information such as threat id, name, and severity.

</dd> <dt>

*ppThreatLocalizedInfo* \[out, optional\]
</dt> <dd>

Type: **PMPTHREAT\_LOCALIZED\_INFO\***

Returns a pointer to a structure containing localized information about the threat. You can pass **NULL** if you are not interested in localized information about the threat. See [**MPTHREAT\_LOCALIZED\_INFO**](mpthreat-localized-info.md).

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

[**MPTHREAT\_INFO**](mpthreat-info.md)
</dt> <dt>

[**MPTHREAT\_LOCALIZED\_INFO**](mpthreat-localized-info.md)
</dt> </dl>

 

 





