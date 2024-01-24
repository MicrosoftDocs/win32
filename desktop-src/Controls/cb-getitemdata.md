---
title: CB_GETITEMDATA message (Winuser.h)
description: An application sends a CB\_GETITEMDATA message to a combo box to retrieve the application-supplied value associated with the specified item in the combo box.
ms.assetid: 433b7f75-2831-4919-b931-c17ba651d145
keywords:
- CB_GETITEMDATA message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETITEMDATA
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETITEMDATA message

An application sends a **CB\_GETITEMDATA** message to a combo box to retrieve the application-supplied value associated with the specified item in the combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the item.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the value associated with the item. If an error occurs, it is CB\_ERR.

If the item is in an owner-drawn combo box created without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the return value is the value contained in the *lParam* parameter of the [**CB\_ADDSTRING**](cb-addstring.md) or [**CB\_INSERTSTRING**](cb-insertstring.md) message, that added the item to the combo box. If the **CBS\_HASSTRINGS** style was not used, the return value is the *lParam* parameter contained in a [**CB\_SETITEMDATA**](cb-setitemdata.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CB\_ADDSTRING**](cb-addstring.md)
</dt> <dt>

[**CB\_INSERTSTRING**](cb-insertstring.md)
</dt> <dt>

[**CB\_SETITEMDATA**](cb-setitemdata.md)
</dt> </dl>

 

 





