---
title: CB_SETITEMDATA message (Winuser.h)
description: An application sends a CB\_SETITEMDATA message to set the value associated with the specified item in a combo box.
ms.assetid: 8be9eb57-a635-4c52-9838-556368813c74
keywords:
- CB_SETITEMDATA message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETITEMDATA
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETITEMDATA message

An application sends a **CB\_SETITEMDATA** message to set the value associated with the specified item in a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the item's zero-based index.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the new value to be associated with the item.

</dd> </dl>

## Return value

If an error occurs, the return value is CB\_ERR.

## Remarks

If the specified item is in an owner-drawn combo box created without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, this message replaces the value in the *lParam* parameter of the [**CB\_ADDSTRING**](cb-addstring.md) or [**CB\_INSERTSTRING**](cb-insertstring.md) message that added the item to the combo box.

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

[**CB\_GETITEMDATA**](cb-getitemdata.md)
</dt> <dt>

[**CB\_INSERTSTRING**](cb-insertstring.md)
</dt> </dl>

 

 





