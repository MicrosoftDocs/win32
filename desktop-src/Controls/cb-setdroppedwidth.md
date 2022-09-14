---
title: CB_SETDROPPEDWIDTH message (Winuser.h)
description: An application sends the CB\_SETDROPPEDWIDTH message to set the minimum allowable width, in pixels, of the list box of a combo box with the CBS\_DROPDOWN or CBS\_DROPDOWNLIST style.
ms.assetid: 89f44733-aebe-44ea-b62d-8bd988f1bd6f
keywords:
- CB_SETDROPPEDWIDTH message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETDROPPEDWIDTH
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETDROPPEDWIDTH message

An application sends the **CB\_SETDROPPEDWIDTH** message to set the minimum allowable width, in pixels, of the list box of a combo box with the [**CBS\_DROPDOWN**](combo-box-styles.md) or [**CBS\_DROPDOWNLIST**](combo-box-styles.md) style.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The minimum allowable width of the list box, in pixels.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the message is successful, The return value is the new width of the list box.

If the message fails, the return value is CB\_ERR.

## Remarks

By default, the minimum allowable width of the drop-down list box is zero. The width of the list box is either the minimum allowable width or the combo box width, whichever is larger.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_GETDROPPEDWIDTH**](cb-getdroppedwidth.md)
</dt> </dl>

 

 





