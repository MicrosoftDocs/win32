---
description: In the presence of WIP policy, get the WIP primary identities for all users on the device.
title: EdpGetPrimaryIdentities function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpGetPrimaryIdentities
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpGetPrimaryIdentities function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, get the WIP primary identities for all users on the device. 

## Syntax


```C++
HRESULT
EdpGetPrimaryIdentities(
    _Outptr_result_buffer_(*NumIdentities) PWSTR **Identities,
    _Out_ DWORD *NumIdentities
    );
```



## Parameters

### Identities 

Returned list of identities.

### NumIdentities

Returned count of identities in *Identities*.


## Return value

An HRESULT value.

## Remarks

The retrieved identities are the primary internet domains (such as contoso.com) that identify and tag enterprise data.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |



 

 




