---
description: In the presence of WIP policy, outputs a Boolean indicating whether the current contents of the clipboard were set by an enlightened application. 
title: EdpGetSourceIsEnlightenedForClipboard function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpGetSourceIsEnlightenedForClipboard
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpGetSourceIsEnlightenedForClipboard function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, outputs a Boolean indicating whether the current contents of the clipboard were set by an enlightened application. 

## Syntax


```C++
HRESULT EdpGetSourceIsEnlightenedForClipboard(
    _Out_ BOOL* IsEnlightened
    );
```



## Parameters

### IsEnlightened

Set to **TRUE** if the application is enlightened; otherwise, **FALSE**.

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



 

 




