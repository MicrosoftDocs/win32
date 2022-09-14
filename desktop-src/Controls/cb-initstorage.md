---
title: CB_INITSTORAGE message (Winuser.h)
description: An application sends the CB\_INITSTORAGE message before adding a large number of items to the list box portion of a combo box. This message allocates memory for storing list box items.
ms.assetid: fb289968-a95b-4ca0-977d-b8651166f357
keywords:
- CB_INITSTORAGE message Windows Controls
topic_type:
- apiref
api_name:
- CB_INITSTORAGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_INITSTORAGE message

An application sends the **CB\_INITSTORAGE** message before adding a large number of items to the list box portion of a combo box. This message allocates memory for storing list box items.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The number of items to add.

</dd> <dt>

*lParam* 
</dt> <dd>

The amount of memory to allocate for item strings, in bytes.

</dd> </dl>

## Return value

If the message is successful, the return value is the total number of items for which memory has been pre-allocated, that is, the total number of items added by all successful **CB\_INITSTORAGE** messages.

If the message fails, the return value is CB\_ERRSPACE.

The message allocates memory and returns the success and error values described above.

## Remarks

The **CB\_INITSTORAGE** message helps speed up the initialization of combo boxes that have a large number of items (over 100). It reserves the specified amount of memory so that subsequent [**CB\_ADDSTRING**](cb-addstring.md), [**CB\_INSERTSTRING**](cb-insertstring.md), and [**CB\_DIR**](cb-dir.md) messages take the shortest possible time. You can use estimates for the *wParam* and *lParam* parameters. If you overestimate, the extra memory is allocated, if you underestimate, the normal allocation is used for items that exceed the requested amount.

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

[**CB\_DIR**](cb-dir.md)
</dt> <dt>

[**CB\_INSERTSTRING**](cb-insertstring.md)
</dt> </dl>

 

 





