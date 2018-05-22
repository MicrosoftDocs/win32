---
title: LVM\_GETEXTENDEDLISTVIEWSTYLE message
description: Gets the extended styles that are currently in use for a given list-view control. You can send this message explicitly or use the ListView\_GetExtendedListViewStyle macro.
ms.assetid: '5cfccdb8-a81c-4fa9-a4fa-19cf49bd6ce0'
keywords: ["LVM_GETEXTENDEDLISTVIEWSTYLE message Windows Controls"]
topic_type:
- apiref
api_name:
- LVM_GETEXTENDEDLISTVIEWSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# LVM\_GETEXTENDEDLISTVIEWSTYLE message

Gets the extended styles that are currently in use for a given list-view control. You can send this message explicitly or use the [**ListView\_GetExtendedListViewStyle**](listview-getextendedlistviewstyle.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **DWORD** that represents the styles currently in use for a given list-view control. This value can be a combination of [Extended List-View Styles](extended-list-view-styles.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





