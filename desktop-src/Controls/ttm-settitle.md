---
title: TTM_SETTITLE message (Commctrl.h)
description: Adds a standard icon and title string to a tooltip.
ms.assetid: e745a592-eef7-4e0d-8939-a48b52c4ab9f
keywords:
- TTM_SETTITLE message Windows Controls
topic_type:
- apiref
api_name:
- TTM_SETTITLE
- TTM_SETTITLEA
- TTM_SETTITLEW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_SETTITLE message

Adds a standard icon and title string to a tooltip.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Set *wParam* to one of the following values to specify the icon to be displayed. As of Windows XP SP2 and later, this parameter can also contain an **HICON** value. Any value greater than TTI\_ERROR is assumed to be an **HICON**.



| Value                                                                                                                                                                      | Meaning                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="TTI_NONE"></span><span id="tti_none"></span><dl> <dt>**TTI\_NONE**</dt> </dl>                             | No icon.<br/>         |
| <span id="TTI_INFO"></span><span id="tti_info"></span><dl> <dt>**TTI\_INFO**</dt> </dl>                             | Info icon.<br/>       |
| <span id="TTI_WARNING"></span><span id="tti_warning"></span><dl> <dt>**TTI\_WARNING**</dt> </dl>                    | Warning icon<br/>     |
| <span id="TTI_ERROR"></span><span id="tti_error"></span><dl> <dt>**TTI\_ERROR**</dt> </dl>                          | Error Icon<br/>       |
| <span id="TTI_INFO_LARGE"></span><span id="tti_info_large"></span><dl> <dt>**TTI\_INFO\_LARGE**</dt> </dl>          | Large error Icon<br/> |
| <span id="TTI_WARNING_LARGE"></span><span id="tti_warning_large"></span><dl> <dt>**TTI\_WARNING\_LARGE**</dt> </dl> | Large error Icon<br/> |
| <span id="TTI_ERROR_LARGE"></span><span id="tti_error_large"></span><dl> <dt>**TTI\_ERROR\_LARGE**</dt> </dl>       | Large error Icon<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the title string. You must assign a value to *lParam*.

</dd> </dl>

## Return value

Returns **TRUE** if successful, **FALSE** if not.

## Remarks

The title of a tooltip appears above the text, in a different font. It is not sufficient to have a title; the tooltip must have text as well, or it is not displayed.

When *wParam* contains an **HICON**, a copy of the icon is created by the tooltip window.

When calling **TTM\_SETTITLE**, the string pointed to by *lParam* must not exceed 100 **TCHARs** in length, including the terminating **NULL**.

## Examples

The following example shows how to add a title and a system icon to a tooltip.


```C++
// hwndTip is the handle of the tooltip window.
HICON hIcon = LoadIcon(NULL, IDI_INFORMATION);
SendMessage(hwndTip, TTM_SETTITLE, (WPARAM)hIcon, L"Title text");
DestroyIcon(hIcon);
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_SETTITLEW** (Unicode) and **TTM\_SETTITLEA** (ANSI)<br/>                 |



## See also

<dl> <dt>

[About Tooltip Controls](tooltip-controls.md)
</dt> </dl>

 

 





