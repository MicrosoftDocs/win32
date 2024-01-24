---
title: PSM_INDEXTOID message (Prsht.h)
description: Takes the index of a property sheet page and returns its resource ID. You can send this message explicitly or use the PropSheet\_IndexToId macro.
ms.assetid: c153675a-360f-4916-aa0b-500636dd9022
keywords:
- PSM_INDEXTOID message Windows Controls
topic_type:
- apiref
api_name:
- PSM_INDEXTOID
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_INDEXTOID message

Takes the index of a property sheet page and returns its resource ID. You can send this message explicitly or use the [**PropSheet\_IndexToId**](/windows/desktop/api/Prsht/nf-prsht-propsheet_indextoid) macro.

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

Returns the resource ID of the property sheet page specified by *wParam* if successful. Otherwise, it returns zero.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





