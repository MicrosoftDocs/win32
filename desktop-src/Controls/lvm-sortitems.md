---
title: LVM_SORTITEMS message (Commctrl.h)
description: Uses an application-defined comparison function to sort the items of a list-view control. The index of each item changes to reflect the new sequence. You can send this message explicitly or by using the ListView\_SortItems macro.
ms.assetid: ed3d5cec-69af-49a1-9cb7-eb5da1163071
keywords:
- LVM_SORTITEMS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SORTITEMS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SORTITEMS message

Uses an application-defined comparison function to sort the items of a list-view control. The index of each item changes to reflect the new sequence. You can send this message explicitly or by using the [**ListView\_SortItems**](/windows/desktop/api/Commctrl/nf-commctrl-listview_sortitems) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Application-defined value that is passed to the comparison function.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the application-defined comparison function. The comparison function is called during the sort operation each time the relative order of two list items needs to be compared.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The comparison function has the following form:

``` syntax
int CALLBACK CompareFunc(LPARAM lParam1, LPARAM lParam2, LPARAM lParamSort);
```

The *lParam1* parameter is the value associated with the first item being compared, and the *lParam2* parameter is the value associated with the second item. These are the values that were specified in the **lParam** member of the items' [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure when they were inserted into the list. The [**ListView\_SortItems**](/windows/desktop/api/Commctrl/nf-commctrl-listview_sortitems)'s *wParam* parameter is passed to the callback function as its third parameter.

The comparison function must return a negative value if the first item should precede the second, a positive value if the first item should follow the second, or zero if the two items are equivalent.

> [!Note]  
> During the sorting process, the list-view contents are unstable. If the callback function sends any messages to the list-view control aside from [**LVM\_GETITEM**](lvm-getitem.md) ([**ListView\_GetItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitem)), the results are unpredictable.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





