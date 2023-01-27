---
description: Frees the EDP_CONTEXT retrieved from EdpGetContextForProcess.
title: EdpFreeContext function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpFreeContext
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpFreeContext function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


Frees the [EDP_CONTEXT](edp_context_structure.md) retrieved from [EdpGetContextForProcess](edpgetcontextforprocess-function.md).

## Syntax


```C++
VOID
EdpFreeContext(
    _In_opt_ EDP_CONTEXT* context
    );
```



## Parameters

### context

Context retrieved from **EdpGetContextForProcess**.

## Return value

Void.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |



 

 




