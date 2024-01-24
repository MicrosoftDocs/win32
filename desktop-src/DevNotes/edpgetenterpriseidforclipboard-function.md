---
description: In the presence of WIP policy, get the WIP enterprise ID for the data currently present in clipboard. 
title: EdpGetEnterpriseIdForClipboard function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpGetEnterpriseIdForClipboard
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpGetEnterpriseIdForClipboard function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, get the WIP enterprise ID for the data currently present in clipboard. 

## Syntax


```C++
HRESULT EdpGetEnterpriseIdForClipboard(
    _Outptr_result_maybenull_ PWSTR* enterpriseId
    );
```



## Parameters

### enterpriseId

Recevies a pointer to the enterprise ID if the data is enterprise. Otherwise the value will is NULL. Must be freed with [HeapFree](/windows/win32/api/heapapi/nf-heapapi-heapfree).

## Return value

An HRESULT value.

## Remarks


## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |


 

 




