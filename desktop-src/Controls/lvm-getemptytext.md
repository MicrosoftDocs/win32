---
title: LVM_GETEMPTYTEXT message (Commctrl.h)
description: Gets the text meant for display when the list-view control appears empty. Send this message explicitly or by using the ListView\_GetEmptyText macro.
ms.assetid: aa6cb0ae-0c6c-42b7-80c5-c086c9579c81
keywords:
- LVM_GETEMPTYTEXT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETEMPTYTEXT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETEMPTYTEXT message

Gets the text meant for display when the list-view control appears empty. Send this message explicitly or by using the [**ListView\_GetEmptyText**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getemptytext) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The size of the buffer pointed to by *lParam*, including the terminating **NULL**.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a null-terminated, Unicode buffer of size specified by *wParam* to receive the text. The caller is responsible for allocating the buffer.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





