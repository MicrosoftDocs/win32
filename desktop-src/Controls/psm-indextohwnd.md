---
title: PSM_INDEXTOHWND message (Prsht.h)
description: Takes the index of a property sheet page and returns its window handle. You can send this message explicitly or use the PropSheet\_IndexToHwnd macro.
ms.assetid: 93b46b4c-47f9-4ce8-8797-f3d4bd5248e9
keywords:
- PSM_INDEXTOHWND message Windows Controls
topic_type:
- apiref
api_name:
- PSM_INDEXTOHWND
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_INDEXTOHWND message

Takes the index of a property sheet page and returns its window handle. You can send this message explicitly or use the [**PropSheet\_IndexToHwnd**](/windows/desktop/api/Prsht/nf-prsht-propsheet_indextohwnd) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the page.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns the handle to the window of the property sheet page specified by *wParam* if successful. Otherwise, it returns zero.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





