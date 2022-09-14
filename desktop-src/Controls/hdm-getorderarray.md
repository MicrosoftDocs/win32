---
title: HDM_GETORDERARRAY message (Commctrl.h)
description: Gets the current left-to-right order of items in a header control. You can send this message explicitly or use the Header\_GetOrderArray macro.
ms.assetid: b287d3c1-ae61-41a4-a884-dc008eb24ad8
keywords:
- HDM_GETORDERARRAY message Windows Controls
topic_type:
- apiref
api_name:
- HDM_GETORDERARRAY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_GETORDERARRAY message

Gets the current left-to-right order of items in a header control. You can send this message explicitly or use the [**Header\_GetOrderArray**](/windows/desktop/api/Commctrl/nf-commctrl-header_getorderarray) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The number of integer elements that *lParam* can hold. This value must be equal to the number of items in the control (see [**HDM\_GETITEMCOUNT**](hdm-getitemcount.md)).

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an array of integers that receive the index values for items in the header.

</dd> </dl>

## Return value

Returns nonzero if successful, and the buffer at *lParam* receives the item number for each item in the header control in the order in which they appear from left to right. Otherwise, the message returns zero.

## Remarks

The number of elements in *lParam* is specified in *wParam* and must be equal to the number of items in the control. For example, the following code fragment will reserve enough memory to hold the index values.


```
int iItems,

    *lpiArray;



// Get memory for buffer.

(iItems = SendMessage(hwndHD, HDM_GETITEMCOUNT, 0,0))!=-1)

    if(!(lpiArray = calloc(iItems,sizeof(int))))

MessageBox(hwnd, "Out of memory.","Error", MB_OK);
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





