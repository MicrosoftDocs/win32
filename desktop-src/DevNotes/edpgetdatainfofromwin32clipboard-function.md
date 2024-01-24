---
description: In the presence of WIP policy, generates a string with format information about the data contained in the Win32 clipboard. 
title: EdpGetDataInfoFromWin32Clipboard function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpGetDataInfoFromWin32Clipboard
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpGetDataInfoFromWin32Clipboard function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, generates a string with format information about the data contained in the Win32 clipboard. 

## Syntax


```C++
HRESULT EdpGetDataInfoFromWin32Clipboard(
    _Outptr_result_z_ PWSTR* dataInfo
    );

```

## Parameters

### dataInfo

A string with concatenated format tokens. Possible format names are "Image", "Text", "Audio" and "Other".

## Return value

An HRESULT value.

## Remarks

The information returned by this function relates to the data used by [SetClipboardData](/windows/win32/api/winuser/nf-winuser-setclipboarddata) and [GetClipboardData](/windows/win32/api/winuser/nf-winuser-getclipboarddata). For example if the clipboard contains image and text, dataInfo will contain “Image | Text”. 

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |



 

 




