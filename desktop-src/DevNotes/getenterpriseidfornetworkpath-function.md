---
description: In the presence of WIP policy, returns the WIP enterprise ID associated with a file or folder on a network share.
title: GetEnterpriseIdForNetworkPath function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetEnterpriseIdForNetworkPath
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# GetEnterpriseIdForNetworkPath function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, returns the WIP enterprise ID associated with a file or folder on a network share.

## Syntax


```C++
HRESULT GetEnterpriseIdForNetworkPath(
    _In_ PCWSTR networkPath,
    _Outptr_result_maybenull_ PWSTR* identity,
    _Out_ bool* isNetworkFile
    );
```

## Parameters

### networkPath

Full path to the file or folder. For example, `\\server\share\example.txt`.

### identity

Receives the enterprise ID of the file or folder. This is NULL if the file or folder is not a network file, or if the file or folder is not on an enterprise network share.

### isNetworkFile

Set to **TRUE** if the file is on a network share.

## Return value

An HRESULT value.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |



 

 




