---
title: EM_SETFONTSIZE message (Richedit.h)
description: Sets the font size for the selected text in a rich edit control.
ms.assetid: 18d91370-12c0-4e5f-a0e9-ffde02abc966
keywords:
- EM_SETFONTSIZE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETFONTSIZE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETFONTSIZE message

Sets the font size for the selected text in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Change in point size of the selected text. The result will be rounded according to values shown in the following table. This parameter should be in the range of -1637 to 1638. The resulting font size will be within the range of 1 to 1638.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

If no error occurred, the return value is **TRUE**.

If an error occurred, the return value is **FALSE**.

## Remarks

You can easily get the font size by sending the [**EM\_GETCHARFORMAT**](em-getcharformat.md) message.

Rich Edit first adds *wParam* to the current font size and then uses the resulting size and the following table to determine the rounding value.



| Band    | Rounding value |
|---------|----------------|
| <=12 | 1              |
| 28      | 2              |
| 36      | 0              |
| 48      | 0              |
| 72      | 0              |
| 80      | 0              |
| > 80 | 10             |



 

If the resulting font size is not evenly divisible by the rounding value, the font size is then rounded to a number evenly divisible by the rounding value. So if the font size is less than or equal to 12, the rounding value will be 1. Similarly, if the font size is less than or equal to 28, the rounding value is 2. For values greater than 28, font sizes are rounded to the next band. So, the font size jumps to 36, 48, 72, 80. After 80, all rounding is done in increments of ten points.

The font size is rounded up or down depending on the sign of *wParam*. If *wParam* is positive, the rounding is always up. Otherwise, rounding is always down. So, if the current font size is 10 and *wParam* is 3, the resulting font size would be 14 (10 + 3 = 13, which is not divisible by 2, so the size rounds up to 14). Conversely, if the current font size is 14 and *wParam* is -3, the resulting font size would be 10 (14 - 3 = 11, which is not divisible by 2, so the size rounds down to 10).

The change is applied to each part of the selection. So, if some of the text is 10pt and some 20pt, after a call with *wParam* set to 1, the font sizes become 11pt and 22pt, respectively.

Additional examples are shown in the following table.



| Original font size | *wParam* | Resulting font size |
|--------------------|----------|---------------------|
| 7                  | 1        | 8                   |
| 7                  | 3        | 10                  |
| 10                 | 3        | 14                  |
| 14                 | -3       | 10                  |
| 28                 | 1        | 36                  |
| 28                 | 3        | 36                  |
| 80                 | 1        | 90                  |
| 80                 | -1       | 72                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_GETCHARFORMAT**](em-getcharformat.md)
</dt> <dt>

[**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Rich Edit Controls](about-rich-edit-controls.md)
</dt> </dl>

 

 





