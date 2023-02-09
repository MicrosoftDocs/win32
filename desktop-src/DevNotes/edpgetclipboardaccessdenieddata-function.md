---
description: In the presence of WIP policy, returns an ‘access denied’ message dependent on the format provided.  
title: EdpGetClipboardAccessDeniedData function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpGetClipboardAccessDeniedData
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpGetClipboardAccessDeniedData function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, returns an ‘access denied’ message dependent on the format provided. 

## Syntax


```C++
STDAPI
EdpGetClipboardAccessDeniedData(
    _In_ UINT formatId,
    _Outptr_ HANDLE* data
    );


```

## Parameters

### formatId

Clipboard data format. **CF_TEXT**, **CF_OEMTEXT**, **CF_UNICODETEXT**, and **CF_BITMAP** are supported. For more information, see [Standard Clipboard Formats](/windows/win32/dataxchg/standard-clipboard-formats).

### data

For **CF_TEXT**, **CF_OEMTEXT** and **CF_UNICODETEXT**, this is a **PWSTR**. For **CF_BITMAP**, this is an HBITMAP, as obtained from a call to [LoadBitmap](/windows/win32/api/winuser/nf-winuser-loadbitmapw). This must not be freed.

## Return value

An HRESULT value.

## Remarks

This function can be used by WIP enlightened applications to show the user that copying data from enterprise personal is not permitted under the WIP policy.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |



 

 




