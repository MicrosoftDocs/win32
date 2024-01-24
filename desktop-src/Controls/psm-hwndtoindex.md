---
title: PSM_HWNDTOINDEX message (Prsht.h)
description: Takes the window handle of the property sheet page and returns its zero-based index. You can send this message explicitly or use the PropSheet\_HwndToIndex macro.
ms.assetid: 'vs|controls|~\controls\propsheet\messages\psm_hwndtoindex.htm'
keywords:
- PSM_HWNDTOINDEX message Windows Controls
topic_type:
- apiref
api_name:
- PSM_HWNDTOINDEX
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_HWNDTOINDEX message

Takes the window handle of the property sheet page and returns its zero-based index. You can send this message explicitly or use the [**PropSheet\_HwndToIndex**](/windows/desktop/api/Prsht/nf-prsht-propsheet_hwndtoindex) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the page's window.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns the zero-based index of the property sheet page specified by *wParam* if successful. Otherwise, it returns -1.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





