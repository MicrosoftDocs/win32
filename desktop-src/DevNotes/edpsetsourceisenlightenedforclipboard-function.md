---
description: In the presence of WIP policy, this API can be used to indicate to the clipboard that the application performing the copy is a WIP enlightened application.
title: EdpSetSourceIsEnlightenedForClipboard function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpSetSourceIsEnlightenedForClipboard
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpSetSourceIsEnlightenedForClipboard function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, this API can be used to indicate to the clipboard that the application performing the copy is a WIP enlightened application.

## Syntax


```C++
HRESULT EdpSetSourceIsEnlightenedForClipboard(
    _In_ BOOL IsEnlightened
    );

```



## Parameters

### IsEnlightened

**TRUE** if the application is enlightened; otherwise, **FALSE**.

## Return value

An HRESULT value.

## Remarks

For more information on enlightened apps, see [List of enlightened Microsoft apps for use with Windows Information Protection (WIP)](/windows/security/information-protection/windows-information-protection/enlightened-microsoft-apps-and-wip).


## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |



 

 




