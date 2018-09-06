---
title: PSM_PAGETOINDEX message
description: Takes the HPROPSHEETPAGE handle of the property sheet page and returns its zero-based index. You can send this message explicitly or use the PropSheet\_PageToIndex macro.
ms.assetid: f893b504-7b46-4bce-9598-79522825d43c
keywords:
- PSM_PAGETOINDEX message Windows Controls
topic_type:
- apiref
api_name:
- PSM_PAGETOINDEX
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSM\_PAGETOINDEX message

Takes the HPROPSHEETPAGE handle of the property sheet page and returns its zero-based index. You can send this message explicitly or use the [**PropSheet\_PageToIndex**](/windows/desktop/api/Prsht/nf-prsht-propsheet_pagetoindex) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

HPROPSHEETPAGE handle to the property sheet page.

</dd> </dl>

## Return value

Returns the zero-based index of the property sheet page specified by *lParam* if successful. Otherwise, it returns -1.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





