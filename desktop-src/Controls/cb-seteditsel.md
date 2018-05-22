---
title: CB\_SETEDITSEL message
description: An application sends a CB\_SETEDITSEL message to select characters in the edit control of a combo box.
ms.assetid: '25a07341-a21c-42a9-a220-62650997757b'
keywords: ["CB_SETEDITSEL message Windows Controls"]
topic_type:
- apiref
api_name:
- CB_SETEDITSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# CB\_SETEDITSEL message

An application sends a **CB\_SETEDITSEL** message to select characters in the edit control of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) of *lParam* specifies the starting position. If the **LOWORD** is –1, the selection, if any, is removed.

The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) of *lParam* specifies the ending position. If the **HIWORD** is –1, all text from the starting position to the last character in the edit control is selected.

</dd> </dl>

## Return value

If the message succeeds, the return value is **TRUE**. If the message is sent to a combo box with the [**CBS\_DROPDOWNLIST**](combo-box-styles.md#cbs-dropdownlist) style, it is CB\_ERR.

## Remarks

The positions are zero-based. The first character of the edit control is in the zero position. The first character after the last selected character is in the ending position. For example, to select the first four characters of the edit control, use a starting position of 0 and an ending position of 4.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CB\_GETEDITSEL**](cb-geteditsel.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKELPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632661)
</dt> </dl>

 

 





