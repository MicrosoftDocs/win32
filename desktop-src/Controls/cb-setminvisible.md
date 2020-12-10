---
title: CB_SETMINVISIBLE message (Commctrl.h)
description: An application sends a CB\_SETMINVISIBLE message to set the minimum number of visible items in the drop-down list of a combo box.
ms.assetid: 3cf9e488-50ce-4825-acf0-4e665d074f9e
keywords:
- CB_SETMINVISIBLE message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETMINVISIBLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETMINVISIBLE message

An application sends a **CB\_SETMINVISIBLE** message to set the minimum number of visible items in the drop-down list of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the minimum number of visible items.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

If the message is successful, the return value is **TRUE**. Otherwise the return value is **FALSE**.

## Remarks

When the number of items in the drop-down list is greater than the minimum, the combo box uses a scroll bar. By default, 30 is the minimum number of visible items.

This message is ignored if the combo box control has style [**CBS\_NOINTEGRALHEIGHT**](combo-box-styles.md).

To use **CB\_SETMINVISIBLE**, the application must specify comctl32.dll version 6 in the manifest. For more information, see [Enabling Visual Styles](cookbook-overview.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CB\_GETMINVISIBLE**](cb-getminvisible.md)
</dt> <dt>

[**ComboBox\_SetMinVisible**](/windows/desktop/api/Commctrl/nf-commctrl-combobox_setminvisible)
</dt> </dl>

 

 





