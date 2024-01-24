---
title: CB_GETCUEBANNER message (Winuser.h)
description: Gets the cue banner text displayed in the edit control of a combo box. Send this message explicitly or by using the ComboBox\_GetCueBannerText macro.
ms.assetid: 38959228-9f07-4636-a1ea-681efe77b9ec
keywords:
- CB_GETCUEBANNER message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETCUEBANNER
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETCUEBANNER message

Gets the cue banner text displayed in the edit control of a combo box. Send this message explicitly or by using the [**ComboBox\_GetCueBannerText**](/windows/desktop/api/Commctrl/nf-commctrl-combobox_getcuebannertext) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A pointer to a Unicode string buffer that receives the cue banner text. The calling application is responsible for allocating the memory for the buffer. The buffer size must be equal to the length of the cue banner string in **WCHARs**, plus 1 for the terminating **NULL** **WCHAR**.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

The size of the buffer pointed to by *lpcwText* in **WCHARs**.

</dd> </dl>

## Return value

Returns 1 if successful, or an error value otherwise.

If there is no cue banner text to get, the return value is 0. If the calling application fails to allocate a buffer, or set *lParam* before sending this message, undefined behavior may result and the return value may not be reliable.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

[Combo Box Features](combo-box-features.md)
</dt> </dl>

 

 





