---
title: CB_SHOWDROPDOWN message (Winuser.h)
description: An application sends a CB\_SHOWDROPDOWN message to show or hide the list box of a combo box that has the CBS\_DROPDOWN or CBS\_DROPDOWNLIST style.
ms.assetid: 32b995d7-eed6-4173-8525-0d356dea39b3
keywords:
- CB_SHOWDROPDOWN message Windows Controls
topic_type:
- apiref
api_name:
- CB_SHOWDROPDOWN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SHOWDROPDOWN message

An application sends a **CB\_SHOWDROPDOWN** message to show or hide the list box of a combo box that has the [**CBS\_DROPDOWN**](combo-box-styles.md) or [**CBS\_DROPDOWNLIST**](combo-box-styles.md) style.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **BOOL** that specifies whether the drop-down list box is to be shown or hidden. A value of **TRUE** shows the list box; a value of **FALSE** hides it.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is always **TRUE**.

## Remarks

This message has no effect on a combo box created with the [**CBS\_SIMPLE**](combo-box-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_GETDROPPEDSTATE**](cb-getdroppedstate.md)
</dt> </dl>

 

 





