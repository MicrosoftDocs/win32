---
title: EM_GETCUEBANNER message (Commctrl.h)
description: Gets the text that is displayed as the textual cue, or tip, in an edit control.
ms.assetid: 311b783a-cd78-440f-bfc2-f5108ae7d1f8
keywords:
- EM_GETCUEBANNER message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETCUEBANNER
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETCUEBANNER message

Gets the text that is displayed as the textual cue, or tip, in an edit control.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A pointer to a Unicode buffer that receives the text set as the textual cue. The caller is responsible for allocating the buffer.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

The size of the buffer pointed to by *wParam* in **WCHARs**, including the terminating **NULL**.

</dd> </dl>

## Return value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**Edit\_GetCueBannerText**](/windows/desktop/api/Commctrl/nf-commctrl-edit_getcuebannertext)
</dt> </dl>

 

 





