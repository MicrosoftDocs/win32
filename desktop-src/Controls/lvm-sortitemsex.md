---
title: LVM_SORTITEMSEX message (Commctrl.h)
description: Uses an application-defined comparison function to sort the items of a list-view control. The index of each item changes to reflect the new sequence. You can send this message explicitly or by using the ListView\_SortItemsEx macro.
ms.assetid: eab2f6f5-68fd-4cb6-acf4-cb267ee40fdc
keywords:
- LVM_SORTITEMSEX message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SORTITEMSEX
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SORTITEMSEX message

Uses an application-defined comparison function to sort the items of a list-view control. The index of each item changes to reflect the new sequence. You can send this message explicitly or by using the [**ListView\_SortItemsEx**](/windows/desktop/api/Commctrl/nf-commctrl-listview_sortitemsex) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Application-defined value that is passed to the comparison function.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an application-defined comparison function. It is called during the sort operation each time the relative order of two list items needs to be compared.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The comparison function has the following form:

``` syntax
int CALLBACK CompareFunc(LPARAM lParam1, LPARAM lParam2, LPARAM lParamSort);  
```

This message is similar to [**LVM\_SORTITEMS**](lvm-sortitems.md), except for the type of information passed to the comparison function. With **LVM\_SORTITEMSEX**, *lParam1* is the current index of the first item, and *lParam2* is the current index of the second item. You can send an [**LVM\_GETITEMTEXT**](lvm-getitemtext.md) message to retrieve more information on an item, if needed.

The comparison function must return a negative value if the first item should precede the second, a positive value if the first item should follow the second, or zero if the two items are equivalent.

> [!Note]  
> During the sorting process, the list-view contents are unstable. If the callback function sends any messages to the list-view control aside from [**LVM\_GETITEM**](lvm-getitem.md) ([**ListView\_GetItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitem)), the results are unpredictable.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





